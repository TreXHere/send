from pyrogram import Client, filters
from pytube import YouTube
import os

# Replace these with your actual values
API_ID = "your_api_id"
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
CHANNEL_ID = "@your_channel"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(_, update):
    update.reply_text("Hi! Send me a YouTube link, and I will download and send the audio to the channel.")

@app.on_message(filters.text & ~filters.command)
def download_song(_, update):
    # Get the YouTube URL from the user
    youtube_url = update.text

    # Download the audio
    video = YouTube(youtube_url)
    audio_stream = video.streams.filter(only_audio=True).first()
    audio_path = f"{video.title}.webm"
    audio_stream.download(output_path=os.getcwd(), filename=video.title)

    # Send the audio file to the channel
    app.send_audio(chat_id=CHANNEL_ID, audio=audio_path)

if __name__ == "__main__":
    app.run()
