import streamlit as st
import requests

st.set_page_config(page_title="Web Content Q&A", layout="centered")

# Title
st.title("Web Content Q&A Tool")

# Step 1: Input URLs
st.subheader("Step 1: Enter URLs")
urls = st.text_area("Enter one or more URLs (one per line):", height=150)

if st.button("Ingest Content", key="ingest"):
    if urls.strip():
        response = requests.post("http://127.0.0.1:5000/ingest", json={"urls": urls.split("\n")})
        if response.status_code == 200:
            st.success("Content ingested successfully! Now ask questions.")
            st.session_state["ingested"] = True
        else:
            st.error("Failed to ingest content.")
    else:
        st.warning("Please enter at least one URL.")

# Step 2: Ask Questions
st.subheader("Step 2: Ask a Question")
question = st.text_input("Ask based on the ingested content:")

if st.button("Get Answer", key="ask") and question.strip():
    if st.session_state.get("ingested", False):
        response = requests.post("http://127.0.0.1:5000/ask", json={"question": question})
        answer = response.json().get("answer", "No relevant information found.")
        st.markdown(f"*Answer:* {answer}")
    else:
        st.warning("Please ingest content first.")

# Footer
st.markdown("---")
st.caption("Built By Aman")

