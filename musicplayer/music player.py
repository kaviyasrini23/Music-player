import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Initialize the music player
mixer.init()

# Global variables
folder_path = "D:/Music"
current_volume = 0.5  # Default volume level
song_index = 0  # To keep track of the current song being played

# Function to open a folder and load audio files
def open_folder():
    global folder_path
    folder_path = filedialog.askdirectory()  # Store selected folder in global variable
    if folder_path:
        file_listbox.delete(0, tk.END)  # Clear the listbox before adding new songs
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp3"):
                file_listbox.insert(tk.END, filename)

# Function to play music
def play_music():
    global song_index
    selected_song = file_listbox.get(tk.ACTIVE)
    if selected_song and folder_path:  # Ensure both song and folder are selected
        song_index = file_listbox.curselection()[0]  # Get the index of the selected song
        song_path = os.path.join(folder_path, selected_song)
        mixer.music.load(song_path)
        mixer.music.set_volume(current_volume)  # Set volume when playing
        mixer.music.play()

# Function to play the next song
def next_song():
    global song_index
    song_index += 1
    if song_index >= file_listbox.size():  # Loop back to the first song if at the end
        song_index = 0
    file_listbox.selection_clear(0, tk.END)
    file_listbox.select_set(song_index)
    file_listbox.activate(song_index)
    play_music()

# Function to play the previous song
def prev_song():
    global song_index
    song_index -= 1
    if song_index < 0:  # Loop back to the last song if at the beginning
        song_index = file_listbox.size() - 1
    file_listbox.selection_clear(0, tk.END)
    file_listbox.select_set(song_index)
    file_listbox.activate(song_index)
    play_music()

# Function to pause music
def pause_music():
    mixer.music.pause()

# Function to resume music
def resume_music():
    mixer.music.unpause()

# Function to stop music
def stop_music():
    mixer.music.stop()

# Function to update the volume from the slider
def update_volume(val):
    global current_volume
    current_volume = float(val) / 100  # Convert slider value (0-100) to volume (0.0-1.0)
    mixer.music.set_volume(current_volume)

# Create the main window
root = tk.Tk()
root.title("Music Player")
root.geometry("500x500")
root.configure(bg="black")

# Frame for buttons and controls
control_frame = tk.Frame(root, bg="black")
control_frame.pack(pady=20)

# Previous, Play, Pause, Resume, Next, and Stop buttons
prev_button = tk.Button(control_frame, text="PREVIOUS", font=("Times New Roman", 12), command=prev_song, bg="purple", fg="white")
prev_button.grid(row=0, column=0, padx=10)

play_button = tk.Button(control_frame, text="PLAY", font=("Times New Roman", 12), command=play_music, bg="green", fg="white")
play_button.grid(row=0, column=1, padx=10)

pause_button = tk.Button(control_frame, text="PAUSE", font=("Times New Roman", 12), command=pause_music, bg="orange", fg="white")
pause_button.grid(row=0, column=2, padx=10)

resume_button = tk.Button(control_frame, text="RESUME", font=("Times New Roman", 12), command=resume_music, bg="blue", fg="white")
resume_button.grid(row=0, column=3, padx=10)

stop_button = tk.Button(control_frame, text="STOP", font=("Times New Roman", 12), command=stop_music, bg="red", fg="white")
stop_button.grid(row=0, column=4, padx=10)

next_button = tk.Button(control_frame, text="NEXT", font=("Times New Roman", 12), command=next_song, bg="purple", fg="white")
next_button.grid(row=0, column=5, padx=10)

# Volume control using a slider
volume_slider = tk.Scale(control_frame, from_=0, to=100, orient="horizontal", label="Volume", command=update_volume, bg="black", fg="white", troughcolor="gray")
volume_slider.set(current_volume * 100)  # Set the slider to the default volume
volume_slider.grid(row=1, column=0, columnspan=6, padx=10, pady=10)

# Frame for file selection
file_frame = tk.Frame(root)
file_frame.pack()

# Listbox to display the audio files
file_listbox = tk.Listbox(file_frame, width=50, height=10, bg="black", fg="white", selectbackground="gray")
file_listbox.pack(side="left", fill="y")

# Scrollbar for the Listbox
scrollbar = tk.Scrollbar(file_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

file_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=file_listbox.yview)

# Button to open a folder
open_folder_button = tk.Button(root, text="Open Folder", font=("Times New Roman", 12), command=open_folder, bg="lightblue", fg="black")
open_folder_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
