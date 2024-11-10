# NotesTube - YouTube Transcript to Detailed Notes Converter

NotesTube is a web application built with Streamlit that converts YouTube video transcripts into summarized, bullet-point notes. This app uses the Gemini API for generative AI summarization and provides users with the option to download the summary as a PDF file.

## Features

- Extracts the transcript from a YouTube video.
- Generates a concise summary in bullet points.
- Allows users to download the summary as a PDF for offline reference.
- Displays the thumbnail of the input YouTube video for easy identification.

## Technology Stack

- **Streamlit** - Web application framework for Python.
- **YouTube Transcript API** - Retrieves transcripts for YouTube videos.
- **Google Gemini API** - Used for AI-based summarization.
- **ReportLab** - Generates PDF files of the summary.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/NotesTube.git
    cd NotesTube
    ```

2. **Install required dependencies**:
    Make sure you have Python 3.x installed, then install dependencies using:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file in the project root and add your Gemini API key:
    ```plaintext
    GEMINI_API_KEY=your_gemini_api_key
    ```

4. **Run the Streamlit app**:
    Start the app with:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Enter YouTube Video Link**:
   - Copy and paste the YouTube video link in the text box.
2. **Generate Notes**:
   - Click "Get Detailed Notes" to retrieve and summarize the video transcript.
3. **Download PDF**:
   - After the summary is generated, click "Download PDF" to save the notes.

## Project Structure

- `app.py`: Main application code for Streamlit.
- `requirements.txt`: Lists all Python libraries required to run the application.
- `.env`: Environment file to store the Gemini API key (not included for security).
  
## Dependencies

Install the following libraries:

- `streamlit`
- `dotenv`
- `google-generativeai`
- `youtube-transcript-api`
- `reportlab`

## Sample Screenshots

| Screenshot | Description |
|------------|-------------|
| ![Main Screen](screenshots/main_screen.png) | Main screen with video link input and thumbnail display |
| ![Summary Screen](screenshots/summary_screen.png) | Summarized notes with the option to download as PDF |

## Contributing

Feel free to fork the repository, create a new branch, and submit pull requests. For major changes, open an issue to discuss your ideas.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For any questions or feedback, reach out to [your-email@example.com].

