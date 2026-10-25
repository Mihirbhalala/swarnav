import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings

class Command(BaseCommand):
    help = "Loads the backed-up SQLite data into the currently connected database (e.g. PostgreSQL)."

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            default='datadump_sqlite.json',
            help='Path to the JSON dump file (default: datadump_sqlite.json)',
        )

    def handle(self, *args, **options):
        file_path = options['file']
        if not os.path.exists(file_path):
            self.stderr.write(self.style.ERROR(f"Backup file '{file_path}' not found."))
            return

        db_settings = settings.DATABASES['default']
        db_engine = db_settings.get('ENGINE', '')
        db_name = db_settings.get('NAME', '')
        self.stdout.write(self.style.NOTICE(f"Current database engine: {db_engine}"))

        if 'postgresql' in db_engine:
            self.stdout.write(f"Ensuring PostgreSQL database '{db_name}' exists...")
            try:
                import psycopg2
                from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
                user = db_settings.get('USER', 'postgres')
                password = db_settings.get('PASSWORD', '')
                host = db_settings.get('HOST', 'localhost') or 'localhost'
                port = db_settings.get('PORT', '5432') or '5432'

                # Connect to maintenance database 'postgres' to check/create db_name
                conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host, port=port)
                conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cur = conn.cursor()
                cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (str(db_name),))
                exists = cur.fetchone()
                if not exists:
                    self.stdout.write(f"Database '{db_name}' not found. Creating it now...")
                    cur.execute(f'CREATE DATABASE "{db_name}";')
                    self.stdout.write(self.style.SUCCESS(f"Database '{db_name}' created successfully!"))
                else:
                    self.stdout.write(f"Database '{db_name}' already exists.")
                cur.close()
                conn.close()
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Database check notice: {e}"))

        self.stdout.write("Running database migrations...")
        call_command('migrate', interactive=False)

        self.stdout.write(f"Loading data from '{file_path}'...")
        call_command('loaddata', file_path)

        self.stdout.write(self.style.SUCCESS("All data successfully restored into PostgreSQL!"))
