from crewai import Task
from tools import YT_tool
from agents import content_researcher,content_writer


research_task= Task(
    description=("Identify the video {topic}"
    "Get detailed information about the video from youtube"
    ),
    
    expected_output="A comprehensive # paragraphs long report based on the {topic} of the video content",
    tools=[YT_tool],
    agent=content_researcher,
)


writing_task=Task(
    description=(
        "get the info from the youtube channel on the topic {topic}"
    ),
    expected_output="Summarize the info from the youtube channel video on the topic {topic} and create content for Blog",
    tools=[YT_tool],
    agent=content_writer,
    async_execution=False,
    output_file="new_content.md"
)