# 📝 Quizly API - Quiz Management Backend

Quizly ist ein leistungsstarkes Django REST Framework Backend für die Erstellung, Verwaltung und Durchführung von Video-basierten Quizzes. Benutzer können Quizzes aus YouTube-Videos generieren, eigene Fragen verwalten und den Fortschritt verfolgen.

---

## 🚀 Key Features

### 🔐 Authentication
- **User Registration & Login:** Einfache Registrierung und Anmeldung.
- **Token-basierte Authentifizierung:** Sicherer Zugriff auf alle geschützten Endpunkte.
- **Logout & Token Refresh:** Unterstützt sicheren Logout und Erneuerung von Tokens.

### 📚 Quiz Management
- Erstellung von Quizzes: Generiere Quizzes basierend auf YouTube-Videos.
- Fragen & Antworten: Jede Frage enthält mehrere Optionen und eine richtige Antwort.
- CRUD-Unterstützung: Benutzer können ihre Quizzes erstellen, lesen, aktualisieren und löschen.
- Benutzerbasierte Zugriffe: Jeder Benutzer kann nur eigene Quizzes verwalten.

### 📊 Platform Insights
- API liefert Details zu Quizzes inklusive Fragen, Video-URLs, Erstellungs- und Aktualisierungszeiten.

---

## 🛠 Tech Stack
- **Framework:** Django + Django REST Framework
- **Database:** SQLite (Development)
- **Authentication:** JWT-Token (Access & Refresh)

---

## 🔧 Installation & Setup

1. **Clone the project:**

        git clone https://github.com/Younes-Darabi/quizly.git
        cd quizly


3. Set up a Virtual Environment:

        python -m venv venv
   
# Windows:

        venv\Scripts\activate
        
# Linux/Mac:
   
        source venv/bin/activate

3. Environment Configuration:
   Create a `.env` file in the root directory and add your secret key and google api key:
   ```env
   SECRET_KEY=your_secret_key_here
   GOOGLE_API_KEY=your-google-api-here

4. Install Dependencies:

        pip install -r requirements.txt

5. Apply Database Migrations:

        python manage.py migrate

6. Run the Development Server:

        python manage.py runserver


---

## 📍 API Endpoints Overview
### 🔐 Authentication

- POST /api/register/ — Register a new user
- POST /api/login/ — Login and set authentication cookies
- POST /api/logout/ — Logout and invalidate all tokens
- POST /api/token/refresh/ — Refresh the access token using the refresh token

### 📚 Quiz Management

- POST /api/quizzes/ — Create a new quiz from a YouTube URL
- GET /api/quizzes/ — List all quizzes of the authenticated user
- GET /api/quizzes/{id}/ — Retrieve a specific quiz of the authenticated user
- PATCH /api/quizzes/{id}/ — Partially update a quiz (title, description, etc.)
- DELETE /api/quizzes/{id}/ — Delete a quiz and all its questions permanently

---

### 🔗 Related Projects
* **Frontend Repository:** [https://github.com/Developer-Akademie-Backendkurs/project.Quizly](https://github.com/Developer-Akademie-Backendkurs/project.Quizly)

---

Developed with ❤️ by Younes
