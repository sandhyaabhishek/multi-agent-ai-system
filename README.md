# Multi-Agent AI System 🤖

A Python-based **Multi-Agent AI system** where multiple AI agents collaborate to complete a task.
The system demonstrates how **AI agents can work together in a workflow** to research, write, and review content automatically.

This project uses **LangChain and a local LLM (Ollama)** to simulate agent collaboration similar to modern AI agent frameworks.

---

## 🚀 Features

* Research Agent gathers key information about a topic
* Writer Agent generates structured content based on research
* Reviewer Agent improves and refines the generated content
* Demonstrates **multi-agent collaboration architecture**
* Runs locally using **Ollama LLM**

---

## 🧠 Architecture

Topic Input
↓
Research Agent
↓
Writer Agent
↓
Reviewer Agent
↓
Final Article Output

---

## 🛠 Tech Stack

* Python
* LangChain
* Ollama (Local LLM)
* AI Agents Architecture

---

## 📂 Project Structure

```
multi-agent-ai
│
├── main.py
├── agents.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository:

```
git clone https://github.com/sandhyaabhishek/multi-agent-ai-system.git
```

Navigate into the project:

```
cd multi-agent-ai-system
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶ Run the Project

Start Ollama model:

```
ollama run llama3
```

Run the AI agents:

```
python main.py
```

Enter a topic when prompted.

Example:

```
Enter topic: Artificial Intelligence in healthcare
```

The agents will automatically:

1. Research the topic
2. Generate an article
3. Review and improve the article

---

## 📸 Example Output

```
Enter topic: Artificial Intelligence in healthcare

Research Result:
AI is transforming healthcare through predictive analytics...

Draft Article:
Artificial Intelligence is revolutionizing healthcare...

Final Article:
Artificial Intelligence is significantly transforming healthcare...
```

---

## 📈 Learning Outcomes

This project demonstrates:

* Multi-agent AI architecture
* AI task decomposition
* LLM-powered automation workflows
* Prompt engineering for agent collaboration

---

## 📌 Future Improvements

* Add a web interface using **Streamlit**
* Implement more specialized AI agents
* Add document retrieval (RAG) support
* Integrate external APIs for research

---

## 👨‍💻 Author

Abhishek Gautam
B.Tech Information Technology

GitHub: https://github.com/sandhyaabhishek
LinkedIn: https://linkedin.com/in/abhishek-gautam

