import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st
import google.generativeai as genai
from google.generativeai.types import (
    BlockedPromptException,
    StopCandidateException,
    BrokenResponseError,
    IncompleteIterationError,
)
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# read all pdf files and return text


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# split text into chunks


def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000, chunk_overlap=1000)
    chunks = splitter.split_text(text)
    return chunks  # list of strings

# get embeddings for each chunk


def get_vector_store(chunks):
    if not chunks:
        st.error("No text chunks to process. The PDF might be empty or unreadable.")
        return False
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001")  # type: ignore
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
        return True
    except BlockedPromptException as e:
        st.error("The PDF content was flagged by Google's safety filters. Please try a different document.")
        print(f"Embedding blocked: {e}")
        return False
    except Exception as e:
        st.error(f"Error processing the PDF: {str(e)}")
        print(f"Embedding error: {e}")
        return False


def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                                   client=genai,
                                   temperature=0.3,
                                   )
    prompt = PromptTemplate(template=prompt_template,
                            input_variables=["context", "question"])
    chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)
    return chain


def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "upload some pdfs and ask me a question"}]


def user_input(user_question):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001")  # type: ignore

        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True) 
        docs = new_db.similarity_search(user_question)

        chain = get_conversational_chain()

        response = chain(
            {"input_documents": docs, "question": user_question}, return_only_outputs=True, )

        print(response)
        return response
    except BlockedPromptException as e:
        print(f"Prompt was blocked by Gemini: {e}")
        return {"output_text": "I'm sorry, but I cannot process this request. The content was flagged by Google's safety filters. Please try rephrasing your question."}
    except StopCandidateException as e:
        print(f"Response generation was stopped: {e}")
        return {"output_text": "I'm sorry, but the response generation was stopped due to content safety concerns. Please try rephrasing your question."}
    except (BrokenResponseError, IncompleteIterationError) as e:
        print(f"Response error: {e}")
        return {"output_text": "I'm sorry, but I encountered an error while generating the response. Please try again."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"output_text": f"An unexpected error occurred: {str(e)}. Please try again."}


def main():
    st.set_page_config(
        page_title="Gemini PDF Chatbot",
        page_icon="🤖"
    )

    # Sidebar for uploading PDF files
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader(
            "Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    if get_vector_store(text_chunks):
                        st.success("Done")
            else:
                st.error("Please upload at least one PDF file before processing.")

    # Main content area for displaying chat messages
    st.title("Chat with PDF files using Gemini🤖")
    st.write("Welcome to the chat!")
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    # Chat input
    # Placeholder for chat messages

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "upload some pdfs and ask me a question"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Get bot response for the user's question
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = user_input(prompt)
                placeholder = st.empty()
                full_response = ''
                if response and 'output_text' in response:
                    output_text = response['output_text']
                    # Handle both string responses (from error handling) and iterable responses
                    if isinstance(output_text, str):
                        full_response = output_text
                        placeholder.markdown(full_response)
                    else:
                        for item in output_text:
                            full_response += item
                            placeholder.markdown(full_response)
                        placeholder.markdown(full_response)
                    message = {"role": "assistant", "content": full_response}
                    st.session_state.messages.append(message)
                else:
                    st.error("Failed to get a valid response. Please try again.")


if __name__ == "__main__":
    main()
