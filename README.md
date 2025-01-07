# RAG API Using Llama 3.2

This repository contains a modified implementation of a Retrieval-Augmented Generation (RAG) API using the Meta Llama 3.2 model. 
The modifications are designed for individuals with computational constraints of downloading the model locally or those encountering issues with the vLLM library.

## Original Code
The original implementation can be found [here](https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-2-rag-api?utm_source=akshay).

## Changes Made
- Switched to Groq or HuggingFace instead of vLLM.
- Used PyPDFLoader (pypdf) to load pdf files from directory instead of ingestion (ingest_pdfs).
- Changed Embedding Method from fastembed to HuggingFaceEmbeddings.
- Using ChromaDB instead of Qdrant for Vector Database for ease of setup locally.

  
## Advantages of This Approach
- **Lightweight Implementation:** Optimized to work on machines with limited computational resources.
- **Compatibility:** Avoids reliance on the vLLM library to reduce dependency overhead.
- **Faster Inference with Groq**: Ensures quicker model predictions and better throughput, making it more ideal for real-time use case.
- **Local Implementation:** Made to work on Windows locally instead of Lightning.ai studio.

## Requirements
To run this API, ensure you have the following installed:

- Python 3.9 or later
- Required Python libraries (listed in `requirements.txt`)

## Usage

### 1. Prepare the Environment
Create a virtual environment and activate it:
```bash
python3 -m venv env
env/scripts/activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Create a `./data` directory to store your PDF files.

### 3. Start the server
Run the server file using:
```bash
python server.py
```

This will create a `client.py` file, which you can then modify by referring to the provided code.


### 4. Test the API
Once the server is running successfully, open a new terminal in the project directory and test it out:



## Overview on Retrieval-Augmented Generation (RAG)
While traditional LLMs have made significant advancements since the introduction of the transformer architecture, they still face limitations. One key challenge is that they are often too generic and lack domain-specific expertise. For instance, while ChatGPT is incredibly useful, it may not provide the depth of knowledge required for tasks that demand specialized expertise—especially in areas that are highly technical or private in nature. This is where RAG steps in.

Retrieval-Augmented Generation (RAG) is a powerful framework that combines the strengths of both retrieval-based and generative models. By leveraging a retrieval mechanism, RAG can fetch relevant information from external sources, which is then used by the generative model to produce more accurate and contextually rich responses. This hybrid approach enhances the capabilities of language models, particularly in tasks where specific knowledge is required that may not be contained within the model's training data.


## Troubleshooting

### Issues Encountered
- **Out of Memory Errors:**
  - Running the `meta-llama/Llama-3.2-3B-Instruct` model locally using Hugging Face led to system crashes due to computational limitations.

- **Dependency Issues:**
  - After installing `vllm` using `pip install`, issues such as `no resource module found` occurred, prompting the decision to replace `vllm` entirely for this implementation.

## Contributing
Feel free to open issues or submit pull requests to improve this implementation. Contributions are welcome!


