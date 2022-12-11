from flask import Flask, jsonify, request

app = Flask(__name__)


books_db = [

    {
    "name":"English",
    "price":"550"
    },
    {
    "name":"Maths",
    "price":"580"
    }

]

#Retrieve all books
@app.route('/books')
def get_all_books():
    return jsonify({"books":books_db})

#Retrieve single book
@app.route('/book/<string:name>')
def get_book(name):
    for book in books_db:
        if book['name']==name:   
            return jsonify(book)
    return jsonify({'message':"book not found"})


#create a book
@app.route('/book', methods= ['POST'])
def create_book():
    request_data = request.get_json()
    books_db.append(request_data)

    return jsonify({"message": "book created"})


@app.route("/")
def hello():
    return "Hello world"


app.run(port=5000)