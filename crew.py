import os
from dotenv import load_dotenv
import streamlit as st
from crewai import Agent, Task, Crew, Process
from crewai_tools import YoutubeChannelSearchTool, RagTool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

# Streamlit app title
st.title("YouTube Content Research & Writing Assistant")

# Define Embedder Configuration
embedder = {
    "provider": "huggingface",
    "config": {
        "model": "all-MiniLM-L6-v2",
    }
}
rag = RagTool()

# Define LLM
llm = ChatGroq(model="groq/llama3-8b-8192")

# Define the YouTube Tool
YT_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@{channel}",
    embedder=embedder,
)

# Define Agents
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

content_writer = Agent(
    role="Content writer",
    goal="Write detailed and unbiased content for the provided topic using the gathered research.",
    verbose=True,
    memoryview=True,
    backstory="This person is a content writer and is highly unbiased.",
    tools=[],  # No tools needed as it summarizes from research.
    allow_delegation=False,
    embedder_config=embedder,
    llm=llm,
)

# Define Tasks
research_task = Task(
    description="Identify videos for the topic {topic} and extract detailed information.",
    expected_output="A comprehensive multi-paragraph report on the {topic} from YouTube content.",
    tools=[YT_tool],
    agent=content_researcher,
)

writing_task = Task(
    description="Summarize the researched video content into a blog article on the {topic}.",
    expected_output="A detailed blog post summarizing insights on the topic {topic}.",
    tools=[],  # No tools used, relies on research_task output
    agent=content_writer,
    async_execution=False,
    output_file="new_content.md",
)

# Define Crew
crew = Crew(
    embedder=embedder,
    agents=[content_researcher, content_writer],
    tasks=[research_task, writing_task],
    processes=Process.sequential,  # Sequential execution
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
)

# Streamlit Interface
st.header("Research a Topic and Generate Blog Content")
topic = st.text_input("Enter the topic for research:")


channel = st.text_input("Enter the YouTube channel's name:")

if st.button("Generate Content"):
    if topic:
        with st.spinner("Processing... Please wait."):
            result = crew.kickoff(inputs={"topic": topic})
        st.success("Process completed!")
        
        # Display results
        st.subheader("Generated Blog Content")
        st.write(result)
    else:
        st.error("Please enter a topic before proceeding.")
