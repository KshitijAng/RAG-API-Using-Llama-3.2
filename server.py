import litserve as ls
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings

class DocumentChatAPI(ls.LitAPI):
    def setup(self, device):
        # Use Groq for the LLM model
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key='GROQ_API_KEY',
            model_name="llama-3.2-3b-preview"
        )

        # Load Embedding model
        embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2")
        
        # Load documents and create vector store with Chroma
        loader = PyPDFLoader("./data")
        docs = loader.load_and_split()
        self.vectorstore = Chroma.from_documents(docs, embed_model)

        # Create Retrieval-based QA chain
        retriever = self.vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
        self.qa_chain = RetrievalQA.from_chain_type(llm=self.llm, retriever=retriever)

    def decode_request(self, request):
        return request["input"]

    def predict(self, query):
        # Perform retrieval and generate response
        response = self.qa_chain.run(query)
        return response

    def encode_response(self, output):
        return output


if __name__ == "__main__":
    api = DocumentChatAPI()
    server = ls.LitServer(api)
    server.run(port=8080)
