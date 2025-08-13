"""
To run, cd into your project directory and then run the following command:
flask --app (name of your project) run --debug
"""

from flask import Flask, render_template # imports

app = Flask(__name__) # create Flask app





"""
Don't delete the code below! Needed for running the app.
"""

if __name__ == "__main__":
    app.run(debug=True)
