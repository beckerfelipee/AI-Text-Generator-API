import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from flask import Flask, request
from huggingface_hub import login

app = Flask(__name__)

login(token="")

model_name = 'mistralai/Mistral-7B-v0.3'
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
).to('cuda')
tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.get('/')
def index():
    return {'status': 'NLP ready!'}

@app.post('/')
def inference():
    max_tokens = request.json['max_tokens']
    temperature = request.json['temperature']
    top_p = request.json['top_p']

    prompt = request.json['prompt']

    input_ids = tokenizer(prompt, return_tensors='pt').input_ids.to('cuda')
    prompt_len = input_ids.shape[1]

    output = model.generate(
        input_ids,
        max_new_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        do_sample=True
    )

    output_text = tokenizer.decode(output[0][prompt_len:], skip_special_tokens=True)
    return {'output': output_text}
