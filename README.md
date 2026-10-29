# Swarnav Yatra Portal

A modern Django web platform for curated pilgrimage journeys, featuring comprehensive day-by-day itineraries, route guides, temple histories, and practical travel advisories for sacred Yatras across India (including the holy Char Dham Yatra).

---

## 🌟 Features

- **Char Dham & Sacred Yatra Itineraries:** Detailed day-by-day guides covering sacred shrines (Yamunotri, Gangotri, Kedarnath, Badrinath, Tungnath, Lakhamandal, Triyuginarayan, etc.).
- **Factual & Authentic Content:** Sourced directly from official temple committees (BKTC), Uttarakhand Tourism Development Board (UTDB), and District Portals.
- **Django Unfold Admin:** Modern, tailored administrative interface powered by `django-unfold`.
- **Responsive Frontend:** Clean and accessible layout with rich typography, imagery, and route maps.
- **AI-Powered Enhancements:** Integration with Google Gemini (`google-genai`) for itinerary assistance and content generation.

---

## 📂 Project Structure

```text
Swarnav/
├── core/                   # Core application (landing page, general views, layout templates)
├── yatras/                 # Yatra packages, itineraries, day-by-day routes, models & views
├── swarnav_project/        # Main Django project settings, WSGI/ASGI configuration, URL routing
├── templates/              # Base HTML templates and partials
├── static/                 # CSS, JavaScript, images, and brand assets
├── source_content/         # Original documentation, route outlines, and Word source files
├── db.sqlite3              # SQLite database
├── manage.py               # Django CLI management utility
├── requirements.txt        # Python package dependencies
├── CONTENT_SOURCES.md      # Citation of official government & temple administration sources
├── IMAGE_SOURCES.md        # Image provenance and attribution documentation
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+** (Python 3.12 recommended)
- **Virtual Environment** (`venv`)

### 2. Setup Virtual Environment

On Windows (PowerShell / Command Prompt):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and fill in any required variables:
```powershell
cp .env.example .env
```

Key environment variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `True` for development, `False` for production
- `GEMINI_API_KEY`: API key for Google Gemini (optional for AI generation)

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Once running, access the portal:
- **Public Site:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Dashboard:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ☁️ Free Deployment (Render + Neon)
1. Create a free PostgreSQL database at [neon.tech](https://neon.tech) and copy its connection string.
2. (Optional) Create a free [cloudinary.com](https://cloudinary.com) account and copy its `CLOUDINARY_URL`, so photos uploaded in admin are not lost when the server restarts.
3. On [render.com](https://render.com), choose **New → Blueprint** and select this repository. Render reads [`render.yaml`](render.yaml) and asks for the secret values (`DATABASE_URL`, `GEMINI_API_KEY`, email login, `CLOUDINARY_URL`, first admin username/email/password).
4. Every deploy runs [`build.sh`](build.sh): installs packages, collects static files, migrates, loads the tour data into an empty database, and creates the admin account if it doesn't exist.

Free tier notes: the site sleeps after ~15 minutes without visitors (the first visit then takes ~1 minute), and Render's free tier has no shell, so run one-off commands from your computer with `DATABASE_URL` pointing at Neon.

---

## 📚 Documentation & Sources
- [CONTENT_SOURCES.md](CONTENT_SOURCES.md) - Official government and temple portals referenced for sacred shrine details and route information.
- [IMAGE_SOURCES.md](IMAGE_SOURCES.md) - Complete attribution and usage rights for imagery across the portal.

---

## 🛠️ Tech Stack
- **Backend:** Django 5.2, Python 3
- **Admin Theme:** Django Unfold
- **Database:** SQLite (default for development) / PostgreSQL ready
- **Document Processing:** python-docx
- **Image Processing:** Pillow
- **AI Integration:** Google GenAI SDK (`google-genai`)
