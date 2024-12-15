from crewai_tools import YoutubeChannelSearchTool
from embedchain import App

from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv 
# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")




embedder={
                "provider":"huggingface", 
                "config":{
                    "model":"all-MiniLM-L6-v2", 
}, },
YT_tool = YoutubeChannelSearchTool(youtube_channel_handle="@Fireship",embedder=embedder,
)
