# from fastapi import FastAPI
# from pydantic import BaseModel
# import requests
# import time
# from fastapi.staticfiles import StaticFiles


# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")


# class PromptRequest(BaseModel):
#     prompt: str
#     temperature: float = 0.7
#     num_predict: int = 100
#     top_k: int = 40
#     top_p: float = 0.9


# @app.post("/generate")
# def generate(data: PromptRequest):

#     start = time.time()

#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": "mistral",
#             "prompt": data.prompt,
#             "temperature": data.temperature,
#             "num_predict": data.num_predict,
#             "top_k": data.top_k,
#             "top_p": data.top_p,
#             "stream": False
            
#         }
#     )

#     end = time.time()
#     result = response.json()

#     return {
#         "response": result["response"],
#         "input_tokens": result.get("prompt_eval_count"),
#         "output_tokens": result.get("eval_count"),
#         "elapsed_time": round(end - start, 2),
#         "inference_cost": "₹0 (local)"
#     }

# from unittest import result

# from fastapi import FastAPI
# from fastapi.responses import FileResponse
# from pydantic import BaseModel
# import requests
# import time
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")


# @app.get("/")
# def home():
#     return FileResponse("index.html")


# class PromptRequest(BaseModel):
#     prompt: str
#     temperature: float = 0.7
#     num_predict: int = 100
#     top_k: int = 40
#     top_p: float = 0.9


# @app.post("/generate")
# def generate(data: PromptRequest):

#     start = time.time()

#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": "mistral",
#             "prompt": data.prompt,
#             "temperature": data.temperature,
#             "num_predict": data.num_predict,
#             "top_k": data.top_k,
#             "top_p": data.top_p,
#             "stream": False
#         }
#     )

#     end = time.time()
#     result = response.json()
#     a=3
    
# #"₹0 (local)"
#     # return {
#     #     "response": result["response"],
#     #     "input_tokens": result.get("prompt_eval_count"),
#     #     "output_tokens": result.get("eval_count"),
#     #     "elapsed_time": round(end - start, 2),
#     #     "inference_cost":a*(result.get("eval_count"))
#     # }

#     a = 3
#     output_tokens = result.get("eval_count", 0)

#     return {
#             "response": result["response"],
#              "input_tokens": result.get("prompt_eval_count", 0),
#             "output_tokens": output_tokens,
#             "elapsed_time": round(end - start, 2),
#             "inference_cost": a * output_tokens
#             }



from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests
import time
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("index.html")


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

    end = time.time()
    result = response.json()
    cost_per_token = 0.0003  # Cost per token in INR
    inf_cost = cost_per_token* result.get("eval_count")
    return {
        "response": result["response"],
        "input_tokens": result.get("prompt_eval_count"),
        "output_tokens": result.get("eval_count"),
        "elapsed_time": round(end - start, 2),
        "inference_cost": inf_cost
    }