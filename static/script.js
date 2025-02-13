document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("generateBtn").addEventListener("click", generatePasswords);
});

async function generatePasswords() {
    const numPasswords = document.getElementById("numPasswords").value;
    const length = document.getElementById("passwordLength").value;

    if (numPasswords < 1 || length < 3) {
        alert("Please enter valid values. Minimum length: 3");
        return;
    }

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ num_passwords: parseInt(numPasswords), length: parseInt(length) })
        });

        const data = await response.json();
        const passwordList = document.getElementById("passwordList");
        passwordList.innerHTML = "";

        if (data.passwords) {
            data.passwords.forEach(password => {
                const li = document.createElement("li");
                li.textContent = password;
                passwordList.appendChild(li);
            });
        } else {
            alert("Error generating passwords");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to connect to the server.");
    }
}
