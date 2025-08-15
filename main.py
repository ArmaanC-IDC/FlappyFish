"""
To run, cd into your project directory and then run the following command:
flask --app (name of your project) run --debug
"""

from flask import Flask, render_template, request # imports
import time
import random

app = Flask(__name__) # create Flask app

class Card:
    def __init__(self, id, text, isopen=False):
        self.id = id
        self.text = text
        self.isopen = isopen

emojis = [
    "🌊",  # Water Wave
    "🐠",  # Tropical Fish
    "🐟",  # Fish
    "🐬",  # Dolphin
    "🐳",  # Spouting Whale
    "🐋",  # Whale
    "🦈",  # Shark
    "🐙",  # Octopus
    "🦀",  # Crab
    "🦞",  # Lobster
    "🦐",  # Shrimp
    "🦑",  # Squid
    "🐚",  # Shell
    "🪸",  # Coral
    "🪼",  # Jellyfish
    "⚓",  # Anchor
    "⛵",  # Sailboat
    "🚤"   # Speedboat
]

def create_board():
    emojis_shuffled = emojis*2
    random.shuffle(emojis_shuffled)
    emojis_2d = [emojis_shuffled[i * 6:(i + 1) * 6] for i in range(6)]

    for i in range(len(emojis_2d)):
        for j in range(len(emojis_2d[i])):
            emojis_2d[i][j] = Card(str(i)+"_"+str(j), emojis_2d[i][j])
    
    return emojis_2d

board = create_board()
numTurns = 0

#Keep track of currently flipped cards
open_cards = []

@app.route("/")
def main():
    global numTurns, board
    clicked_card_id = request.args.get("clicked_card", "")
    reset = request.args.get("reset", "")
    if (reset=="True"):
        #reset the board
        for row in board:
            for card in row:
                card.isopen = False
        board = create_board()

    if clicked_card_id:
        found = False
        for row in board:
            for card in row:
                if card.id == clicked_card_id:
#only flip if not open
                    if not card.isopen:
                        card.isopen = True
                        open_cards.append(card)
                    found = True
                    break
            if found:
#stop outsiide loop
                break

#
        if len(open_cards) == 2:
            numTurns += 1
            card1, card2 = open_cards
            if card1.text != card2.text:
                time.sleep(0.5)
#not match is flip them back
                card1.isopen = False
                card2.isopen = False
#reset  open cards list
            open_cards.clear()

            #check if player won
            won = True
            for row in board:
                for card in row:
                    if not card.isopen:
                        won = False
            
            if won:
                return render_template("winpage.html")

    try:
        if board is None:
            board = create_board()
    except:
        board = create_board()

    return render_template("index.html", board=board, numTurns=numTurns)



"""
Don't delete the code below! Needed for running the app.
"""

if __name__ == "__main__":
    app.run(debug=True)
