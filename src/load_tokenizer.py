from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.2"
)

text = "SIP of ₹10,000 per month in Indian mutual funds"
tokens = tokenizer.tokenize(text)

print(tokens)
print("Token count:", len(tokens))
