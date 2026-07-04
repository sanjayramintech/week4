const prompt = document.getElementById("prompt");
const temperature = document.getElementById("temperature");
const top_k = document.getElementById("top_k");
const top_p = document.getElementById("top_p");
const num_predict = document.getElementById("num_predict");

const responseBox = document.getElementById("responseBox");
const input = document.getElementById("input");
const output = document.getElementById("output");
const time = document.getElementById("time");
const cost = document.getElementById("cost");

const btn = document.getElementById("generateBtn");
const loader = document.getElementById("loader");

async function generate() {
    loader.style.display = "inline-block";
    btn.disabled = true;
    try {
        const payload = {
            prompt: prompt.value || "",
            temperature: parseFloat(temperature.value),
            top_k: parseInt(top_k.value),
            top_p: parseFloat(top_p.value),
            num_predict: parseInt(num_predict.value)
        };

        console.log("Sending:", payload);

        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        console.log("Response:", data);

        if (!response.ok) {
            responseBox.textContent = data.detail || "Error occurred";
            return;
        }

        responseBox.textContent = data.response || "No response";

        input.textContent = data.input_tokens ?? 0;
        output.textContent = data.output_tokens ?? 0;
        time.textContent = (data.elapsed_time ?? 0) + " sec";
        cost.textContent = data.inference_cost || "N/A";

    } catch (error) {
        console.error("Error:", error);
        responseBox.textContent = "Something went wrong!";
    }
    loader.style.display = "none";
    btn.disabled = false;
}

window.addEventListener("DOMContentLoaded", () => {

    const top_p = document.getElementById("top_p");
    const toppValue = document.getElementById("toppValue");

    const temperature = document.getElementById("temperature");
    const tempValue = document.getElementById("tempValue");

    const top_k = document.getElementById("top_k");
    const topkValue = document.getElementById("topkValue");

    // Top P
    top_p.addEventListener("input", () => {
        toppValue.textContent = top_p.value;
    });

    // Temperature
    temperature.addEventListener("input", () => {
        tempValue.textContent = temperature.value;
    });

    // Top K
    top_k.addEventListener("input", () => {
        topkValue.textContent = top_k.value;
    });

});