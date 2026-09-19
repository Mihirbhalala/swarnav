"""
Django Management Command to build the Advanced RAG Knowledge Index for Swarnav AI Assistant.
Extracts models (TourPackage, ItineraryDay, etc.) and source Word documents.
Usage:
    python manage.py build_ai_index [--with-embeddings]
"""
from django.core.management.base import BaseCommand
from core.ai.rag_engine import build_and_save_index, load_index
from core.ai.ai_config import is_ai_configured


class Command(BaseCommand):
    help = "Extracts pilgrimage tours, day-by-day itineraries and documents into the AI RAG Knowledge Index."

    def add_arguments(self, parser):
        parser.add_argument(
            '--with-embeddings',
            action='store_true',
            help='Generate remote vector embeddings via Google Gemini text-embedding-004 API (requires GEMINI_API_KEY)',
        )

    def handle(self, *args, **options):
        with_embeddings = options.get('with_embeddings', False)
        if with_embeddings and not is_ai_configured():
            self.stdout.write(
                self.style.WARNING("Warning: GEMINI_API_KEY is not configured in .env. Falling back to local index.")
            )
            with_embeddings = False

        self.stdout.write("Building Swarnav AI Knowledge Index...")
        total = build_and_save_index(force_embeddings=with_embeddings)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully compiled and saved {total} knowledge items into knowledge index!")
        )
