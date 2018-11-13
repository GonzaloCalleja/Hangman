
from HangmanTest import Hangman
from tkinter import *
import random
from tkinter import messagebox



from PIL import ImageTk, Image

alphabet = "abcdefghijklmnopqrstuvwxyz"


class setupGUI(object):

    def __init__(self):
        self.words = open("words.txt", "r").read().split("\n")
        self.errors = 10
        self.game = Hangman(random.choice(self.words))
        self.game.play()


        window = Tk(screenName="Hangman")
        bgcolor = "grey"
        window.title("Poker")
        window.geometry("900x400")

        self.frame = Frame(master=window, bg=bgcolor)
        self.frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self.frame.pack(fill=BOTH, expand=1)  # Expand the frame to fill the root window

        self.label = Label(self.frame, text="Hangman Game", bg=bgcolor, fg="white")
        self.label.grid(row=0, column=2)
        self.label.config(font=("Courier", 15))

        self.alphabet_frame = Frame(master=self.frame, bg="white")
        self.alphabet_frame.grid(row=11, column=1, columnspan=6, rowspan=9)

        self.letters = []

        for i in range(len(alphabet)):
            self.letters.append(Button(master=self.alphabet_frame, text=alphabet[i], relief="flat",
                                       font=('Helvetica', 10),
                                       command=lambda i=i: self.select(i)))
            self.letters[i].grid(row=11, column=i+1)


        #self.hangman_frame = Frame(master=self.frame, bg="white")
        #self.alphabet_frame.grid(row=2, column=1, columnspan=3)



        self.hangman_image = Canvas(master=self.frame, bg="gray", highlightthickness=0)
        self.hangman_image.grid(row=1, column=14, columnspan=6, rowspan=9)

        self.get_image(0)

        self.word_label = Label(master=self.frame, text=self.game.get_display(), bg="darkgray", font=("Helvetica", 36))
        self.word_label.grid(row=2,column=1,rowspan=2,columnspan=12)

        self.wrong = Label(master=self.frame, text="Wrong", fg="red", bg="lightgray", font=("Helvetica", 36))
        self.wrong.grid(row=6, column=0, rowspan=2, columnspan=3)

        self.right = Label(master=self.frame, text="Correct", fg="green",bg="lightgray", font=("Helvetica", 36))
        self.right.grid(row=6, column=3, rowspan=2, columnspan=3)


        window.mainloop()




    def exit_game(self):
        exit(0)

    def select(self, id):

        if self.game.check(alphabet[id]):
            #self.word_label.labelText = self.game.get_display()
            self.word_label.config(text =self.game.get_display())

        wrong = ""
        for char in self.game.get_attempts():
            wrong += char + " "

        self.wrong.config(text=wrong)

        correct = ""
        for char in self.game.correct:
            correct += char + " "
        self.right.config(text=correct)

        if self.game.get_penalty() > 10:
            self.lose()

        if "_" not in self.game.get_display():
            self.win()

        self.get_image(self.game.get_penalty())


    def win(self):
        #messagebox.showinfo("win", "win")
        if messagebox.askyesno("WIN", "You won!! Do you want to play again?"):
            self.game = Hangman(random.choice(self.words))
            self.game.play()
            self.word_label.config(text=self.game.get_display())
            self.wrong.config(text="Wrong")
            self.right.config(text="Correct")
            self.get_image(0)

    def lose(self):
        #messagebox.showinfo("lost", "lost")
        if messagebox.askyesno("Lost", "You lost!! Do you want to play again?"):

            self.game = Hangman(random.choice(self.words))
            self.game.play()
            self.word_label.config(text=self.game.get_display())
            self.wrong.config(text="Wrong")
            self.right.config(text="Correct")
            self.get_image(0)


        #self.letters[id] = Label(master=self.alphabet_frame, text=alphabet[id])



    def get_image(self, number):
        #width = self.hangman_image.winfo_width() %2
        #height = self.hangman_image.winfo_height() %2
        size = 350, 350
        name = str(number) + ".png"
        im = Image.open("HangmanImages/" + name)
        # resize the image to fit our table
        im.thumbnail(size)
        # Put the image into a canvas compatible class, and stick in an
        # arbitrary variable to the garbage collector doesn't destroy it
        self.hangman_image.image = ImageTk.PhotoImage(im)
        # Add the image to the canvas, and set the anchor to the top left / north west corner
        self.hangman_image.create_image(15, -40, image=self.hangman_image.image, anchor='nw')


c = setupGUI()
