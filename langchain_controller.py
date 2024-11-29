from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()
groq_api_key_ = os.getenv("GROQ_API_KEY")

if not groq_api_key_:
    raise ValueError("GROQ_API_KEY was not found in file .env!")

class DefaultLLM():
    def __init__(self):
        # self.llm = ChatGroq(temperature=0, groq_api_key=groq_api_key_, model_name="llama3-groq-70b-8192-tool-use-preview")        
        self.llm = ChatGoogleGenerativeAI(temperature=0, google_api_key ="AIzaSyABteNnOamk5IH9FEFl6EEXiCmlNBlZUJg", model="gemini-1.5-pro")

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False
        )
    
    def single_forward(self, question):
        system = "You are a helpful assistant."
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([
            ("system", system), 
            ("human", human)
        ])

        chain = prompt | self.llm
        result = chain.invoke({"text": question})
        return result

