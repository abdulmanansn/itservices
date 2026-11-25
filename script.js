
function showMessage() {
    alert("Welcome to CloudTech!");
}

document.getElementById("contactForm")
.addEventListener("submit", async function(event) {

    event.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };

    const response = await fetch("/api/contact", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").textContent =
        result.message;

    if (response.ok) {
        this.reset();
    }
});
