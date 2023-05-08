from tkinter import *
from pytube import YouTube
import threading

# Function to download the video or audio
def download_video():
    # Get the URL from the text entry widget
    url = url_entry.get()

    # Create a YouTube object from the URL
    yt = YouTube(url)

    if mode_var.get() == "video":
        # Get the selected resolution from the option menu
        selected_resolution = resolution_var.get()

        # Get the corresponding video stream
        stream = yt.streams.filter(res=selected_resolution).first()

    elif mode_var.get() == "audio":
        # Get the audio stream
        stream = yt.streams.filter(only_audio=True).first()

    # Download the video in a separate thread
    status_label.config(text="Downloading...")
    t = threading.Thread(target=download_video_thread, args=(stream,))
    t.start()

# Function to download the video in a separate thread
def download_video_thread(stream):
    stream.download()
    status_label.config(text="Download complete!")

# Create the main window
root = Tk()
root.title("YouTube Downloader")
root.geometry("500x400")
root.resizable(False, False)
root.config(bg="#303030")

# Set the font style
font_style = ("Helvetica", 12)

# Create the title label
title_label = Label(root, text="YouTube Downloader", font=("Helvetica", 18), fg="white", bg="#303030")
title_label.pack(pady=20)

# Create the mode selection frame
mode_frame = Frame(root, bg="#303030")
mode_frame.pack()

# Create the video mode button
video_button = Button(mode_frame, text="Video", font=font_style, width=10, bg="#212121", fg="white", bd=0, activebackground="#424242", activeforeground="white", relief="flat", command=lambda: mode_var.set("video"))
video_button.pack(side=LEFT, padx=(0, 10))

# Create the audio mode button
audio_button = Button(mode_frame, text="Audio", font=font_style, width=10, bg="#212121", fg="white", bd=0, activebackground="#424242", activeforeground="white", relief="flat", command=lambda: mode_var.set("audio"))
audio_button.pack(side=LEFT)

# Create the URL entry widget
url_label = Label(root, text="Enter the YouTube video URL:", font=font_style, fg="white", bg="#303030")
url_label.pack(pady=(20, 5))
url_entry = Entry(root, width=50, font=font_style)
url_entry.pack(pady=5)

# Create the resolution selection widget (for video mode only)
resolution_frame = Frame(root, bg="#303030")
resolution_frame.pack()

resolution_label = Label(resolution_frame, text="Select the resolution:", font=font_style, fg="white", bg="#303030")
resolution_label.pack(side=LEFT, padx=(0, 10))

resolutions = ["360p", "720p", "1080p"]
resolution_var = StringVar()
resolution_var.set(resolutions[0])
resolution_option_menu = OptionMenu(resolution_frame, resolution_var, *resolutions)
resolution_option_menu.config(font=font_style, bg="#212121", fg="white", bd=0, activebackground="#424242", activeforeground="white")
resolution_option_menu.pack(side=LEFT)

# Create the download button
download_button = Button(root, text="Download", command=download_video, font=font_style, bg="#4CAF50", fg="white", padx=20, pady=10)

# Create the status label
status_label = Label(root, text="", font=font_style, fg="white", bg="#303030")
status_label.pack(pady=10)

# Create the tabs
tab_frame = Frame(root, bg="#303030")
tab_frame.pack(pady=10)

mode_var = StringVar()
mode_var.set("video")

video_tab = Button(tab_frame, text="Video", font=font_style, bg="#212121", fg="white", bd=0, activebackground="#424242", activeforeground="white", relief="flat", command=lambda: mode_var.set("video"))

audio_tab = Button(tab_frame, text="Audio", font=font_style, bg="#212121", fg="white", bd=0, activebackground="#424242", activeforeground="white", relief="flat", command=lambda: mode_var.set("audio"))

# Create the download button
download_button = Button(root, text="Download", font=font_style, bg="#212121", fg="white", bd=0, activebackground="#424242", activeforeground="white", relief="flat", command=download_video)
download_button.pack(pady=10)

# Create the mode label
mode_label = Label(root, text="Mode: video", font=font_style, fg="white", bg="#303030")
mode_label.pack()

# Function to update the mode label
def update_mode_label():
    mode = "video" if mode_var.get() == "video" else "audio"
    mode_label.config(text=f"Mode: {mode}")
    
# Bind the update_mode_label function to the mode variable
mode_var.trace("w", lambda *args: update_mode_label())

# Start the main event loop
root.mainloop()