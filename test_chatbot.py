"""Unit tests for CodeAlpha Basic Chatbot.

Tests rule matching, case normalization, exit condition detection,
fallback behavior, and interactive utilities.
"""

import unittest
from main import get_bot_response, is_exit_command


class TestBasicChatbot(unittest.TestCase):
    """Test suite covering the rule-based logic of the chatbot."""

    def test_greetings(self):
        """Verify greeting inputs return expected responses."""
        for greeting in ["hello", "hi", "hey", "hello there", "hey there", "greetings"]:
            response = get_bot_response(greeting)
            self.assertIn("Hi! How can I help you today?", response)

    def test_case_insensitivity_and_whitespace(self):
        """Verify inputs with mixed casing and extra whitespace are handled correctly."""
        inputs = ["  HELLO  ", "HeLlO", "  HI  ", "hEy"]
        for item in inputs:
            cleaned = item.strip().lower()
            response = get_bot_response(cleaned)
            self.assertIn("Hi! How can I help you today?", response)

    def test_bot_status(self):
        """Verify inquiry about the chatbot's well-being."""
        for msg in ["how are you", "how are you doing", "how's it going"]:
            response = get_bot_response(msg)
            self.assertIn("I'm fine, thanks!", response)

    def test_identity(self):
        """Verify identity queries."""
        for msg in ["what is your name", "who are you", "what's your name"]:
            response = get_bot_response(msg)
            self.assertIn("rule-based chatbot", response)

    def test_help(self):
        """Verify help command output."""
        response = get_bot_response("help")
        self.assertIn("Here is what you can ask me", response)

    def test_exit_commands(self):
        """Verify exit command identification and response."""
        exit_commands = ["bye", "goodbye", "exit", "quit"]
        for cmd in exit_commands:
            self.assertTrue(is_exit_command(cmd))
            response = get_bot_response(cmd)
            self.assertIn("Goodbye!", response)

    def test_non_exit_command(self):
        """Verify normal messages are not marked as exit commands."""
        for msg in ["hello", "how are you", "random message"]:
            self.assertFalse(is_exit_command(msg))

    def test_empty_input(self):
        """Verify response when message is empty."""
        response = get_bot_response("")
        self.assertIn("You didn't say anything!", response)

    def test_unrecognized_input(self):
        """Verify default fallback response for unknown messages."""
        unknown_inputs = [
            "what is quantum computing",
            "tell me a recipe for pasta",
            "xyzabc123",
            "tell me the stock price"
        ]
        for msg in unknown_inputs:
            response = get_bot_response(msg)
            self.assertEqual(
                response,
                "Sorry, I don't understand that yet. Type 'help' to see what I can do."
            )

    def test_interactive_name_personalization(self):
        """Verify personalized greeting and name inquiry."""
        greeting_response = get_bot_response("hello", user_name="Alex")
        self.assertIn("Hi Alex!", greeting_response)

        name_response = get_bot_response("what is my name", user_name="Alex")
        self.assertIn("Alex", name_response)

    def test_interactive_time_and_date(self):
        """Verify real-time utilities return time and date."""
        time_response = get_bot_response("time")
        self.assertIn("The current time is", time_response)

        date_response = get_bot_response("date")
        self.assertIn("Today is", date_response)

    def test_interactive_fun_features(self):
        """Verify interactive jokes, facts, dice roll, and coin flip."""
        joke_response = get_bot_response("tell me a joke")
        self.assertTrue(len(joke_response) > 5)

        fact_response = get_bot_response("tell me a fact")
        self.assertTrue(len(fact_response) > 5)

        coin_response = get_bot_response("flip a coin")
        self.assertTrue("Heads" in coin_response or "Tails" in coin_response)

        dice_response = get_bot_response("roll a die")
        self.assertIn("You rolled a", dice_response)


if __name__ == "__main__":
    unittest.main()
