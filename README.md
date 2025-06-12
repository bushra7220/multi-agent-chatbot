# 📘 Multi-Agent Chatbot using LangChain & OpenAI

This project is a multi-agent chatbot system that performs:

- 🤖 **Question Answering**
- 📝 **Summary Generation**
- 🎯 **MCQ Generation**

It uses **LangChain**, **FAISS vector store**, and **OpenAI models (gpt-3.5 / gpt-4)** to process PDF-based educational content.

---

## 🔧 Project Structure

```
multi-agent-chatbot/
├── app/
│   └── ui.py
├── agents/
│   ├── question_answer_agent.py
│   ├── summary_agent.py
│   └── mcq_generator.py
├── config/
│   └── config.py
├── myutils/
│   ├── pdf_loader.py
│   └── vectorestore.py
├── prompts/
│   ├── qa_prompt.py
│   ├── summary_prompt.py
│   └── mcq_prompt.py
├── data/
│   └── physics-textbook.pdf
├── requirements.txt
└── README.md
```

---

## 🚀 How It Works

1. **Load and chunk a textbook PDF**
2. **Embed chunks into FAISS vector store**
3. **Run one of three agents**:
   - Question answering via `create_retrieval_chain`
   - Summarization using custom prompt and LLM
   - MCQ generation with customizable output

Each agent has a dedicated `build_*_agent()` function with its own prompt.

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/bushra7220/multi-agent-chatbot.git
cd multi-agent-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key

Create a `.env` file:

```env
OPENAI_API_KEY=your-openai-key-here
```

### 4. Run the Streamlit app

```bash
streamlit run app/ui.py
```

---

## ✅ Features

- 🔍 **Question Answering:** Retrieves and answers contextually based on the textbook
- ✍️ **Summarization:** Uses `create_stuff_documents_chain` to summarize large chunks
- 📚 **MCQ Generator:** Dynamically generates all possible MCQs from content
- 📎 **Model Selection:** Switch between `gpt-3.5` and `gpt-4`
- ✅ **Chunking & Retrieval:** Uses FAISS + OpenAIEmbeddings
- 🧠 **No External Search APIs** like Tavily
- 🛠 **Custom Prompt Templates** for full control

---

## 🧠 Technologies Used

- **LangChain**
- **OpenAI GPT-3.5 / GPT-4**
- **FAISS for Vector Search**
- **Streamlit UI**