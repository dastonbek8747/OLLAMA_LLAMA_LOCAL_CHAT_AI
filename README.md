# 🦙 Ollama Llama Local Chat AI

**Ollama** orqali lokal ishlaydigan **Llama 3.2** modeli bilan kod yozish yordamchisi. Internet talab qilmaydi (lokal model).

---

## ✨ Imkoniyatlar

- 🦙 **Lokal model:** Ollama + Llama 3.2
- 💻 **Kod yozish:** foydalanuvchi talabiga ko'ra kod generatsiyasi
- 🔒 **Maxfiylik:** ma'lumotlar tashqi serverga yuborilmaydi
- 🎯 **Prompt shabloni:** til va vazifani aniqlash

---

## 🛠 Texnologiyalar

| Texnologiya | Maqsad |
|---|---|
| **Python 3.10+** | Asosiy til |
| **LangChain** | Prompt boshqaruvi |
| **Ollama** | Lokal LLM server |

---

## ⚙️ O'rnatish

**1. Ollama'ni o'rnating:** https://ollama.com

```bash
ollama pull llama3.2
```

**2. Python bog'liqliklari:**

```bash
git clone https://github.com/dastonbek8747/OLLAMA_LLAMA_LOCAL_CHAT_AI.git
cd OLLAMA_LLAMA_LOCAL_CHAT_AI
python -m venv venv
source venv/bin/activate
pip install langchain-core langchain-ollama
```

---

## ▶️ Ishga tushirish

```bash
python main.py
```

---

## 📁 Loyiha tuzilishi

```
OLLAMA_LLAMA_LOCAL_CHAT_AI/
└── main.py            # ChatPromptTemplate + OllamaLLM
```

---

## 📄 Litsenziya

Litsenziya ko'rsatilmagan.
