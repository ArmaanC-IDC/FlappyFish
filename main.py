"""
To run, cd into your project directory and then run the following command:
flask --app (name of your project) run --debug
"""

from flask import Flask, render_template, request  # imports
import time
import random

app = Flask(__name__)  # create Flask app

# Card class
class Card:
    def __init__(self, id, text, isopen=False):
        self.id = id
        self.text = text
        self.isopen = isopen

# --- Game settings ---
rows = 6
cols = 5
symbols = ["🌊", "🐋", "🐚", "🪸", "✨", "🪩", "🌅", "🪼", "⚓️", "🦦",
           "🐠", "🦈", "🐬", "🫧", "🦪"]

# --- Function to generate a randomized board ---
def generate_board():
    total_cards = rows * cols
    needed_pairs = total_cards // 2
    deck = symbols[:needed_pairs] * 2
    random.shuffle(deck)

    board = []
    for r in range(rows):
        row = []
        for c in range(cols):
            card_id = f"{r}_{c}"
            row.append(Card(card_id, deck.pop()))
        board.append(row)
    return board

# create shuffled board once at startup
board = generate_board()


numTurns = 0
open_cards: list[Card] = []  # track currently flipped cards

# --- Flask route ---
@app.route("/")
def main():
    global numTurns, board, open_cards
    clicked_card_id = request.args.get("clicked_card", "")
    reset = request.args.get("reset", "")

    if reset == "True":
        # reset and reshuffle the board
        board = generate_board()
        numTurns = 0
        open_cards = []

    if clicked_card_id:
        found = False
        for row in board:
            for card in row:
                if card.id == clicked_card_id:
                    if not card.isopen:
                        card.isopen = True
                        open_cards.append(card)
                    found = True
                    break
            if found:
                break

        if len(open_cards) == 2:
            numTurns += 1
            card1, card2 = open_cards
            if card1.text != card2.text:
                time.sleep(0.5)
                card1.isopen = False
                card2.isopen = False
            open_cards.clear()

            # check if player won
            won = True
            for row in board:
                for card in row:
                    if not card.isopen:
                        won = False
            if won:
                return render_template("winpage.html")

    return render_template("index.html", board=board, numTurns=numTurns)

# --- Run app ---
if __name__ == "__main__":
    app.run(debug=True)
