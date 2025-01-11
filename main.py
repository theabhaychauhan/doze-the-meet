import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    print("Loading the model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")   
    

    print("Model loaded successfully!")

    query = "Explain the concept of artificial intelligence in simple terms."

    print(f"\nInput query: {query}")

    inputs = tokenizer(query, return_tensors="pt")

    print("Generating a response...")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=100,
        num_return_sequences=1,
        temperature=0.7,
        do_sample=True
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"\nGenerated Response:\n{response}")


if __name__ == "__main__":
    main()
