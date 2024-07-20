import warnings
warnings.filterwarnings("ignore")
# from langchain.document_loaders import DirectoryLoader
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import weaviate
from langchain.vectorstores import Weaviate
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from dotenv import dotenv_values

env_vars = dotenv_values('.env')
OPENAI_API_KEY = env_vars.get('OPENAI_API_KEY')
WEAVIATE_KEY = env_vars.get('WEAVIATE_KEY')
WEAVIATE_CLUSTER = env_vars.get('WEAVIATE_CLUSTER')


# def pdf_loader(file_path):
#     loader = DirectoryLoader(file_path, glob="**/*.pdf")
#     data = loader.load()
#     # print(f'You have {len(data)} documents in your data')
#     # print(f'There are {len(data[0].page_content)} characters in your document')
#     # print(data)
#     return data

def pdf_reader(file_path):
    reader = PdfReader(file_path)
    pdf_texts = [p.extract_text().strip() for p in reader.pages]
    # Filter the empty strings
    pdf_texts = [text for text in pdf_texts if text]
    # print(pdf_texts[0])
    return pdf_texts

# def text_splitter(data):
#     ### TESTING SPLITTING: splitting our text we want to do that because each chunk of text will be comprised in a vector and we don't want them to be too big because otherwise they would be two large pieces of text to put in rgbt model and actuall the gpt model has limited input size so once you enter a large number of inputs or tokens into the gpt model it will crash so we can't make your chunks too big otherwise they won't be suitable as an input for GPT 
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#     docs = text_splitter.split_documents(data)
#     # print(docs)
#     return docs

def text_splitter_chunks(pdf_texts):
    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=0
    )
    character_split_texts = character_splitter.split_text('\n\n'.join(pdf_texts))
    # print(character_split_texts[10])
    # print(f"\nTotal chunks: {len(character_split_texts)}")
    return character_split_texts


def embedding():
    ### EMBEDDING
    embeddings = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY)
    # print(embeddings)
    return embeddings
    

def connect_vectordb():
    ### VECTOR DATABASE STORAGE WEAVIATE  
    # connect Weaviate Cluster
    auth_config = weaviate.AuthApiKey(api_key=WEAVIATE_KEY)
    WEAVIATE_URL = WEAVIATE_CLUSTER
    client = weaviate.Client(
        url=WEAVIATE_URL,
        additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY},
        # embedded_options=None,
        auth_client_secret=auth_config,
        startup_period=10
    )
    return client
    # print(client)

def store_to_vector(client):
    # define input structure
    client.schema.delete_all()
    client.schema.get()
    schema = {
        "classes": [
            {
                "class": "Chatbot",
                "description": "Documents for chatbot",
                "vectorizer": "text2vec-openai",
                "moduleConfig": {"text2vec-openai": {"model": "ada", "type": "text"}},
                "properties": [
                    {
                        "dataType": ["text"],
                        "description": "The content of the paragraph",
                        "moduleConfig": {
                            "text2vec-openai": {
                                "skip": False,
                                "vectorizePropertyName": False,
                            }
                        },
                        "name": "content",
                    },
                ],
            },
        ]
    }

    client.schema.create(schema)
    vectorstore = Weaviate(client, "Chatbot", "content", attributes=["source"])
    return vectorstore
    # print(vectorstore)

def simlarity_search(docs, vectorstore):
    # load text into the vectorstore
    text_meta_pair = [(doc.page_content, doc.metadata) for doc in docs]
    texts, meta = list(zip(*text_meta_pair))
    return vectorstore.add_texts(texts, meta)
    # print(vectorstore.add_texts(texts, meta))

def start_chat(query, vectorstore):
    #chatbot
    # query = "Under what circumstances and to what extent the Sellers are responsible for a breach of representations and warranties?"
    
    # retrieve text related to the query
    docs = vectorstore.similarity_search(query, k=4)
    # define chain
    chain = load_qa_chain(
        OpenAI(openai_api_key = OPENAI_API_KEY,temperature=0),
        chain_type="stuff")
    return chain.run(input_documents=docs, question=query)
    # print(chain.run(input_documents=docs, question=query))

