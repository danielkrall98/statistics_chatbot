# The Main CLI-Tool

from llm import call_llm
from prompts import get_query_prompt, get_answer_prompt
from query_engine import run_query, df

def main():
    print("Statistik Chatbot (type 'exit' to quit)\n")

    while True:
        question = input("Frage: ")

        if question.lower() == "exit":
            break

        # Step 1: Generate Query
        query_prompt = get_query_prompt(question, df)
        query_code = call_llm(query_prompt)

        print("\nGenerated Query:\n", query_code)

        # Step 2: Execute Query
        result = run_query(query_code)

        print("\nRaw Result:\n", result)

        # Step 3: Generate Answer
        answer_prompt = get_answer_prompt(question, str(result))
        answer = call_llm(answer_prompt)

        print("\nAntwort:\n", answer)
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()