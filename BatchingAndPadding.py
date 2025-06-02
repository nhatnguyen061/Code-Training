from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

texts = [
    "Hello, my dog is cute",
    "I love programming in Python",]
inputs = tokenizer(
    texts,
    padding=True,
    truncation=True,
    return_tensors="pt"
)
print(inputs['input_ids'])