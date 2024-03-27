import os

class Config:
    # Klucz sekretny dla zabezpieczenia aplikacji
    SECRET_KEY = '5749372817563927'

    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Tomek")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "blogasylogasy")

    # Ustawienia bazy danych
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Przykładowa baza SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Wyłącza sygnały o modyfikacjach w bazie danych

    # Konfiguracja maila
    MAIL_SERVER = 'smtp.example.com'  # Serwer poczty wychodzącej
    MAIL_PORT = 587  # Port serwera poczty
    MAIL_USE_TLS = True  # Używa TLS dla połączeń z serwerem poczty
    MAIL_USERNAME = 'your-email@example.com'  # Twój adres e-mail
    MAIL_PASSWORD = 'your-email-password'  # Twoje hasło do poczty

    # Konfiguracja paginacji (opcjonalne)
    POSTS_PER_PAGE = 10  # Ilość postów na stronę
