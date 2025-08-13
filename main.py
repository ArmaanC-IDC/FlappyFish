"""
To run, cd into your project directory and then run the following command:
flask --app (name of your project) run --debug
"""

from flask import Flask, render_template, request # imports

app = Flask(__name__) # create Flask app

class Card:
    def __init__(self, id, text, isopen=False):
        self.id = id
        self.text = text
        self.isopen = isopen

board = [
    [Card("0_0", "🌟"), Card("0_1", "🍩"), Card("0_2", "🐶"), Card("0_3", "🍎"), Card("0_4", "🎲"), Card("0_5", "🎵")],
    [Card("1_0", "🚗"), Card("1_1", "🎁"), Card("1_2", "🦄"), Card("1_3", "🍕"), Card("1_4", "💎"), Card("1_5", "🍀")],
    [Card("2_0", "📚"), Card("2_1", "🍎"), Card("2_2", "🍕"), Card("2_3", "🚗"), Card("2_4", "🌟"), Card("2_5", "🌹")],
    [Card("3_0", "💎"), Card("3_1", "🎲"), Card("3_2", "🎵"), Card("3_3", "🐶"), Card("3_4", "🦄"), Card("3_5", "🍀")],
    [Card("4_0", "🎁"), Card("4_1", "🌹"), Card("4_2", "🚀"), Card("4_3", "🎵"), Card("4_4", "😀"), Card("4_5", "😀")],
    [Card("5_0", "🚀"), Card("5_1", "📚"), Card("5_2", "⚽"), Card("5_3", "🍩"), Card("5_4", "⚽"), Card("5_5", "🌈")],
]

@app.route("/")
def main():    
    if request.method=="GET":
        print("Clicked Card: " + request.args.get("clicked_card", ""))    
    return render_template("index.html", board=board)



"""
Don't delete the code below! Needed for running the app.
"""

if __name__ == "__main__":
    app.run(debug=True)
