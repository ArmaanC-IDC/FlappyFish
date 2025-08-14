"""
To run, cd into your project directory and then run the following command:
flask --app (name of your project) run --debug
"""

from flask import Flask, render_template, request # imports
import time

app = Flask(__name__) # create Flask app

class Card:
    def __init__(self, id, text, isopen=False):
        self.id = id
        self.text = text
        self.isopen = isopen

board = [
    [Card("0_0", "🌟"), Card("0_1", "🍩")],
    [Card("1_0", "🍩"), Card("1_1", "🌟")],
    [Card("0_0", "🌟"), Card("0_1", "🍩")],
    [Card("1_0", "🍩"), Card("1_1", "🌟")],
    [Card("0_0", "🌟"), Card("0_1", "🍩")],
    [Card("1_0", "🍩"), Card("1_1", "🌟")],
]

numTurns = 0

#Keep track of currently flipped cards
open_cards = []

@app.route("/")
def main():
    global numTurns
    clicked_card_id = request.args.get("clicked_card", "")
    reset = request.args.get("reset", "")
    if (reset=="True"):
        #reset the board
        for row in board:
            for card in row:
                card.isopen = False
        numTurns = 0

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
                return "<h1>YOU WON!</h1>"

    return render_template("index.html", board=board, numTurns=numTurns)



"""
Don't delete the code below! Needed for running the app.
"""

if __name__ == "__main__":
    app.run(debug=True)
