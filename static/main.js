const form = document.getElementById("giftForm")
const giftsContainer = document.getElementById("gifts");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const name = form.elements.name.value;
    const gift = form.elements.gift.value;

    const item = document.createElement("p");
    item.textContent = `Gift for ${name}: ${gift}`;
    giftsContainer.appendChild(item);

    form.reset();
})