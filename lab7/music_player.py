import os
import pygame
from tkinter import *
from tkinter import messagebox
from pynput import keyboard  # для управления с клавиатуры

class MP:
    def __init__(self, win):
        pygame.mixer.init()

        self.music_files = []
        self.current_track_index = 0

        win.title("Music Player")
        win.geometry("500x100")
        win.resizable(0, 0)

        # Кнопки
        Button(win, text='Load', width=10, font=('Arial', 12), command=self.load).place(x=30, y=30)
        Button(win, text='Play', width=10, font=('Arial', 12), command=self.play).place(x=130, y=30)
        Button(win, text='Pause', width=10, font=('Arial', 12), command=self.pause).place(x=230, y=30)
        Button(win, text='Previous', width=10, font=('Arial', 12), command=self.previous_track).place(x=330, y=30)
        Button(win, text='Next', width=10, font=('Arial', 12), command=self.next_track).place(x=430, y=30)

        # Горячие клавиши
        listener = keyboard.Listener(on_press=self.on_key_press)
        listener.start()

    def load(self):
        folder = os.path.dirname(__file__)  # текущая папка (где лежит .py)
        self.music_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".mp3")]
        if not self.music_files:
            messagebox.showerror("Ошибка", "Файлы .mp3 не найдены в папке!")
        else:
            self.current_track_index = 0
            print("Загружено:", self.music_files)

    def play(self):
        if self.music_files:
            pygame.mixer.music.load(self.music_files[self.current_track_index])
            pygame.mixer.music.play()
            print(f"Играет: {os.path.basename(self.music_files[self.current_track_index])}")

    def pause(self):
        pygame.mixer.music.pause()
        print("Пауза")

    def unpause(self):
        pygame.mixer.music.unpause()
        print("Продолжить")

    def previous_track(self):
        if self.music_files:
            self.current_track_index = (self.current_track_index - 1) % len(self.music_files)
            self.play()

    def next_track(self):
        if self.music_files:
            self.current_track_index = (self.current_track_index + 1) % len(self.music_files)
            self.play()

    def on_key_press(self, key):
        try:
            if key.char == 'p':  # Play
                self.play()
            elif key.char == 's':  # Pause
                self.pause()
            elif key.char == 'r':  # Resume (unpause)
                self.unpause()
            elif key.char == 'n':  # Next
                self.next_track()
            elif key.char == 'b':  # Previous
                self.previous_track()
        except AttributeError:
            pass  # спец.клавиши типа Shift игнорируем

# Запуск
if __name__ == "__main__":
    root = Tk()
    MP(root)
    root.mainloop()

