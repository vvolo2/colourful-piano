# 🎵 Note Visualiser

A colourful, interactive musical note visualiser built in Python as a final project for COMP112 (Introduction to Computer Science).

## What it does

Type musical notes and watch unique colour graphics and patterns appear on screen — each note generates its own distinct visual design, accompanied by its corresponding sound.

## Features

- Interactive note input — type a note and see it come to life
- Unique colour patterns and graphics for each of the 12 notes (A, A#, B, C, C#, D, D#, E, F, F#, G, G#)
- Audio playback using PyAudio — hear the note as it's drawn
- Visuals rendered with Python's `turtle` graphics module

## Requirements

- Python 3.x
- PyAudio (`pip install pyaudio`)
- The `.wav` note files included in this repository (one per note)

> **Note:** On macOS, installing PyAudio may require PortAudio. You can install it via Homebrew:
> ```bash
> brew install portaudio
> pip install pyaudio
> ```

## How to run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/note-visualiser.git
   cd note-visualiser
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python COMP112_final_VV.py
   ```

## Project structure

```
note-visualiser/
├── COMP112_final_VV.py   # Main program
├── pyaudio.py            # Audio helper module
├── requirements.txt      # Python dependencies
├── A.wav                 # Note audio files
├── As.wav
├── B.wav
├── C.wav
├── Cs.wav
├── D.wav
├── Ds.wav
├── E.wav
├── F.wav
├── Fs.wav
├── G.wav
└── Gs.wav
```

## About

This was created as a final project for COMP112 at university, exploring the intersection of music and visual art through code. Built with Python's built-in `turtle` graphics library and PyAudio for audio playback.
