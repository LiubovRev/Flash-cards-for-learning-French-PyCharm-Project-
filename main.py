from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_page)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_page)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_page = PhotoImage(file="/home/liubov/PycharmProjects/31-day/flash-card-project-start/images/card_front.png")
back_page = PhotoImage(file="/home/liubov/PycharmProjects/31-day/flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(412, 274, image=front_page)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 25, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



image_wrong = PhotoImage(file="/home/liubov/PycharmProjects/31-day/flash-card-project-start/images/wrong.png")
wrong_butt = Button(image=image_wrong, highlightthickness=0, command=next_card)
wrong_butt.grid(column=0, row=1)

image_right = PhotoImage(file="/home/liubov/PycharmProjects/31-day/flash-card-project-start/images/right.png")
right_butt = Button(image=image_right, highlightthickness=0, command=is_known)
right_butt.grid(column=1, row=1)

next_card()






window.mainloop()
