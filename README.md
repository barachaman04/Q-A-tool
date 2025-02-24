# Q-A-tool

# Web Content Q&A Tool

# Description

This is a web-based tool that allows users to enter one or more URLs, extract content from them, and ask questions based on the extracted information. The tool ensures that answers are strictly derived from the provided content without relying on external knowledge.

# Features

Ingest Web Content: Users can input one or multiple URLs to extract content.

Ask Questions: Users can query the extracted content and receive relevant answers.

User-Friendly Interface: Built using Streamlit, ensuring a clean and minimalistic UI.

Backend Processing: Uses a simple API to fetch and process webpage content.

# Installation & Setup (Local)
# Prerequisites
E
nsure you have the following installed on your system:

Python (>=3.8)
pip (Python package manager)

Step 1: Clone the Repository
sh
Copy
Edit
git clone <your-repository-url>
cd web-content-qa-tool

Step 2: Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

Step 3: Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt

Step 4: Run the Backend API
Start the API that will handle content extraction and answering questions:
sh
Copy
Edit
python backend.py

Step 5: Run the Frontend (Streamlit UI)
sh
Copy
Edit
streamlit run app.py

Step 6: Access the Tool
Once the app is running, open your browser and go to:

arduino
Copy
Edit
http://localhost:8501

# Deployment
For deploying this app, you can:

Use Streamlit Cloud (for UI hosting)
Deploy the backend on Flask/FastAPI with a cloud provider (AWS, Heroku, Render, etc.)
Folder Structure
graphql
Copy
Edit
web-content-qa-tool/
│── backend.py           # API for ingesting & processing content
│── app.py               # Streamlit UI for user interaction
│── requirements.txt     # Dependencies
│── README.md            # Documentation
│── venv/                # Virtual environment (optional)
Technologies Used
Frontend: Streamlit
Backend: Flask/FastAPI
Scraping: Requests, BeautifulSoup


<img width="1440" alt="Screenshot 2025-02-24 at 3 00 05 PM" src="https://github.com/user-attachments/assets/5bf8e2e8-667d-4259-bfd1-c7bec54c57e6" />
<img width="1440" alt="Screenshot 2025-02-24 at 3 00 15 PM" src="https://github.com/user-attachments/assets/a174e2df-6420-4d99-b7ed-0e0f62001c39" />

