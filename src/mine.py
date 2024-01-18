import gradio as gr
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings   #from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def get_pdf_text(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text() if page.extract_text() else ''
        text += "\n"  # Separator between PDFs
    return text

def handle_user_input(user_question, pdf_files):
    load_dotenv()
    raw_text = get_pdf_text(pdf_files)
    
    # Process raw text into chunks and create vector store
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    text_chunks = text_splitter.split_text(raw_text)
    embeddings = OpenAIEmbeddings()  #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)

    # Create conversation chain
    llm = ChatOpenAI()  # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), memory=memory)

    # Handle user question
    response = conversation_chain({'question': user_question})
    return response['chat_history'][-1].content

# Gradio Interface
iface = gr.Interface(
    fn=handle_user_input,
    inputs=[
        gr.components.Textbox(label="Ask a question about your documents"),
        gr.components.File(label="Upload your PDFs here", type="file", multiple=True, file_count="multiple")
    ],
    outputs="text",
    title="🅱🅻🅰🆀's Reader Bot 📖📚",
    description="Upload PDF documents and ask questions about their content"
)

if __name__ == "__main__":
    iface.launch()