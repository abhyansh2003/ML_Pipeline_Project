from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("We are testing our 2nd method of logging")
    return "This is my 2nd ML Pipeline Project"

if __name__ == "__main__":
    app.run(debug=True)