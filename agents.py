from crewai import Agent

from tools import YT_tool
import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv 
# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")


# Define Hugging Face Embedder Config
embedder = {
    "provider": "huggingface",
    "config": {
        "model": "all-MiniLM-L6-v2",
    }
}

# Define LLM
llm = ChatGroq(model="groq/llama3-8b-8192")

# Content Researcher Agent
content_researcher = Agent(
    role="Content researcher of YouTube videos",
    goal="Get relevant video content for the topic {topic} from the YouTube channel",
    verbose=True,
    memoryview=True,
    backstory="This person is an expert researcher and is highly accurate.",
    tools=[YT_tool],
    allow_delegation=True,
    embedder_config=embedder,
    llm=llm,
)

# Content Writer Agent
content_writer = Agent(
    role="Content writer",
    goal="Write detailed and unbiased content for the provided topic using the gathered research.",
    verbose=True,
    memoryview=True,
    backstory="This person is a content writer and is highly unbiased.",
    tools=[YT_tool],
    allow_delegation=False,
    embedder_config=embedder,
    llm=llm,
)
