"""
Interactive Terminal Runner for Swarnav AI Pilgrimage Assistant.
Allows direct terminal chat with the Advanced RAG + Agent Assistant.
Usage:
    python manage.py run_ai_chat
"""
import sys
from django.core.management.base import BaseCommand
from core.ai.agent_service import execute_agent_chat
from core.ai.ai_config import is_ai_configured, GEMINI_MODEL


class Command(BaseCommand):
    help = "Run an interactive terminal session with the Swarnav AI Pilgrimage Assistant."

    def handle(self, *args, **options):
        configured = is_ai_configured()
        mode_text = f"Live Google Gemini ({GEMINI_MODEL})" if configured else "Local RAG & Tool Fallback Engine"

        self.stdout.write(self.style.SUCCESS("=" * 65))
        self.stdout.write(self.style.SUCCESS("  ✨ SWARNAV AI PILGRIMAGE ASSISTANT (INTERACTIVE RUNNER) ✨"))
        self.stdout.write(self.style.SUCCESS("=" * 65))
        self.stdout.write(f"Engine Mode: {mode_text}")
        self.stdout.write("Supported Languages: English, ગુજરાતી (Gujarati), हिंदी (Hindi)")
        self.stdout.write("Type 'exit' or 'quit' to end session. Type 'reset' to clear memory.\n")

        session_history = []

        # Initial Greeting
        print("Assistant: 🙏 Jai Shri Krishna / Har Har Mahadev! Welcome to Swarnav Tour & Travels.")
        print("           How may I help you with your sacred yatra today?\n")

        while True:
            try:
                user_input = input("You: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\nSession ended. Har Har Mahadev!")
                break

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\nAssistant: 🙏 Shubh Yatra! Wishing you a blessed journey. Har Har Mahadev!")
                break

            if user_input.lower() == 'reset':
                session_history = []
                print("\n[Conversation memory reset]\n")
                continue

            # Process query
            try:
                res = execute_agent_chat(user_input, session_history=session_history)
                reply = res.get("reply", "")

                print(f"\nAssistant:\n{reply}\n")

                if res.get("action_card"):
                    card = res["action_card"]
                    print(f"--- [ACTION CARD] ---")
                    print(f"Reference ID: {card.get('inquiry_ref')}")
                    print(f"WhatsApp Handoff Link: {card.get('whatsapp_link')}")
                    print("---------------------\n")

                if res.get("suggested_questions"):
                    print("Suggested Follow-ups:")
                    for q in res["suggested_questions"]:
                        print(f"  • {q}")
                    print()

                # Update history
                session_history.append({"sender": "user", "text": user_input})
                session_history.append({"sender": "bot", "text": reply})
                session_history = session_history[-10:]

            except Exception as e:
                print(f"\n[Error processing request: {e}]\n")
