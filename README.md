# 🧠 NIW RAG Boilerplate

This project is a **Retrieval-Augmented Generation (RAG)** pipeline for generating **National Interest Waiver (NIW)** letters using LLMs (e.g., GPT-4) and example-based semantic search. It leverages **LlamaParse**, **LlamaIndex**, and **OpenAI** to automate the drafting of recommendation letters based on user profiles and previously approved NIW submissions.

---

## 📁 Project Structure

```
niw_rag_boilerplate/
├── app/
│   ├── api.py              # (To be implemented) FastAPI backend
│   ├── generator.py        # GPT-4 based letter generator
├── backend/
│   ├── parse.py            # Uses LlamaParse to extract clean text from PDFs
│   ├── embed.py            # Embeds parsed documents using LlamaIndex
│   ├── query.py            # Retrieves relevant chunks from vector store
├── data/
│   └── accepted_niw_letters/   # Store sample letters (PDF or DOCX)
├── scripts/
│   ├── test_ingest.py      # Test script to parse, embed, query, and generate
├── .env                    # API keys for OpenAI and LlamaCloud
├── requirements.txt        # Python dependencies
└── README.md               # You're here!
```

---

## ⚙️ Features

- ✅ Parse accepted NIW letters using **LlamaParse**
- ✅ Create semantic embeddings with **LlamaIndex**
- ✅ Query vector store using user profile
- ✅ Generate a custom NIW letter with **OpenAI GPT-4**
- 📦 Modular architecture, production-ready
- 🧪 Ideal for use in legaltech, immigration, and document automation products

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/niw_rag_boilerplate.git
cd niw_rag_boilerplate
```

### 2. Set up environment

Create a `.env` file in the root:

```env
OPENAI_API_KEY=your-openai-api-key
LLAMA_CLOUD_API_KEY=your-llama-cloud-api-key
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add sample data

Put accepted NIW letters into:

```
data/accepted_niw_letters/
```

PDF and DOCX formats are supported.

### 5. Run the pipeline

```bash
python -m scripts.test_ingest
```

You should see relevant snippets printed, followed by a fully generated NIW letter.

---

## 🧪 Coming Soon

- [ ] FastAPI REST API (`app/api.py`)
- [ ] Frontend UI (e.g., Streamlit or Next.js)
- [ ] DOCX/PDF output
- [ ] Feedback and revision loop

---

## 📚 Tech Stack

- [LlamaParse](https://docs.llamaindex.ai/en/stable/api/llamaparse/)
- [LlamaIndex](https://docs.llamaindex.ai/)
- [OpenAI GPT-4](https://platform.openai.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Chroma](https://www.trychroma.com/) (optional)

---

## 🤝 Contributing

Pull requests are welcome! Please follow the existing file structure and comment clearly. We’re especially open to contributors with experience in:
- NLP / RAG
- Immigration legal tech
- FastAPI or frontend frameworks

---

## 📝 License

MIT License. Use freely, improve boldly.

---

## 💡 Inspiration

This tool is designed to help automate expert-level document drafting for U.S. immigration, specifically for Korean professionals applying under the EB-2 NIW category.