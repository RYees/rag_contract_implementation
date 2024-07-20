from langchain.text_splitter import CharacterTextSplitter
from ..utils import chroma

class CrossEncoderReranker:
    @staticmethod
    def chunking_strategy(pdf_doc):
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