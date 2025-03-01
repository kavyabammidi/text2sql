# 📝 Text2SQL: AI-powered SQL Query Generator & Retriever

## 📌 Overview
Text2SQL is an AI-powered application that converts natural language queries into SQL statements and retrieves relevant data from a database. It leverages **Google Gemini AI** for query generation and **SQLite** for database storage.

---

## 🚀 Features
- Convert **English questions** into **SQL queries**.
- Retrieve data from **SQLite** database.
- Uses **Google Gemini AI** for query generation.
- User-friendly **Streamlit** web interface.

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python, Google Gemini AI
- **Database:** SQLite
- **Deployment:** Heroku / Hugging Face Spaces

---

## 📂 Project Structure
```
📦 TEXT2SQL
├── 📄 app.py            # Main application file
├── 📄 sql.py            # SQLite database setup
├── 📄 requirements.txt  # Dependencies
├── 📄 .env              # Environment variables (API Key)
└── 📄 README.md         # Project documentation
```

---

## 🔧 Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Text2SQL.git
cd Text2SQL
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and add your Google Gemini API key:
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

### **5️⃣ Run the Application**
```bash
streamlit run app.py
```

---

## 🖥️ Usage
1. Enter an **English question** (e.g., "List all students in Data Science class").
2. The **AI** generates an **SQL query**.
3. The **SQL query executes** and displays the **retrieved data**.

---

## 🌍 Deployment
### **Deploy to Heroku**
```bash
git init
git add .
git commit -m "Deploying Text2SQL"
heroku create text2sql-app
git push heroku main
heroku open
```

### **Deploy to Hugging Face Spaces**
1. Create a **new space** on [Hugging Face Spaces](https://huggingface.co/spaces).
2. Upload **app.py**, `requirements.txt`, and `.env`.
3. Commit changes and **Deploy**.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 🙌 Acknowledgments
- **Google Gemini AI** for query generation.
- **Streamlit** for the interactive UI.
- **SQLite** for lightweight database management.

---

### 🎯 Future Enhancements
- Support for **MySQL & PostgreSQL**.
- Implement **user authentication**.
- Improve **query optimization**.

💡 Feel free to contribute or suggest new features!
