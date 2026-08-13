import tkinter as tk
import random
import time

sentences = [
    "I am a good boy currently learning python programming language",
    "Hello everyone welcome to the typing speed test application",
    "Today I stepped on a dog and it was a very painful experience for me"
]

start_time = 0


def start_test():
    global start_time

    sentence = random.choice(sentences)
    sentence_label.config(text=sentence)

    input_box.delete("1.0", tk.END)

    result_label.config(text="")

    start_time = time.time()


def check_result():
    end_time = time.time()

    original = sentence_label.cget("text")
    user_text = input_box.get("1.0", tk.END).strip()

    time_taken = end_time - start_time

    correct_chars = sum(
        1 for a, b in zip(user_text, original) if a == b
    )

    accuracy = (correct_chars / len(original)) * 100

    words = len(user_text.split())

    wpm = (words / time_taken) * 60

    result = (
        f"Time: {time_taken:.2f} sec\n"
        f"Words Typed: {words}\n"
        f"Accuracy: {accuracy:.2f}%\n"
        f"Speed: {wpm:.2f} WPM"
    )

    result_label.config(text=result)


root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("700x500")

title = tk.Label(
    root,
    text="Typing Speed Test",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

sentence_label = tk.Label(
    root,
    text="Click Start Test",
    wraplength=600,
    font=("Arial", 14)
)
sentence_label.pack(pady=20)

input_box = tk.Text(
    root,
    height=5,
    width=60,
    font=("Arial", 12)
)
input_box.pack()

start_button = tk.Button(
    root,
    text="Start Test",
    command=start_test
)
start_button.pack(pady=10)

submit_button = tk.Button(
    root,
    text="Submit",
    command=check_result
)
submit_button.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=20)

root.mainloop()