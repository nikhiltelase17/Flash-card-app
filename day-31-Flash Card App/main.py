from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Reading data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):   # file is not or file is empty
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def is_known():
    if len(to_learn) > 0:
        global data
        to_learn.remove(current_card)
        # Crate words to learn csv
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        next_card()


def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")


def next_card():
    if len(to_learn) > 0:
        global current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(to_learn)
        french_word = current_card["French"]
        canvas.itemconfig(image, image=card_front_img)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=french_word, fill="black")
        flip_timer = window.after(3000, flip_card)
    else:
        print("Jay shree ram")


# # Ui Setup
window = Tk()
window.title("Flapy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
