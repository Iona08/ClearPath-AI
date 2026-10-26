
import ollama
from datetime import datetime

MODEL = "llama3.1:8b"


def ask_ai(mode, details):
    prompt = f"""
You are ClearPath AI, a practical planning assistant for students.

Your goal is to turn confusing tasks into realistic, manageable actions.

Mode: {mode}
User's information: {details}
Current date and time: {datetime.now().strftime("%d %b %Y, %I:%M %p")}


Instructions:
- Use simple, clear English.
- Give specific, numbered action steps.
- Prioritize urgent and important tasks.
- Respect the time and resources the user has.
- Include realistic time estimates where possible.
- For time-limited plans, calculate the total proposed time.
- Never allocate more time than the user says they have.
- If all tasks cannot fit, say so honestly and suggest what
  to prioritize, shorten, or postpone.
- Do not invent deadlines or claim tasks are completed.
- End with one small action the user can start immediately.
"""
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


def main():
    print("\n" + "=" * 45)
    print("        CLEARPATH AI")
    print(" Turn overwhelming tasks into clear actions")
    print("=" * 45)

    while True:
        print("\nChoose what you need:")
        print("1. Priority Planner")
        print("2. Problem Breaker")
        print("3. Time Rescue")
        print("4. Exit")

        choice= input("Choose an option: ").strip()
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please enter a number from 1 to 4.")
            continue
        if choice == "4":
            print("Good luck! One step at a time.")
            break

        modes = {
            "1": "Priority Planner",
            "2": "Problem Breaker",
            "3": "Time Rescue"
        }

        if choice not in modes:
            print("Please enter a valid option from 1 to 4.")
            continue

        if choice == "1":
            details = input(
                "List your tasks and deadlines: "
            ).strip()
        elif choice == "2":
            details = input(
                "Describe the problem you want to solve: "
            ).strip()
        else:
            details = input(
                "What must you finish, and how much time do you have? "
            ).strip()

        if not details:
            print("Please enter some details first.")
            continue

        print("\nClearPath AI is preparing your plan...\n")

        try:
            result = ask_ai(modes[choice], details)
            print("-" * 45)
            print(result)
            print("-" * 45)
        except Exception as error:
            print("\nCould not get an AI response.")
            print("Check that Ollama is running and the model is available.")
            print("Technical details:", error)


if __name__ == "__main__":
    main()
