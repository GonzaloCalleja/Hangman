
from HangmanTest import Game

game = Game()

while True:
    print(game.play())
    play_again = input("GAME FINISHED\nWould you like to try again? (T / F): ")

    if play_again is "F":
        break
    elif play_again is "T":
        continue
    else:
        print("That was not a valid answer")

# solution = "blablabla"
# display = []
# for char in solution:
#     display.append(Letter(char))
#
# count = 0
# while display != solution:
#
#     for letter in display:
#         print(letter, end="")
#
#     char = input("Guess a letter or the word: ")
#     if char is solution:
#         break
#     if char < "a" or char > "z" or len(char) != 1:
#         print("That is not a valid input")
#         continue
#
#     for letter in display:
#         if char is letter.get_value():
#             letter.discover()
#             count += 1
#
#     if count == len(solution):
#         break
#
# print(solution, "was the word!!")
# print("YOU WIN")