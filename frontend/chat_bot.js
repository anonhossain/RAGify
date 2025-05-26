const pdfInput = document.getElementById("pdfInput");
const urlInput = document.getElementById("urlInput");
const chatWindow = document.getElementById("chatWindow");

pdfInput.addEventListener("change", () => {
    if (pdfInput.files.length > 0) {
        urlInput.disabled = true;
    } else {
        urlInput.disabled = false;
    }
});

urlInput.addEventListener("input", () => {
    if (urlInput.value.trim() !== "") {
        pdfInput.disabled = true;
    } else {
        pdfInput.disabled = false;
    }
});

async function submitDocument() {
    if (pdfInput.files.length > 0) {
        const formData = new FormData();
        formData.append("pdf_file", pdfInput.files[0]);

        const response = await fetch("/upload_document", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        alert(data.message || "PDF uploaded successfully");

    } else if (urlInput.value.trim() !== "") {
        const formData = new FormData();
        formData.append("url", urlInput.value);

        const response = await fetch("/embed_website", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        alert(data.message || "Website embedded successfully");
    } else {
        alert("Please select either a PDF or enter a website URL.");
    }
}

async function generateEmbedding() {
    const response = await fetch("/embed_pdf", {
        method: "POST"
    });

    const data = await response.json();
    alert(data.message || "System is ready to chat.");
}

async function sendMessage() {
    const input = document.getElementById("userInput");
    const text = input.value.trim();
    if (!text) return;

    appendMessage(text, "user");

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: new URLSearchParams({ prompt: text })
    });

    const data = await response.json();
    appendMessage(data.response, "bot");

    input.value = "";
}

function appendMessage(message, sender) {
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}`;
    msgDiv.textContent = message;
    chatWindow.appendChild(msgDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
