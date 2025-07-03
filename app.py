import streamlit as st
from chatbot import load_pdf, create_vectorstore, create_qa_chain

st.set_page_config(page_title="PDF Q&A Bot")
st.title("📄 Chat with your PDF")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    if uploaded_file.size > 2 * 1024 * 1024:  # Limit to 2MB
        st.error("❌ File too large. Please upload a PDF under 2MB.")
    else:
        try:
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

            with st.spinner("Processing PDF..."):
                docs = load_pdf("temp.pdf")
                vectorstore = create_vectorstore(docs)
                qa = create_qa_chain(vectorstore)
                st.success("✅ PDF processed successfully!")

                question = st.text_input("Ask a question about the document:")
                if question:
                    answer = qa.run(question)
                    st.markdown("**Answer:**")
                    st.write(answer)
        except Exception as e:
            st.error(f"🚨 Error reading PDF: {str(e)}")
