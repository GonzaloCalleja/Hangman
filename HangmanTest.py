import random


class Letter(object):

    def __init__(self, char):
        self.discovered = False
        self.value = char

    def __str__(self):
        if self.discovered:
            return self.value +" "
        else:
            return "_ "

    def get_value(self):
        return self.value

    def get_discovered(self):
        return self.discovered

    def discover(self):
        self.discovered = True


class Hangman(object):

    def __init__(self, solution):

        self.words = open("words.txt", "r").read().split("\n")
        self.errors = 10

        self.solution = solution
        self.display = []
        self.attempts = []
        self.correct = []
        for char in solution:
            self.display.append(Letter(char))

        self.gameFinished = False

    def get_penalty(self):
        return len(self.attempts)

    def get_attempts(self):
        return self.attempts

    def get_display(self):
        result = ""
        for letter in self.display:
            result += str(letter)
        return result

    def get_game_finished(self):
        return self.gameFinished

    def check(self, char):

        if char == self.solution:
            self.gameFinished = True
            return True

        if char < "a" or char > "z" or len(char) != 1:
            raise Exception("That is not a valid input.")

        if char in self.attempts:
            print("You already tried ", char, "!. Try with another letter")

        boolean = False
        for letter in self.display:
            if char is letter.get_value():
                letter.discover()
                boolean = True

        if boolean:
            if char not in self.correct:
                self.correct.append(char)
        if not boolean:
            if char not in self.attempts:
                self.attempts.append(char)

        for letter in self.display:
            if not letter.get_discovered():
                break
        else:
            self.gameFinished = True

        return boolean



    def play(self):

        game = Hangman(random.choice(self.words))

        # while not game.get_game_finished():
        #
        #     for char in game.get_attempts():
        #         print(char, end=", ")
        #     print()
        #     print(game.get_display())
        #     char = input("Guess a letter (or the word): ")
        #     try:
        #         game.check(char)
        #     except Exception as error:
        #         print(error)
        #
        #     if game.get_penalty() > self.errors:
        #         return "You lost"
        #
        # return "YOU WIN!!"


class Game(object):

    def __init__(self):

        self.words = open("words.txt", "r").read().split("\n")
        self.errors = 10

    def play(self):

        game = Hangman(random.choice(self.words))

        while not game.get_game_finished():

            for char in game.get_attempts():
                print(char, end=", ")
            print()
            print(game.get_display())
            char = input("Guess a letter (or the word): ")
            try:
                game.check(char)
            except Exception as error:
                print(error)

            if game.get_penalty() > self.errors:
                return "You lost"

        return "YOU WIN!!"

