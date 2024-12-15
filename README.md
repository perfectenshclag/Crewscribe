# Crewscribe
## 🎉 Automation with CrewAI 🚀

This project showcases an exciting way to automate content creation using CrewAI! It fetches and analyzes YouTube videos from a specific channel and creates a polished blog post based on the insights. Get ready for a fun ride through the world of AI, automation, and creativity! 🌟

---

## 🌈 Workflow Overview

1. 🧠 **Embedder Configuration**: Uses HuggingFace's "all-MiniLM-L6-v2" model for semantic understanding. 
2. 🤖 **Language Model (LLM)**: ChatGroq ("groq/llama3-8b-8192") powers the natural language processing for our smart agents.
3. 📺 **YouTube Search Tool**: Fetches content from a specific YouTube channel (e.g., `@Fireship`).
4. 🕵️‍♂️ **Agents**:
    - **Content Researcher**: Gathers detailed video insights.
    - **Content Writer**: Transforms research into a captivating blog post. ✍️
5. ⚙️ **Tasks and CrewAI**: Executes tasks in sequence, ensuring a smooth and seamless workflow. 

---

## 💡 Technologies Used

| 🛠️ **Technology**       | 🌟 **Description**                                                                                                    |
|--------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Python**               | The brain behind this project! 🐍                                                                                  |
| **dotenv**               | Keeps API keys secure and hidden. 🗝️                                                                               |
| **CrewAI**               | Orchestrates intelligent agents and processes. 🧩                                                                  |
| **HuggingFace**          | Provides powerful embeddings for analyzing content. 🤗                                                             |
| **ChatGroq**             | A robust language model that powers our agents. 🚀                                                                |
| **YouTube API**          | Enables automated fetching of video data from YouTube. 📹                                                         |

---

## 🚀 How to Get Started

1. **Install Dependencies**:
   ```bash
   pip install crewai huggingface_hub groq-client python-dotenv
   ```
2. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your API keys like this:
     ```
     GROQ_API_KEY=<your_groq_api_key>
     HF_TOKEN=<your_huggingface_token>
     ```
3. **Run the Project**:
   ```bash
   python project.py
   ```
4. **Get Your Results**:
   - The blog content will be saved in `new_content.md`. 🎉

---

## 🌟 How It Works

1. 🔐 **Environment Setup**: Loads API keys securely.
2. 🎯 **Agent Configuration**:
    - The **Content Researcher** digs into YouTube for relevant insights. 🔍
    - The **Content Writer** crafts an engaging blog post. ✍️
3. 📋 **Task Execution**:
    - CrewAI manages sequential task execution.
4. 📝 **Output Generation**:
    - The final blog post is saved as `new_content.md`. 🥳

