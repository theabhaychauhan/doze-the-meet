import os
from app.llm.handlers.llm_handler import LLMHandler
from app.llm.connectors.weaviate_connection import get_weaviate_client

def main():
    query_handler = LLMHandler()
    weaviate_client = get_weaviate_client()

    lecture_transcript = """
    Artificial Intelligence, or AI, refers to the simulation of human intelligence by machines. 
    It includes techniques like machine learning, where algorithms improve over time by learning 
    from data, and natural language processing, which enables machines to understand and generate 
    human language. Applications of AI range from self-driving cars to virtual assistants like Siri 
    and Alexa. AI aims to make machines capable of tasks that typically require human cognition, such 
    as reasoning, problem-solving, and decision-making.
    """

    query = "Summarize the lecture transcript and provide key insights."
    response = query_handler.get_response(f"{lecture_transcript}\n\n{query}")

    print("LLM Response:", response)

    try:
        weaviate_client.data_object.create(
            data_object={
                "lecture": lecture_transcript,
                "summary": response,
                "topic": "Artificial Intelligence",
            },
            class_name="LectureNotes",
        )
        print("Response successfully saved to Weaviate.")
    except Exception as e:
        print(f"Error saving to Weaviate: {e}")

if __name__ == "__main__":
    main()
