# CodeAlpha_Basic_Chatbot (Interactive Edition)

A lively, lightweight, console-based **rule-based chatbot** implemented in pure Python. Developed as an internship project for the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Objective

The primary objective of this project is to build a foundational, rule-driven conversational agent that interacts with users in a terminal environment. The project emphasizes:
- Writing clean, modular, and readable Python code following PEP 8.
- Applying core programming constructs: loops, conditionals (`if-elif-else`), string processing, and functions.
- Adding **interactive user engagement** (personalized user name, simulated typing effect, terminal styling, live time/date, and mini-games) while staying **100% rule-based without AI/LLM models or external APIs**.

---

## ❓ Problem Statement

Understanding human-computer interaction begins with deterministic rule-based systems. The challenge is to construct a console chatbot that:
1. Greets the user upon launch and introduces itself.
2. Interactively asks for the user's name to personalize the conversation.
3. Accepts and validates text input (handling uppercase, lowercase, and whitespace variations).
4. Matches messages against predefined rules using `if-elif-else` branches.
5. Provides interactive utilities (telling jokes, facts, coin toss, dice roll, date/time).
6. Emits appropriate responses and fallback messages with realistic typing simulation.
7. Gracefully terminates upon receiving designated exit keywords.

---

## 🤖 What is a Rule-Based Chatbot?

A **rule-based chatbot** (scripted/decision-tree agent) operates on predetermined rules, keywords, and conditional logic. Unlike AI/LLM chatbots that generate responses dynamically using statistical language models:
- Rule-based bots follow explicit `if/elif/else` conditions.
- They only recognize patterns and vocabulary explicitly programmed by the developer.
- Responses are predictable, instantaneous, deterministic, and never hallucinate.
- They require no internet connection, no heavy dependencies, and no API keys.

---

## ✨ Interactive Features

- **Personalized Experience**: Asks for the user's name at the start and uses it throughout the conversation (e.g., in prompts, greetings, and courtesy responses).
- **Simulated Typing Effect**: Emulates a real chatbot typing responses character-by-character with automatic pipe detection.
- **Terminal Styling (ANSI)**: Utilizes clean terminal color codes (Cyan for Bot, Green for User, Yellow for highlights).
- **Live Utilities**: Provides real-time clock (`time`) and calendar date (`date`) using Python's `datetime` library.
- **Interactive Mini-Games**:
  - `tell me a joke`: Curated developer/programmer jokes.
  - `tell me a fact`: Fascinating computer science history facts.
  - `flip a coin`: Simulates coin toss (`Heads` or `Tails`).
  - `roll a die`: Simulates a 6-sided dice roll.
- **Standard Library Only**: 100% pure Python with zero third-party dependencies.
- **Case Insensitive**: Normalizes all inputs (`"HELLO"`, `"Hello"`, and `"hello"` are evaluated identically).
- **Empty Input Validation**: Prompts the user to re-enter a message if blank lines or spaces are submitted.
- **Graceful Termination**: Exits cleanly when the user types any exit command (`bye`, `goodbye`, `exit`, `quit`) or presses `Ctrl+C`.
- **Default Fallback**: Informs the user when an unrecognized query is provided and guides them to available commands via `help`.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3.8+** | Core programming language |
| **`tkinter` & `ttk`** | Native desktop graphical user interface (zero dependencies) |
| **Streamlit** | Modern, interactive browser-based web user interface |
| **`datetime` Module** | Live time and date utilities |
| **`random` Module** | Randomization for jokes, facts, coin flip, and dice roll |
| **`time` Module** | Typewriter typing delay simulation |
| **`sys` Module** | Stream handling and graceful system exits |
| **`unittest` Module** | Automated testing suite for input-output validation |

---

## 🔍 How the Chatbot Works

The execution flow of the chatbot follows a structured linear loop:

```
[Start Program]
       │
       ▼
[Display Welcome Banner & Instructions]
       │
       ▼
[Interactive Step: Prompt for User Name]
       │
       ▼
[Prompt User for Input: <UserName>: ]
       │
       ▼
[Preprocess Input: strip() & lower()]
       │
       ├─► Is input empty? ───────► (Yes) ──► Print warning prompt ──► Loop back
       │
       ├─► Is exit command? ──────► (Yes) ──► Print farewell ────────► [End Program]
       │
       ▼
[Evaluate get_bot_response()]
  ├── Match Greeting rules (Personalized)
  ├── Match Well-being rules
  ├── Match Identity rules (Bot identity & User name)
  ├── Match Live Utilities (Time & Date)
  ├── Match Fun & Games (Jokes, Facts, Coin, Dice)
  ├── Match Help & Options
  ├── Match Gratitude rules
  └── Fallback (Unknown input rule)
       │
       ▼
[Display Bot Response with Typing Effect]
       │
       ▼
[Repeat Conversation Loop]
```

---

## 💬 Supported Commands & Queries

| Category | Example User Inputs | Bot Action / Response |
| :--- | :--- | :--- |
| **Greetings** | `hello`, `hi`, `hey`, `hello there` | `"Hi <Name>! How can I help you today?"` |
| **Status / Well-being** | `how are you`, `how are you doing`, `how's it going` | `"I'm fine, thanks! How are you doing today?"` |
| **User Status Reply** | `i am good`, `i am fine`, `doing well`, `great` | `"Glad to hear that, <Name>! How can I assist you?"` |
| **Bot Identity** | `what is your name`, `who are you` | `"I'm a simple Python rule-based chatbot created for the CodeAlpha internship."` |
| **User Identity** | `what is my name`, `who am i` | `"Your name is <Name>! It's a pleasure chatting with you."` |
| **Live Time** | `time`, `what time is it`, `current time` | `[Time] The current time is HH:MM AM/PM.` |
| **Live Date** | `date`, `what is today's date`, `today's date` | `[Date] Today is Day, Month DD, YYYY.` |
| **Jokes** | `joke`, `tell me a joke`, `make me laugh` | `[Joke] (Random programming joke)` |
| **Tech Facts** | `fact`, `tell me a fact`, `fun fact` | `[Fact] (Random computer science fact)` |
| **Coin Flip** | `flip a coin`, `coin flip` | `[Coin Flip] Result: It's Heads/Tails!` |
| **Dice Roll** | `roll a die`, `roll dice` | `[Dice Roll] Result: You rolled a [1-6]!` |
| **Help & Guide** | `help`, `what can you do`, `commands` | *(Lists all supported commands categorized)* |
| **Gratitude** | `thank you`, `thanks`, `thanks a lot` | `"You're very welcome, <Name>! Feel free to ask if you need anything else."` |
| **Exit Commands** | `bye`, `goodbye`, `exit`, `quit` | `"Goodbye! Have a wonderful day!"` *(Ends conversation)* |
| **Unrecognized Input** | *(Any unrecognized query)* | `"Sorry, I don't understand that yet. Type 'help' to see what I can do."` |

---

## 🚀 Installation Instructions

### Prerequisites
- Python 3.8 or higher installed on your machine.
- Verify your Python installation by running:
  ```bash
  python --version
  ```

### Clone or Download the Project
```bash
git clone https://github.com/<your-username>/CodeAlpha_Basic_Chatbot.git
cd CodeAlpha_Basic_Chatbot
```

---

## 💻 How to Run

You can interact with the chatbot in three different modes:

### 1. Modern Web UI (Streamlit)
Launch the interactive web-based chat assistant in your browser:
```bash
streamlit run app.py
```
*Features: Chat bubbles, user personalization, sidebar quick prompts (Jokes, Facts, Dice, Coin, Time, Date), and chat reset.*

### 2. Native Desktop GUI (Tkinter)
Launch the desktop window with zero external dependencies (pure Python standard library):
```bash
python gui.py
```
*Features: Dark theme window, quick-action chips toolbar, user name editor, scrollable conversation history, and clear chat option.*

### 3. Terminal / Console Mode
Run directly in your command line or PowerShell:
```bash
python main.py
```

---

## 🧪 Automated Testing

To run the automated unit test suite and verify rule-based logic:
```bash
python -m unittest test_chatbot.py
```

---

## 📋 Example Conversation

```text
==============================================================
        *** WELCOME TO CODEALPHA BASIC CHATBOT ***        
==============================================================
Hello! I am an interactive, rule-based console assistant.
I can converse, tell jokes, share tech facts, check time, and more!
- Type 'help' anytime to explore everything I can do.
- Type 'bye', 'exit', or 'quit' to end our chat.
--------------------------------------------------------------
Bot: Before we begin, may I know your name? (Press Enter to skip): Harsh
Bot: Nice to meet you, Harsh! How can I help you today?

Harsh: HELLO
Bot: Hi Harsh! How can I help you today?

Harsh: how are you
Bot: I'm fine, thanks! How are you doing today?

Harsh: what is my name
Bot: Your name is Harsh! It's a pleasure chatting with you.

Harsh: what time is it
Bot: [Time] The current time is 05:05 PM.

Harsh: tell me a joke
Bot: [Joke] Why do programmers prefer dark mode? Because light attracts bugs!

Harsh: flip a coin
Bot: [Coin Flip] Result: It's Heads!

Harsh: roll a die
Bot: [Dice Roll] Result: You rolled a 6!

Harsh: thanks
Bot: You're very welcome, Harsh! Feel free to ask if you need anything else.

Harsh: bye
Bot: Goodbye! Have a wonderful day!

--------------------------------------------------------------
Conversation ended. Thank you for chatting!
==============================================================
```

---

## 🧪 Testing Cases

The project includes an automated suite in `test_chatbot.py` testing the following test matrix:

| Test Case | Input | Expected Output | Status |
| :--- | :--- | :--- | :--- |
| **TC-01: Greeting Variation** | `"Hi"`, `"HELLO"`, `"hey"` | Greeting response returned | Passed |
| **TC-02: Mixed Case & Whitespace** | `"   HeLLO  "` | Preprocessed and recognized | Passed |
| **TC-03: Bot Status** | `"how are you doing"` | Returns bot state | Passed |
| **TC-04: Bot Identity** | `"what is your name"` | Identifies as rule-based bot | Passed |
| **TC-05: User Name Personalization** | `"hello"`, `"what is my name"` | Addresses user by name | Passed |
| **TC-06: Live Time & Date** | `"time"`, `"date"` | Returns formatted current time/date | Passed |
| **TC-07: Interactive Games** | `"tell me a joke"`, `"flip a coin"`, `"roll a die"` | Returns random dynamic rule result | Passed |
| **TC-08: Empty Input** | `""`, `"    "` | Prompts user to input text | Passed |
| **TC-09: Exit Command** | `"exit"`, `"quit"`, `"bye"` | Confirms exit and breaks loop | Passed |
| **TC-10: Unrecognized Query** | `"tell me the stock price"` | Returns default fallback message | Passed |
| **TC-11: Interrupt Handling** | `Ctrl + C` | Exits cleanly without crash trace | Passed |

---

## ⚠️ Limitations

- **Fixed Rule Scope**: Operates only on predefined conditional branches and exact matched phrases.
- **No Machine Learning**: Does not use generative models or semantic neural search.
- **No Long-term Memory**: Sessions are reset upon program exit.

---

## 🔮 Future Improvements

1. **Fuzzy String Matching**: Integrate `difflib` for automatic typo tolerance (e.g., `"helo"` -> `"hello"`).
2. **External Knowledge File**: Store responses and trigger keywords in a `JSON` configuration file.
3. **Graphical User Interface (GUI)**: Create a desktop interface using `tkinter` or web interface with `Streamlit`.
4. **Chat History Logging**: Save session transcripts to a `.txt` log file.

---

## 👤 Author

- **Project Developer**: Harsh
- **Internship**: CodeAlpha Python Programming Internship
- **Project Name**: `CodeAlpha_Basic_Chatbot`
#   B a s i c - c h a t b o t  
 