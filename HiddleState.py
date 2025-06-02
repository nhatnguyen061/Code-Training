from transformers import AutoModel, AutoTokenizer
import torch
checkpoint = "distilbert-base-uncased"
model = AutoModel.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

sentence = "Hello, my dog is cute"
inputs = tokenizer(sentence, return_tensors="pt")
outputs = model(**inputs)
print(outputs.last_hidden_state.shape)
# print(inputs['input_ids'])
