from fastapi import FastAPI
from pydantic import BaseModel
import requests
import time

app = FastAPI()

#class poopo

# class PromptRequest(BaseModel):
#     prompt: str
#     temperature: float = 0.7

class PromptRequest(BaseModel):
    prompt: str
    temperature: float = 0.7
    num_predict: int = 100
    top_k: int = 40
    top_p: float = 0.9


@app.post("/generate")
def generate(data: PromptRequest):

    start = time.time()

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": data.prompt,
            "temperature": data.temperature,
            "num_predict": data.num_predict,
            "top_k": data.top_k,
            "top_p": data.top_p,
            "stream": False
            
        }
    )

    
    result = response.json()

    return {
        "response": result["response"],
        "input_tokens": result.get("prompt_eval_count"),
        "output_tokens": result.get("eval_count"),
        "elapsed_time": round(end - start, 2),
        "inference_cost": "₹0 (local)"
    }