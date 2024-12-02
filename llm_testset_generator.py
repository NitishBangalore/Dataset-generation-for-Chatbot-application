import os
from langchain_community.document_loaders import (
    WebBaseLoader,
    UnstructuredExcelLoader,
    UnstructuredWordDocumentLoader,
)
from ragas.testset import TestsetGenerator
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = 'sk-...5aEA'

# Initialize Ragas components
generator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o"))
generator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())
generator = TestsetGenerator(llm=generator_llm, embedding_model=generator_embeddings)

loader = WebBaseLoader('https://journeyofquality.com/2024/11/17/evaluate-llm-applications-using-ragas/')

# if you want to load a word file use below code:
# loader = UnstructuredWordDocumentLoader('file_path_to_your_document')

# if you want to load an excel file use below code:
# loader = UnstructuredExcelLoader('file_path_to_your_document')

documents = loader.load()

dataset = generator.generate_with_langchain_docs(documents, testset_size=3)
df = dataset.to_pandas()

df.to_csv(os.path.join(os.path.dirname(__file__), 'test_datasets_llm_apps.csv'), index=False)
