const form =
    document.getElementById("scan-form");

const loader =
    document.getElementById("loader");

const button =
    document.getElementById("scan-button");

const input =
    document.getElementById("url-input");

input.addEventListener("input", () => {

    const value = input.value;

    if (
        value.startsWith("http://") ||
        value.startsWith("https://")
    ) {

        input.style.border =
            "1px solid rgba(52,199,89,0.5)";

    } else {

        input.style.border =
            "1px solid rgba(255,59,48,0.5)";
    }
});

form.addEventListener("submit", () => {

    loader.style.display = "block";

    button.innerHTML =
        "Scanning...";

    button.disabled = true;
});