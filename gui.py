"""CodeAlpha Basic Chatbot - Desktop GUI Edition.

A native desktop graphical user interface using Python's built-in Tkinter.
Runs out of the box with zero external dependencies.
Reuses the deterministic rule-based logic in main.py without retraining.
"""

import datetime
import os
import sys
import tkinter as tk
from tkinter import messagebox, ttk

# Ensure local directory is on sys.path to import main
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from main import get_bot_response, is_exit_command


class ChatbotGUI:
    """Desktop Graphical Interface for CodeAlpha Basic Chatbot."""

    # Color Palette (Modern Dark Theme)
    BG_DARK = "#181824"
    BG_PANEL = "#212130"
    BG_HEADER = "#29293d"
    BG_INPUT = "#2e2e42"
    BG_USER_MSG = "#3b82f6"
    BG_BOT_MSG = "#2a2d3e"
    TEXT_MAIN = "#f3f4f6"
    TEXT_MUTED = "#9ca3af"
    ACCENT_CYAN = "#38bdf8"
    ACCENT_GREEN = "#4ade80"
    BORDER_COLOR = "#374151"

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("CodeAlpha Basic Chatbot - Desktop GUI")
        self.root.geometry("750x800")
        self.root.minsize(600, 650)
        self.root.configure(bg=self.BG_DARK)

        self.user_name = "Friend"

        self._setup_styles()
        self._build_header()
        self._build_quick_actions()
        self._build_chat_display()
        self._build_input_area()

        # Display initial welcome message
        self._display_initial_greeting()

    def _setup_styles(self):
        """Configures ttk styles for a unified modern aesthetic."""
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TButton",
            background="#33334d",
            foreground=self.TEXT_MAIN,
            borderwidth=0,
            focuscolor="none",
            font=("Segoe UI", 9),
            padding=6,
        )
        style.map(
            "TButton",
            background=[("active", "#444466"), ("pressed", "#252538")],
            foreground=[("active", "#ffffff")],
        )

        style.configure(
            "Accent.TButton",
            background="#2563eb",
            foreground="#ffffff",
            font=("Segoe UI", 10, "bold"),
            padding=8,
        )
        style.map(
            "Accent.TButton",
            background=[("active", "#1d4ed8"), ("pressed", "#1e40af")],
        )

        style.configure(
            "Clear.TButton",
            background="#dc2626",
            foreground="#ffffff",
            font=("Segoe UI", 9),
            padding=4,
        )
        style.map(
            "Clear.TButton",
            background=[("active", "#b91c1c"), ("pressed", "#991b1b")],
        )

    def _build_header(self):
        """Builds top bar with title, status badge, and user name editor."""
        header_frame = tk.Frame(self.root, bg=self.BG_HEADER, height=65)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        # Left: Bot Title & Tagline
        title_box = tk.Frame(header_frame, bg=self.BG_HEADER)
        title_box.pack(side=tk.LEFT, padx=15, pady=8)

        lbl_title = tk.Label(
            title_box,
            text="🤖 CodeAlpha Basic Chatbot",
            font=("Segoe UI", 13, "bold"),
            fg=self.TEXT_MAIN,
            bg=self.BG_HEADER,
        )
        lbl_title.pack(anchor="w")

        lbl_subtitle = tk.Label(
            title_box,
            text="Interactive Rule-Based Engine  ●  100% Deterministic",
            font=("Segoe UI", 8),
            fg=self.ACCENT_GREEN,
            bg=self.BG_HEADER,
        )
        lbl_subtitle.pack(anchor="w")

        # Right: User Name Editor & Clear Button
        right_box = tk.Frame(header_frame, bg=self.BG_HEADER)
        right_box.pack(side=tk.RIGHT, padx=15, pady=12)

        lbl_name = tk.Label(
            right_box,
            text="Name:",
            font=("Segoe UI", 9),
            fg=self.TEXT_MUTED,
            bg=self.BG_HEADER,
        )
        lbl_name.pack(side=tk.LEFT, padx=(0, 5))

        self.name_entry = tk.Entry(
            right_box,
            font=("Segoe UI", 9),
            bg=self.BG_INPUT,
            fg=self.TEXT_MAIN,
            insertbackground="white",
            relief=tk.FLAT,
            width=12,
        )
        self.name_entry.insert(0, self.user_name)
        self.name_entry.pack(side=tk.LEFT, padx=(0, 6), ipady=3)
        self.name_entry.bind("<FocusOut>", self._update_user_name)
        self.name_entry.bind("<Return>", self._update_user_name)

        btn_clear = ttk.Button(
            right_box,
            text="🗑️ Clear",
            style="Clear.TButton",
            command=self._clear_chat,
        )
        btn_clear.pack(side=tk.LEFT)

    def _update_user_name(self, event=None):
        """Updates user name from entry field."""
        new_name = self.name_entry.get().strip()
        if new_name:
            self.user_name = new_name.title()
        else:
            self.user_name = "Friend"
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, "Friend")

    def _build_quick_actions(self):
        """Toolbar with one-click action buttons."""
        quick_frame = tk.Frame(self.root, bg=self.BG_PANEL, height=45)
        quick_frame.pack(fill=tk.X, side=tk.TOP, padx=10, pady=(6, 0))

        lbl_quick = tk.Label(
            quick_frame,
            text="Quick Prompts:",
            font=("Segoe UI", 8, "bold"),
            fg=self.TEXT_MUTED,
            bg=self.BG_PANEL,
        )
        lbl_quick.pack(side=tk.LEFT, padx=(8, 8), pady=6)

        actions = [
            ("😄 Joke", "tell me a joke"),
            ("💡 Fact", "tell me a fact"),
            ("🪙 Coin", "flip a coin"),
            ("🎲 Dice", "roll a die"),
            ("⏰ Time", "what time is it"),
            ("📅 Date", "what is today's date"),
            ("❓ Help", "help"),
        ]

        for label, prompt_val in actions:
            btn = ttk.Button(
                quick_frame,
                text=label,
                style="TButton",
                command=lambda p=prompt_val: self._send_prompt(p),
            )
            btn.pack(side=tk.LEFT, padx=3, pady=6)

    def _build_chat_display(self):
        """Constructs scrollable text conversation log."""
        chat_container = tk.Frame(self.root, bg=self.BG_DARK)
        chat_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)

        self.chat_history = tk.Text(
            chat_container,
            bg=self.BG_DARK,
            fg=self.TEXT_MAIN,
            font=("Segoe UI", 10),
            wrap=tk.WORD,
            state=tk.DISABLED,
            bd=0,
            padx=12,
            pady=12,
            relief=tk.FLAT,
        )
        scrollbar = ttk.Scrollbar(
            chat_container,
            orient=tk.VERTICAL,
            command=self.chat_history.yview,
        )
        self.chat_history.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Text Tag Styling
        self.chat_history.tag_configure("bot_header", font=("Segoe UI", 9, "bold"), foreground=self.ACCENT_CYAN)
        self.chat_history.tag_configure("user_header", font=("Segoe UI", 9, "bold"), foreground=self.ACCENT_GREEN)
        self.chat_history.tag_configure("timestamp", font=("Segoe UI", 8), foreground=self.TEXT_MUTED)
        self.chat_history.tag_configure("bot_body", font=("Segoe UI", 10), foreground="#ffffff", lmargin1=15, lmargin2=15)
        self.chat_history.tag_configure("user_body", font=("Segoe UI", 10), foreground="#e0e7ff", lmargin1=15, lmargin2=15)
        self.chat_history.tag_configure("system_msg", font=("Segoe UI", 9, "italic"), foreground="#fbbf24", justify="center")

    def _build_input_area(self):
        """Constructs bottom message input field and send button."""
        bottom_frame = tk.Frame(self.root, bg=self.BG_PANEL, height=70)
        bottom_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=(0, 10))

        input_inner = tk.Frame(bottom_frame, bg=self.BG_PANEL)
        input_inner.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.msg_entry = tk.Entry(
            input_inner,
            font=("Segoe UI", 11),
            bg=self.BG_INPUT,
            fg=self.TEXT_MAIN,
            insertbackground="white",
            relief=tk.FLAT,
            bd=0,
        )
        self.msg_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8), ipady=8)
        self.msg_entry.focus_set()
        self.msg_entry.bind("<Return>", lambda event: self._handle_user_submit())

        btn_send = ttk.Button(
            input_inner,
            text="Send ➔",
            style="Accent.TButton",
            command=self._handle_user_submit,
        )
        btn_send.pack(side=tk.RIGHT, fill=tk.Y)

    def _display_initial_greeting(self):
        """Appends the welcome greeting into the chat log."""
        self.chat_history.configure(state=tk.NORMAL)
        self.chat_history.insert(tk.END, "--- Basic Chatbot Session Started ---\n\n", "system_msg")
        self.chat_history.configure(state=tk.DISABLED)

        welcome_text = (
            "Hello! I am your interactive, rule-based chatbot.\n"
            "I can converse, tell jokes, share tech facts, check time, roll dice, and more!\n"
            "Type a message or use the Quick Prompts toolbar above."
        )
        self._append_message("Bot", welcome_text, is_bot=True)

    def _append_message(self, sender: str, message: str, is_bot: bool):
        """Appends a styled message to the chat view."""
        self.chat_history.configure(state=tk.NORMAL)
        time_str = datetime.datetime.now().strftime("%I:%M %p")

        if is_bot:
            self.chat_history.insert(tk.END, f"🤖 {sender}  ", "bot_header")
            self.chat_history.insert(tk.END, f"[{time_str}]\n", "timestamp")
            self.chat_history.insert(tk.END, f"{message}\n\n", "bot_body")
        else:
            self.chat_history.insert(tk.END, f"👤 {sender}  ", "user_header")
            self.chat_history.insert(tk.END, f"[{time_str}]\n", "timestamp")
            self.chat_history.insert(tk.END, f"{message}\n\n", "user_body")

        self.chat_history.configure(state=tk.DISABLED)
        self.chat_history.see(tk.END)

    def _send_prompt(self, prompt_text: str):
        """Fires an automated prompt message."""
        self._update_user_name()
        self._append_message(self.user_name, prompt_text, is_bot=False)
        bot_response = get_bot_response(prompt_text.strip().lower(), user_name=self.user_name)
        self._append_message("Bot", bot_response, is_bot=True)

    def _handle_user_submit(self):
        """Reads user entry, evaluates rules, and displays response."""
        user_input = self.msg_entry.get().strip()
        if not user_input:
            return

        self._update_user_name()
        self.msg_entry.delete(0, tk.END)

        # Append User Message
        self._append_message(self.user_name, user_input, is_bot=False)

        # Normalize and compute response
        cleaned_msg = user_input.lower()
        bot_response = get_bot_response(cleaned_msg, user_name=self.user_name)

        # Append Bot Message
        self._append_message("Bot", bot_response, is_bot=True)

        # If exit command is received, notify user
        if is_exit_command(cleaned_msg):
            self.chat_history.configure(state=tk.NORMAL)
            self.chat_history.insert(tk.END, "--- Conversation Finished ---\n\n", "system_msg")
            self.chat_history.configure(state=tk.DISABLED)
            self.chat_history.see(tk.END)

    def _clear_chat(self):
        """Clears all conversation messages."""
        if messagebox.askyesno("Clear Chat", "Are you sure you want to clear the conversation?"):
            self.chat_history.configure(state=tk.NORMAL)
            self.chat_history.delete("1.0", tk.END)
            self.chat_history.configure(state=tk.DISABLED)
            self._display_initial_greeting()


def launch_gui():
    """Starts the desktop chatbot application."""
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    launch_gui()
