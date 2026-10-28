from flask import Flask, render_template , request,redirect
from lib.DatabaseConnection import DatabaseConnection
from lib.book_repository import *
from lib.user_repository import *


# instantiate a Flask app object
app = Flask(__name__)

# NEW PART START

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in

database_connection = DatabaseConnection()
database_connection.connect()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

# NEW PART END

# NEW PART START

@app.route('/books', methods=['GET'])
def books():
    book_repository = BookRepository(database_connection)
    book_list =  book_repository.all()
    print(book_list)
    return render_template("books.html", books=book_list)

@app.route('/books', methods=['POST'])
def create_book():
    book_details = request.form
    book_repository = BookRepository(database_connection)
    book = Book(id=None,title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    print(book_details)
    return redirect("/books")





@app.route('/books/<int:id>', methods=['GET'])
def bookssss(id):
    book_repository = BookRepository(database_connection)
    book_list =  book_repository.find(id)
    print(book_list)
    return {
        'id': book_list.id,
        'title':f'{book_list.title}',
        'author':f'{book_list.author}'
    }

@app.route('/authors', methods=['GET'])
def authors():
    return [
    {
        "name": "Julia Donaldson",
        "dob": "1948-09-16"
    },
    {
        "name": "Andrea Beaty",
        "dob": "1961-10-08"
    },
    {
        "name": "Kelly Barnhill",
        "dob": "1973-01-01"
    },
    {
        "name": "Zetta Elliott",
        "dob": "1979-11-11"
    }
    ]


@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/users/new', methods=['GET'])
def signup_form():
    return render_template("signup_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    user_details = request.form
    user_repository = UserRepository(database_connection)
    user = User(username=user_details["username"],password=user_details["password"])
    user_repository.create(user)
    return redirect("/books")



# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
