# 1. field to put job description 
# 2. upload resume
# 3. pdf to image - > processing -> gemini pro
# prompts Template
import streamlit as st
import os
import io
import base64
from PIL import Image
import fitz  # PyMuPDF instead of pdf2image
import google.generativeai as genai
from dotenv import load_dotenv

# Load Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

# Send image + prompt to Gemini
def get_gemini_response(input_text, pdf_content, prompt):
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')  # use gemini-1.5-pro if you have quota
        response = model.generate_content([
            {"text": input_text},
            pdf_content[0],
            {"text": prompt}
        ])
        return response.text
    except Exception as e:
        return f" Gemini API Error: {e}"

# 🖼 Convert first page of PDF to base64-encoded image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            if doc.page_count == 0:
                raise ValueError("PDF has no pages.")
            page = doc.load_page(0)
            pix = page.get_pixmap(dpi=150)
            img_byte_arr = pix.tobytes("jpeg")
            return [{
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }]
        except Exception as e:
            st.error(f" Error processing PDF: {e}")
            return []
    else:
        raise FileNotFoundError("No file uploaded")
# Streamlit UI
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Resume Expert")

input_text = st.text_area(" Paste Job Description:", key="input")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded successfully!")  
    
submit1 = st.button("Tell Me About My Resume")
submit2 = st.button("How Can I Improvise My Skills?")
submit3 = st.button("What are The Keywords that are missing ?")
submit4 = st.button("What is the percentage match?")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description for an engineering position.
Please share your professional evaluation on whether the candidate's profile aligns with the engineering role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a career coach and resume expert. Analyze the resume in the context of the provided engineering job description and suggest specific skills or areas the candidate should improve to increase their chances of selection.
"""

input_prompt3 = """
You are an ATS (Applicant Tracking System) expert. Compare the resume to the engineering job description and list the important keywords from the job description that are missing in the resume.
"""

input_prompt4 = """
You are an ATS (Applicant Tracking System) scanner with a deep understanding of engineering roles and deep ATS functionality.
Evaluate the resume against the provided engineering job description. Give the percentage match between the resume and the job description.
First, output the percentage, then list missing keywords, and finally provide your overall thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
