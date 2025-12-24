const form = document.getElementById("bookForm")
const booksContainer = document.getElementById("books");

async function loadBooks() {
    const response = await fetch('/books');
    const books = await response.json();
    
    booksContainer.innerHTML = '';
    books.forEach(book => {
        const item = document.createElement("p");
        item.textContent = `Book suggested by ${name}: ${book.book}`;
        booksContainer.appendChild(item);
    });
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = form.elements.name.value;
    const book = form.elements.book.value;

    await fetch('/books', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, book })
    });

    form.reset();
    await loadBooks(); 
});

loadBooks();
