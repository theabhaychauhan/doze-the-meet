from app.llm.handlers.llm_handler import LLMHandler

def main():
    query_handler = LLMHandler()

    query = "Explain the concept of artificial intelligence in simple terms."

    response = query_handler.get_response(query)

    print(response)

if __name__ == "__main__":
    main()
