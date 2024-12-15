from tkinter import*
from tkinter import messagebox
from gtts import gTTS
import os
def convert_to_speech():
    text = text_input.get()
    if text:
        tts = gTTS(text=text, lang="en")
        filename = "output.mp3"
        tts.save(filename)
        os.system(f"start{filename}")
        def clear_text():
            text_input.delete(0,'end')
        root = Tk()
        root.title("Text to speech converting")
        root.geometry("400x500")
        Label(root, text="Enter text to convert to speech:").pack(pady=10)
        text_input = Entry(root, width=30)
        text_input.pack(pady=10)
        Button(root, text="convert to speech",comm=convert_to_speech).pack(pady=20)
        root.mainloop()