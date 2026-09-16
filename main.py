"""CodeAlpha Basic Chatbot (Interactive Edition).

A console-based, rule-based chatbot built with Python.
Enhanced with interactive personalization, typing simulation, and utility tools.
Developed for the CodeAlpha Python Programming Internship.
"""

import datetime
import random
import sys
import time

# Reconfigure stdout to utf-8 if supported to prevent Windows cp1252 charmap errors
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Terminal color formatting (ANSI escape codes)
COLOR_BOT = "\033[96m"       # Cyan
COLOR_USER = "\033[92m"      # Green
COLOR_ACCENT = "\033[93m"    # Yellow
COLOR_RESET = "\033[0m"      # Reset
COLOR_BOLD = "\033[1m"       # Bold

# Predefined curated jokes and facts for interactive rules
PROGRAMMING_JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "Why did the Python programmer wear glasses? Because they couldn't C#!",
    "Why was the JavaScript developer sad? Because they didn't know how to 'null' their feelings.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'"
]

TECH_FACTS = [
    "Python was named after the comedy series 'Monty Python's Flying Circus', not the snake!",
    "The first computer bug was an actual real moth found inside the Harvard Mark II computer in 1947.",
    "The first computer mouse was invented in 1964 by Doug Engelbart and was made of wood.",
    "The QWERTY keyboard layout was designed in 1873 to prevent mechanical typewriter jams.",
    "More than 5 billion lines of code are committed to open-source repositories every year!"
]


def bot_say(message, prefix="Bot: ", delay=0.01):
    """Prints a message with a subtle typewriter effect for high interactivity.

    If output is redirected or piped, delay is set to 0 for instant output.
    """
    actual_delay = delay if sys.stdout.isatty() else 0.0

    print(f"{COLOR_BOT}{COLOR_BOLD}{prefix}{COLOR_RESET}", end="", flush=True)
    for char in message:
        print(char, end="", flush=True)
        if actual_delay > 0:
            time.sleep(actual_delay)
    print()


def display_welcome_message():
    """Displays an engaging welcome banner and usage tips."""
    print(f"{COLOR_ACCENT}{'=' * 62}{COLOR_RESET}")
    print(f"{COLOR_BOLD}{COLOR_ACCENT}        *** WELCOME TO CODEALPHA BASIC CHATBOT ***        {COLOR_RESET}")
    print(f"{COLOR_ACCENT}{'=' * 62}{COLOR_RESET}")
    print("Hello! I am an interactive, rule-based console assistant.")
    print("I can converse, tell jokes, share tech facts, check time, and more!")
    print(f"- Type {COLOR_ACCENT}'help'{COLOR_RESET} anytime to explore everything I can do.")
    print(f"- Type {COLOR_ACCENT}'bye'{COLOR_RESET}, {COLOR_ACCENT}'exit'{COLOR_RESET}, or {COLOR_ACCENT}'quit'{COLOR_RESET} to end our chat.")
    print(f"{COLOR_ACCENT}{'-' * 62}{COLOR_RESET}")


def display_help(user_name="Friend"):
    """Returns an interactive guide of supported commands categorized by intent."""
    return (
        f"Here is what you can ask me, {user_name}:\n"
        "  * Greetings      : 'hello', 'hi', 'hey'\n"
        "  * State/Status   : 'how are you', 'how are you doing'\n"
        "  * Identity       : 'what is your name', 'who are you', 'what is my name'\n"
        "  * Live Utilities : 'time', 'date', 'what time is it', 'what is today\\'s date'\n"
        "  * Fun & Games    : 'tell me a joke', 'tell me a fact', 'flip a coin', 'roll a die'\n"
        "  * Courtesy       : 'thank you', 'thanks'\n"
        "  * Exit Chat      : 'bye', 'goodbye', 'exit', 'quit'"
    )


def is_exit_command(user_message):
    """Checks if the user's message matches any termination command."""
    exit_commands = ["bye", "goodbye", "exit", "quit"]
    return user_message in exit_commands


def get_bot_response(user_message, user_name="Friend"):
    """Determines the bot response using rule-based if-elif-else logic.

    Args:
        user_message (str): Preprocessed user input (lowercase, stripped).
        user_name (str): The personalized name of the user.

    Returns:
        str: Predefined response.
    """
    # Rule 1: Empty input check
    if not user_message:
        return "You didn't say anything! Please type a message."

    # Rule 2: Greetings
    elif user_message in ["hello", "hi", "hey", "hello there", "hey there", "greetings"]:
        if user_name != "Friend":
            return f"Hi {user_name}! How can I help you today?"
        return "Hi! How can I help you today?"

    # Rule 3: Inquiry about bot's state / well-being
    elif user_message in ["how are you", "how are you doing", "how are things", "how's it going"]:
        return "I'm fine, thanks! How are you doing today?"

    # Rule 4: User answering how they are
    elif user_message in ["i am fine", "i am good", "i'm good", "i'm fine", "doing well", "great", "good"]:
        return f"Glad to hear that, {user_name}! How can I assist you?"

    # Rule 5: Identity queries about the bot
    elif user_message in ["what is your name", "who are you", "what's your name", "whats your name"]:
        return "I'm a simple Python rule-based chatbot created for the CodeAlpha internship."

    # Rule 6: Identity queries about the user (personalized interactivity)
    elif user_message in ["what is my name", "who am i", "do you know my name"]:
        return f"Your name is {user_name}! It's a pleasure chatting with you."

    # Rule 7: Real-time time & date utilities
    elif user_message in ["time", "what time is it", "current time", "what is the time"]:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"[Time] The current time is {current_time}."

    elif user_message in ["date", "what is today's date", "today's date", "what is the date"]:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"[Date] Today is {current_date}."

    # Rule 8: Interactive fun features (Jokes, Facts, Coin Flip, Dice)
    elif user_message in ["joke", "tell me a joke", "make me laugh"]:
        return f"[Joke] {random.choice(PROGRAMMING_JOKES)}"

    elif user_message in ["fact", "tell me a fact", "tech fact", "fun fact"]:
        return f"[Fact] {random.choice(TECH_FACTS)}"

    elif user_message in ["flip a coin", "coin flip", "flip coin", "toss a coin"]:
        coin_result = random.choice(["Heads", "Tails"])
        return f"[Coin Flip] Result: It's {coin_result}!"

    elif user_message in ["roll a die", "roll dice", "roll a dice", "dice"]:
        dice_result = random.randint(1, 6)
        return f"[Dice Roll] Result: You rolled a {dice_result}!"

    # Rule 9: Help menu
    elif user_message in ["help", "what can you do", "commands", "options"]:
        return display_help(user_name)

    # Rule 10: Courtesy & Gratitude
    elif user_message in ["thank you", "thanks", "thanks a lot", "thank you very much"]:
        return f"You're very welcome, {user_name}! Feel free to ask if you need anything else."

    # Rule 11: Exit commands
    elif is_exit_command(user_message):
        return f"Goodbye! Have a wonderful day!"

    # Rule 12: Default fallback for unrecognized input
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can do."


def run_chatbot():
    """Main interactive conversation loop."""
    display_welcome_message()

    # Interactive Step: Ask the user for their name for personalized interaction
    try:
        user_name_input = input(f"{COLOR_BOT}{COLOR_BOLD}Bot: {COLOR_RESET}Before we begin, may I know your name? (Press Enter to skip): ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)

    user_name = user_name_input.title() if user_name_input else "Friend"
    bot_say(f"Nice to meet you, {user_name}! How can I help you today?")
    print()

    # Main Conversation Loop
    while True:
        try:
            # Display personalized user prompt
            raw_input = input(f"{COLOR_USER}{COLOR_BOLD}{user_name}: {COLOR_RESET}")

            # Normalize user message
            cleaned_message = raw_input.strip().lower()

            # Empty input validation
            if not cleaned_message:
                bot_say("You didn't enter anything. Please enter a message!\n")
                continue

            # Exit command handling
            if is_exit_command(cleaned_message):
                farewell = get_bot_response(cleaned_message, user_name)
                bot_say(f"{farewell}\n")
                print(f"{COLOR_ACCENT}{'-' * 62}{COLOR_RESET}")
                print("Conversation ended. Thank you for chatting!")
                print(f"{COLOR_ACCENT}{'=' * 62}{COLOR_RESET}")
                break

            # Process and display response
            response = get_bot_response(cleaned_message, user_name)
            bot_say(f"{response}\n")

        except (KeyboardInterrupt, EOFError):
            print("\n\nSession interrupted. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    run_chatbot()
