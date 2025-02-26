# RAG API Using Llama 3.2

This repository contains a `modified implementation` of a Retrieval-Augmented Generation (RAG) API using the `Meta Llama 3.2 model`. 
The modifications are designed for individuals with computational constraints of downloading the model locally or those encountering issues with the vLLM library.

**Note: This solution works on Windows only, based on personal trial and error.**

## Original Code
The original implementation can be found [here](https://lightning.ai/lightning-ai/studios/deploy-a-private-llama-3-2-rag-api?utm_source=akshay) from [Akshay Pachaar](https://www.linkedin.com/posts/akshay-pachaar_i-created-a-100-private-llama-32-rag-api-activity-7279837399197605889-0NIK/?utm_source=share&utm_medium=member_android).

## Changes Made
- Switched to `Groq` or `HuggingFace` instead because of the recurring issue of `no resource module found` after installing vLLM library.
- Used `PyPDFLoader` (pypdf) to load pdf files from directory instead of ingestion (ingest_pdfs).
- Changed Embedding Method from fastembed to `HuggingFaceEmbeddings` because of prior experience.
- Using `ChromaDB` instead of Qdrant for Vector Database for ease of setup locally.

  
## Advantages of this Approach
- **Lightweight Implementation:** Optimized to work on machines with limited computational resources.
- **Flexibility:** With the rise of Open Source AI, users have a wide range of options to choose from in terms of model selection, including offerings from `Mistral`, `Meta`, and `HuggingFace`.
- **Faster Inference with Groq**: Ensures quicker model predictions and better throughput, making it more ideal for real-time use case.
- **Local Implementation:** Made to work on Windows locally instead of Lightning.ai studio.


## Possible Drawback
- **Security Concerns:** As the Groq API is used to address computational challenges, security may become a concern, since the data is no longer processed locally.

## Requirements
To run this API, ensure you have the following installed:

- Python 3.9 or later
- [litserve](https://github.com/Lightning-AI/LitServe)
- Required Python libraries (listed in `requirements.txt`)
- [Groq](https://console.groq.com/playground) API Key

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
![Project Logo](assets/API_Test.png "Project Logo")


## Overview on Retrieval-Augmented Generation (RAG)
While traditional LLMs have made significant advancements since the introduction of the transformer architecture, they still face limitations. One key challenge is that they are often too generic and lack domain-specific expertise. For instance, while ChatGPT is incredibly useful, it may not provide the depth of knowledge required for tasks that demand specialized expertise—especially in areas that are highly technical or private in nature. This is where RAG steps in.

Retrieval-Augmented Generation (RAG) is a powerful framework that combines the strengths of both retrieval-based and generative models. By leveraging a retrieval mechanism, RAG can fetch relevant information from external sources, which is then used by the generative model to produce more accurate and contextually rich responses. This hybrid approach enhances the capabilities of language models, particularly in tasks where specific knowledge is required that may not be contained within the model's training data.
![Project Logo](assets/RAG_Diagram.png "Project Logo")


## Troubleshooting

### Issues Encountered
- **Out of Memory Errors:**
  - Running the `meta-llama/Llama-3.2-3B-Instruct` model locally using Hugging Face led to system crashes due to computational limitations.

- **Dependency Issues:**
  - After installing `vllm` using `pip install`, issues such as `no resource module found` occurred, prompting the decision to replace `vllm` entirely for this implementation.

## Contributing
Feel free to open issues or submit pull requests to improve this implementation. Contributions are welcome!


