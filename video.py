import os
from tkinter import *
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

def select_video():
    file = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv *.webm")]
    )
    video_path.set(file)

def select_output():
    folder = filedialog.askdirectory(title="Select Output Folder")
    output_folder.set(folder)

def convert_to_mp3():
    video = video_path.get()
    output = output_folder.get()

    # Check if video file is valid
    if not os.path.isfile(video):
        messagebox.showerror("Error", "Invalid video file!")
        return

    # Check if output folder is selected
    if not output:
        messagebox.showerror("Error", "Please select an output folder!")
        return

    # Automatically create output folder if it doesn't exist
    if not os.path.isdir(output):
        try:
            os.makedirs(output, exist_ok=True)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot create output folder:\n{str(e)}")
            return

    try:
        clip = VideoFileClip(video)
        output_file = os.path.join(
            output,
            os.path.basename(video).rsplit('.', 1)[0] + ".mp3"
        )
        clip.audio.write_audiofile(output_file)
        clip.close()

        messagebox.showinfo(
            "Success",
            f"Conversion Successful!\nFile saved as:\n{output_file}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# GUI Setup
root = Tk()
root.title("Universal Video to MP3 Converter")
root.geometry("500x300")
root.resizable(False, False)

video_path = StringVar()
output_folder = StringVar()

Label(root, text="Select Video File:", font=("Arial", 12)).pack(pady=5)
Entry(root, textvariable=video_path, width=50).pack()
Button(root, text="Browse", command=select_video).pack(pady=5)

Label(root, text="Select Output Folder:", font=("Arial", 12)).pack(pady=5)
Entry(root, textvariable=output_folder, width=50).pack()
Button(root, text="Browse", command=select_output).pack(pady=5)

Button(
    root,
    text="Convert to MP3",
    command=convert_to_mp3,
    bg="green",
    fg="white",
    font=("Arial", 12),
).pack(pady=20)

root.mainloop()
