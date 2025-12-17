import flask
import sqlite3

app = flask.Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
conn = sqlite3.connect('books.db') 
cursor = conn.cursor()  
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gifts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        book TEXT NOT NULL
    )
''')
conn.commit()  
conn.close()

@app.get("/")
def index():
    return flask.send_from_directory("static", "index.html")

@app.post("/books")
def create_book():
    data = flask.request.get_json()
    name = data.get('name')
    book = data.get('book')
    
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (name, book) VALUES (?, ?)', (name, book))
    conn.commit()
    conn.close()

    return '', 201
    
@app.get("/books")
def get_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, book FROM books')
    rows = cursor.fetchall()
    conn.close()
    
    books = [{'id': row[0], 'name': row[1], 'book': row[2]} for row in rows]
    return flask.jsonify(books)

if __name__ == "__main__":
    app.run()
