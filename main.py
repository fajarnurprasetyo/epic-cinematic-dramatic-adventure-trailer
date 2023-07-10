#!venv/bin/python3
import os
import sys
import time
from os import path
from tkinter import *

from pygame import mixer
from pygame.mixer import music

if __name__ == '__main__':
    bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
    audio_start_file = path.join(bundle_dir, 'audio/start.mp3')
    audio_loop_file = path.join(bundle_dir, 'audio/loop.mp3')

    volume = 0
    start_time = 0
    mixer.init()

    window = Tk()
    window.title('Epic Cinematic Dramatic Adventure Trailer')
    window.geometry('420x58')
    window.resizable(False, False)

    frame = Frame(window, padx=8, pady=4)
    frame.pack(fill=X)

    label = Label(frame, text='Label')
    label.pack(anchor=W)

    Frame(frame, height=4).pack()


    def millis():
        return time.time() * 1000


    def slider_changed(value):
        global volume, start_time
        volume = int(value)

        if volume == 0:
            music.stop()
        elif not music.get_busy():
            start_time = millis()
            music.load(audio_start_file)
            music.queue(audio_loop_file, loops=-1)
            music.play()

        music.set_volume(volume / 100)


    slider = Scale(frame, from_=0, to=100, orient=HORIZONTAL, showvalue=False, command=slider_changed)
    slider.pack(fill=X)


    def update():
        play_time = millis() - start_time

        if music.get_busy():
            ms = int(play_time % 1000)
            s = int(play_time / 1000) % 60
            m = int(play_time / 60000) % 60
            label.config(text=f'Volume: {volume}% | Play time: {str(m).zfill(2)}.{str(s).zfill(2)}.{str(ms).zfill(3)}')
        else:
            label.config(text='Stopped')

        window.after(1, update)
        play_time += 1


    update()

    window.mainloop()
