const form = document.getElementById("bookForm")
const booksContainer = document.getElementById("book");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = form.elements.name.value;
    const book = form.elements.book.value;

    const item = document.createElement("p");
    item.textContent = `Book suggested by ${name}: ${book}`;
    booksContainer.appendChild(item);

    form.reset();
})