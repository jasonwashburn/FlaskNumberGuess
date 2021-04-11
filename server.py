import random
from flask import Flask

app = Flask(__name__)


def random_h1_color_decorator(func):
    """
    Decorator to add random color styling to the H1 tags used by other functions
    :param func: function to add H1 color styling to
    :return: returns the original function with additional <style> tag and random color styling
    """
    def wrapper(*args, **kwargs):
        return f'<style>h1 {{color: rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})}}</style>' \
               f'{func(*args, **kwargs)}'
    return wrapper


@app.route("/")
def home():
    """
    Set up the main URL
    :return:
    """
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200">'


@app.route("/<int:guess>")
@random_h1_color_decorator
def check_num(guess):
    """
    Checks the user's guess against the random number then returns a clue or success message.
    :param guess: (int) the user's guess
    :return: returns success message or a clue message
    """
    global random_number
    if guess < random_number:
        return '<h1>Too low, try again!</h1>><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > random_number:
        return '<h1>Too high, try again!</h1>><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif guess == random_number:
        return '<h1>You found me!</h1>><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


random_number = random.randint(1, 10)

if __name__ == "__main__":
    app.run(debug=True)