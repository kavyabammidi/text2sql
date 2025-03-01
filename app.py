from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY is None:
    st.error("API Key is missing! Please check your .env file.")
else:
    genai.configure(api_key=API_KEY)

# Function to generate SQL query from natural language input
def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Use latest model
        response = model.generate_content([prompt[0], question])
        return response.text.strip()  # Ensure clean output
    except Exception as e:
        st.error(f"Error fetching response from Gemini AI: {e}")
        return None

# Function to clean SQL query
def clean_sql_query(sql):
    # Correct the case for section values
    if "section=" in sql:
        section_value = sql.split("section=")[1].split("'")[1]
        if section_value.islower():
            sql = sql.replace(f"section='{section_value}'", f"section='{section_value.upper()}'")
    return sql

# Function to execute SQL query
def read_sql_query(sql, db):
    conn = None
    try:
        # Basic validation to ensure the query starts with SELECT
        if not sql.strip().lower().startswith("select"):
            st.error("Invalid SQL query. Only SELECT queries are allowed.")
            return []
        
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        st.error(f"Error executing SQL query: {e}")
        return []
    finally:
        if conn:
            conn.close()

# SQL Prompt for Gemini AI
prompt = [
    """
    You are an expert in converting English questions into SQL queries. 
    The database is named 'student.db' and has a table named 'student' with columns: 
    name, class, section, and marks.

    Rules:
    1. Always use lowercase for table and column names (e.g., `student`, `name`, `class`, `section`, `marks`).
    2. Always enclose string values in single quotes and match the exact case as stored in the database (e.g., 'A', 'B', 'C' for section).
    3. Do not include any unnecessary subqueries or complex logic unless explicitly required.
    4. Ensure the SQL query is simple, efficient, and directly executable.
    5. **Only return the SQL query. Do not include any explanations, additional text, or formatting.**
    6.remove all symbols from the query you have give only the query 
    Example 1:
    Question: "What is the average marks of all students?"
    SQL Command: SELECT AVG(marks) FROM student;

    Example 2:
    Question: "List all students in section A."
    SQL Command: SELECT * FROM student WHERE section='A';

    Example 3:
    Question: "What is the highest marks in the Data Science class?"
    SQL Command: SELECT MAX(marks) FROM student WHERE class='datascience';

    Example 4:
    Question: "What is the second highest marks in the Data Science class?"
    SQL Command: SELECT marks FROM student WHERE class='datascience' ORDER BY marks DESC LIMIT 1 OFFSET 1;
    """
]

# Streamlit App UI
st.set_page_config(page_title="SQL Query Generator & Retriever")
st.header("AI-powered SQL Query Generator")

# User Input
question = st.text_input("Enter your query:", key="input")
submit = st.button("Generate SQL & Retrieve Data")

# Handling Submission
if submit:
    response = get_gemini_response(question, prompt)

    if response:
        response = clean_sql_query(response)  # Clean the SQL query
        st.subheader("Generated SQL Query:")
        st.code(response, language="sql")  # Display the generated SQL query
        
        data = read_sql_query(response, "student.db")

        st.subheader("Query Results:")
        for row in data:
            st.write(row)  # Display query results