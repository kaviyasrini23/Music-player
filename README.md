# Python Music Player 🎵

A simple music player built using Python's `tkinter` for the GUI, `pygame.mixer` for handling audio, and `os` for file handling. This app allows you to select and play songs from a folder, adjust the volume, and control playback (play, pause, resume, stop, previous, next).

## Features

*Play, pause, resume, and stop music*
*Play previous or next song in the folder*
*Volume control with a slider*
*Displays available songs in a listbox*
*Simple and intuitive graphical interface*

# Requirements

 Python 3.x
  pygame library
  tkinter (comes bundled with Python)

# Installation

1. *Clone the repository:*

   bash:
   
   git clone https://github.com/YourUsername/music-player.git
   cd music-player
   

3. *Install required libraries:*

   You will need to install the pygame library if you haven't already:

   bash:
   pip install pygame
   

4. *Run the app:*

   Once the libraries are installed, you can run the Python script:

   bash:
   
   python music_player.py
   

#How to Use

1. *Open Folder*: Click the "Open Folder" button to select the folder containing your `.mp3` music files. The songs will be loaded into the listbox.
2. *Play Music*: Select a song from the list and click "Play".
3. *Control Playback*:
   
    *Pause*: Pause the currently playing song.
    *Resume*: Resume the paused song.
    *Stop*: Stop the music entirely.
    *Next*: Play the next song in the list.
    *Previous*: Play the previous song in the list.
   
5. *Adjust Volume*: Use the volume slider to increase or decrease the volume.
   
# Code Overview

# Libraries Used

  os: To handle the filesystem and retrieve audio files.
  tkinter For creating the GUI.
  pygame.mixer: For playing, pausing, stopping, and controlling audio.

### Functions

  open_folder(): Opens a folder dialog for selecting a directory containing `.mp3` files.
  play_music(): Plays the selected song.
  next_song(): Skips to the next song in the list.
  prev_song(): Goes back to the previous song in the list.
  pause_music(): Pauses the current song.
  resume_music(): Resumes the paused song.
  stop_music(): Stops the music.
  update_volume(): Adjusts the music volume based on the slider input.

### GUI Components

 *Listbox*: Displays the songs available in the selected folder.
 *Buttons*: Control playback (Play, Pause, Resume, Stop, Previous, Next).
 *Volume Slider*: Adjusts the playback volume.
  
# Screenshot

(Insert screenshot of the music player here)

# Contributing

Contributions are welcome! Feel free to fork this project, create an issue, or submit a pull request.

# License

This project is licensed under the MIT License.

