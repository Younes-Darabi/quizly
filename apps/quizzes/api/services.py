import yt_dlp
import os
import whisper
from google import genai


class Services:

    def make_standard_link(URL):
        if "youtu.be/" in URL:
            video_id = URL.split("/")[-1].split("?")[0]
        elif "youtube.com/watch?v=" in URL:
            video_id = URL.split("v=")[1].split("&")[0]
        else:
            raise ValueError("YouTube link is not valid")
        return f"https://www.youtube.com/watch?v={video_id}"

    def download_file_from_youtube(URL):
        os.makedirs("/audio_file/", exist_ok=True)
        tmp_filename = "/audio_file/audio.%(ext)s"
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": tmp_filename,
            "quiet": True,
            "noplaylist": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(URL, download=True)
            return ydl.prepare_filename(info)

    def convert_audio_to_text(AUDIO):
        model = whisper.load_model("turbo")
        result = model.transcribe(AUDIO)
        os.remove(AUDIO)
        return (result["text"])

    def make_questions_with_ai(TEXT):
        prompt = f"""
            Based on the following transcript, generate a quiz in valid JSON format.

            The quiz must follow this exact structure:

            {{
            "title": "Create a concise quiz title based on the topic of the transcript.",
            "description": "Summarize the transcript in no more than 150 characters. Do not include any quiz questions or answers.",
            "questions": [
                {{
                "question_title": "The question goes here.",
                "question_options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": "The correct answer from the above options"
                }},
                ... (exactly 10 questions)
            ]
            }}

            Requirements:
            - Each question must have exactly 4 distinct answer options.
            - Only one correct answer is allowed per question, and it must be present in 'question_options'.
            - The output must be valid JSON and parsable as-is (e.g., using Python's json.loads).
            - Do not include explanations, comments, or any text outside the JSON.

            Transcript:
            {TEXT}
            """
        api_key = os.getenv("GOOGLE_API_KEY")
        client = genai.Client(api_key=api_key)
        return client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
