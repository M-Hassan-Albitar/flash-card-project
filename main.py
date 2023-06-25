import random
from tkinter import *
import pandas as pd
import random

# Constance
BACKGROUND_COLOR = "#B1DDC6"

# LOGIC
current_card = {}
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    data_list = data.to_dict(orient="records")
else:
    data_list = data.to_dict(orient="records")


def next_card():
    global current_card, flip
    window.after_cancel(flip)
    current_card = random.choice(data_list)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=front_img)
    flip = window.after(3000, change_card)


def change_card():
    global current_card
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=back_img)


def to_learn():
    global current_card
    data_list.remove(current_card)
    learn = pd.DataFrame(data_list)
    learn.to_csv("./data/words_to_learn.csv", encoding=None)
    next_card()


# UI
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip = window.after(3000, change_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")

card_img = canvas.create_image((400, 263), image=front_img)
title = canvas.create_text((400, 132), font=("Ariel", 40, "italic"))
word = canvas.create_text((400, 270), font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

right_btn = Button(image=right_img, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
right_btn.grid(row=1, column=1)
wrong_btn = Button(image=wrong_img, highlightthickness=0, background=BACKGROUND_COLOR, command=to_learn)
wrong_btn.grid(row=1, column=0)

# Call Function to create default title and word in canvas texts
next_card()

window.mainloop()
