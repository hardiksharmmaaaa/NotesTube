import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv() #load all the env Variables

import google.generativeai as genai 

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

prompt='''
You are an advanced summarization tool designed to transform lengthy YouTube video transcripts into concise, clear, and informative summaries. Your goal is to:

Capture the main points, insights, and any key actions mentioned in the video.
Keep the summary brief and to the point, focusing on what viewers need to know without excessive detail.
Organize information logically, starting with the main topic or theme of the video,
followed by essential details, tips, or steps in a sequential format.

Example Transcript Input: [Include a sample transcript for better calibration]

Desired Output Style: Provide a short summary of approximately 3-5 sentences. 
The summary should reflect the key ideas and conclusions presented in the video, leaving out filler language and irrelevant details.

Start with a summary statement: For instance, "This video discusses…" or "In this video, you will learn…" followed by the main points.

Output Format: Respond in full sentences with no bullet points or lists."

'''

def Create_content(transcript_text):
