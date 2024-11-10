import streamlit as st
from dotenv import load_dotenv
import os
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

load_dotenv()  # Load environment variables

import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi  # Retrieve transcript of YouTube videos

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Prompt to guide the summarizer model
prompt = "Summarize this YouTube video transcript in clear bullet points within 250 words."

# Function to extract transcript from YouTube video
def extract_transcript(url):
    try:
        video_id = url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript = " ".join([item["text"] for item in transcript_text])
        return transcript
        
    except Exception as e:
        st.error("Error retrieving transcript. Please check the URL.")
        return None

# Function to create summary with Gemini Model
def create_content(transcript_text):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt + "\n" + transcript_text)
    return response.text

# Function to generate PDF
def generate_pdf(summary):
    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=letter)
    pdf_canvas.drawString(72, 750, "Video Summary:")
    
    text_object = pdf_canvas.beginText(72, 730)
    text_object.setFont("Helvetica", 12)
    text_object.setLeading(14)
    text_object.textLines(summary)
    pdf_canvas.drawText(text_object)
    pdf_canvas.save()
    
    buffer.seek(0)
    return buffer

# Streamlit App Interface
st.title("NotesTube - YouTube Transcript to Detailed Notes Converter")
yt_link = st.text_input("Enter the YouTube Video Link")

if yt_link:
    video_id = yt_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript(yt_link)

    if transcript_text:
        summary = create_content(transcript_text)
        st.markdown("## Detailed Notes:")
        st.write(summary)

        # Generate and provide PDF download
        pdf_buffer = generate_pdf(summary)
        st.download_button(
            label="Download PDF",
            data=pdf_buffer,
            file_name="Video_Summary.pdf",
            mime="application/pdf"
        )
