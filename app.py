from flask import Flask, render_template, request, send_file
from moviepy.editor import VideoFileClip
import os
import uuid

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    video = request.files["video"]

    if video.filename == "":
        return "Please upload a valid video file"

    # Save uploaded video
    video_id = str(uuid.uuid4())
    temp_video = f"{video_id}.mp4"
    video.save(temp_video)

    # Convert to MP3
    output_file = f"{video_id}.mp3"
    clip = VideoFileClip(temp_video)
    clip.audio.write_audiofile(output_file)
    clip.close()

    # Remove original video
    os.remove(temp_video)

    # Send MP3 file to user
    return send_file(output_file, as_attachment=True)
    

if __name__ == "__main__":
    app.run(debug=True)
