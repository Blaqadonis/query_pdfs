# 🅱🅻🅰🆀's Reader Bot 📖📚

## Introduction
🅱🅻🅰🆀's Reader Bot is an innovative web application designed to simplify the process of extracting and querying information from PDF documents. Utilizing OpenAI embeddings, it offers precise, context-aware responses to user queries.

## Features

### 1. **PDF Text Extraction**
   - **Function:** `get_pdf_text`
   - **Description:** Extracts text from uploaded PDF files, handling multiple documents and concatenating their texts for clarity.

### 2. **Text Chunking**
   - **Function:** `handle_user_input`
   - **Description:** Processes raw PDF text into manageable chunks, enabling efficient text handling and analysis.

### 3. **Vector Store Creation**
   - **Part of:** `handle_user_input`
   - **Description:** Converts text chunks into numerical embeddings using OpenAI embeddings for machine learning models.

### 4. **Conversational Retrieval Chain**
   - **Part of:** `handle_user_input`
   - **Description:** Combines vector store with a language model to generate responses to user queries.

### 5. **User Query Handling**
   - **Part of:** `handle_user_input`
   - **Description:** Answers queries related to uploaded PDFs using the conversational chain.

## Technology Stack
- OpenAI embeddings for text-to-embeddings conversion.
- HuggingFaceInstructEmbeddings for local, cost-free processing.
- Gradio for web interface.
- PyPDF2 for PDF text extraction.
- Python environment management with dotenv.
- FAISS for efficient similarity search in large databases.

## Getting Started
1. **Clone the Repository**
   - ```git clone https://github.com/Blaqadonis/query_pdfs.git```
2. **Install Dependencies**
   - ```pip install -r requirements.txt```
3. **Set Up Environment Variables**
   - Create a ```.env``` file with your `OPENAI_API_KEY` and `HUGGINGFACEHUB_API_TOKEN`.
4. **Run the Application**
   - Navigate to the `src` directory and run ```python mine.py```.

## Usage
1. **Start the Application**
   - Launch the Gradio interface.
2. **Upload PDF Documents**
   - Use the file upload feature to add your PDFs.
3. **Ask Questions**
   - Input your query related to the document's content.
4. **Receive Answers**
   - The application provides answers based on the uploaded document's content.
  
![Final Product Screenshot](https://github.com/Blaqadonis/query_pdfs/blob/main/imgs/final_product_2.png)



## Contributing
Contributions, suggestions, and issue reports are highly welcome. Please feel free to fork the repository, make changes, and submit pull requests.

