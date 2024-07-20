from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from ..utils import chroma

class ChunkingApproaches:
    @staticmethod
    def chunking_CharacterTextSplitter(pdf_doc):
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            separator="\n\n",
            chunk_size=100,
            chunk_overlap=100,
            is_separator_regex=False,
            model_name='text-embedding-3-small',
            encoding_name='text-embedding-3-small'
        )
        character_split_texts = text_splitter.split_text('\n\n'.join(pdf_doc))
        token_split_texts = chroma.sentence_transfomer_textsplitter(character_split_texts)
        return token_split_texts
    
    def chunking_RecursiveCharacterTextSplitter(pdf_doc):
        text = '\n\n'.join([page.page_content for page in pdf_doc])
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n","\n", " "],
            chunk_size = 200,
            chunk_overlap = 100,
            length_function = len(text),
            is_separator_regex=False
        )

        chunk_list = text_splitter.create_documents([text])
        return chunk_list