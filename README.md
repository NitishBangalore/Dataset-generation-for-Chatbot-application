# Dataset-generation-for-Chatbot-application
Test dataset generation using Ragas to test the Chatbot application.
Certainly! Here's a more concise version of the README with the implementation code removed, while still maintaining the key details:

---

# Test Dataset Generation for Chatbot LLM Applications

This project demonstrates how to generate systematic test datasets for evaluating **Retrieval-Augmented Generation (RAG)** models, particularly for **Chatbot LLM applications**. Generating test datasets (queries) for evaluating LLMs is typically a time-consuming task that requires manual creation of queries from various data sources like URLs or documents. This project automates that process using the **Ragas toolkit**.

## Overview

Test dataset generation involves creating systematic, reusable test cases for **RAG models**. RAG models combine **retrieval mechanisms** with **generative capabilities** and are commonly used in applications such as:

- **Question-Answering**
- **Knowledge-based reasoning**
- **AI-driven chatbots**

The goal of this project is to automate the creation of test datasets (queries) for Chatbot LLM testing using URLs and documents.

## Prerequisites

### 1. Install Python
Ensure that **Python 3.12** or above is installed. You can download Python from the official site:
- [Download Python](https://www.python.org/downloads/)

### 2. Install an IDE
You can use any Python IDE. We recommend **PyCharm**:
- [Download PyCharm](https://www.jetbrains.com/pycharm/)

### 3. Install Required Libraries
Install the necessary Python libraries:
```bash
pip install langchain langchain_openai xlsxwriter ragas nltk unstructured RapidFuzz python-docx networkx openpyxl
```

### 4. Set Up OpenAI API Key
You'll need to set your **OpenAI API Key** to use the OpenAI LLM evaluator. Get your API key from [OpenAI](https://platform.openai.com/api-keys) and export it in your code.

```python
os.environ["OPENAI_API_KEY"] = 'sk-...5aEA'
```

## How It Works

The code uses the **Ragas toolkit** and **Langchain** to automatically generate test queries from documents or URLs. You can choose the data source you want to use for test dataset generation:

1. **URL**: Use `WebBaseLoader` to load content from a URL.
2. **Word/Excel Document**: Use `UnstructuredWordDocumentLoader` or `UnstructuredExcelLoader` to load documents from your local machine.

Once the data is loaded, the **TestsetGenerator** uses an LLM evaluator (e.g., OpenAI's GPT-4) to generate queries based on the content. The resulting dataset is saved as a CSV file containing:

- `user_input` (generated query)
- `reference_context` (context for the query)
- `reference` (ground truth)
- `synthesizer_name` (the LLM model used)

## Sample Output (CSV)

The generated CSV file might look like this:

| user_input      | reference_context                 | reference               | synthesizer_name |
|-----------------|-----------------------------------|-------------------------|------------------|
| What is RAG?    | RAG combines retrieval and generative capabilities | Retrieval-Augmented Generation | gpt-4o           |
| How does Ragas work? | Ragas helps in generating test datasets for LLMs | Ragas for LLM testing   | gpt-4o           |
| What is OpenAI? | OpenAI provides API for GPT models | OpenAI API Key          | gpt-4o           |

## Running the Code

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/test-dataset-generation.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python generate_testset.py
   ```

The script will generate a CSV file (`test_datasets_llm_apps.csv`) with the test queries.





## Acknowledgments

- [Ragas toolkit](https://github.com/Ragas) for test dataset generation
- [Langchain](https://www.langchain.com/) for LLM tools integration
- OpenAI for providing the API for LLMs

