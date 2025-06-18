# Django Blog

A Django-based blog application using Bootstrap for single-user casual blogging.

## Setup Instructions

### Environment Variables

1. Copy the `.env.example` file to create your own `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and set your configuration:
   - `SECRET_KEY`: Your Django secret key (keep this secret in production!)
   - `DEBUG`: Set to `True` for development, `False` for production
   - `ALLOWED_HOSTS`: Comma-separated list of allowed hosts (can be empty for local development)

3. To generate a new secret key, you can use:
   ```bash
   python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

### Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python3 manage.py migrate
   ```

3. Create a superuser (optional):
   ```bash
   python3 manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python3 manage.py runserver
   ```

The blog will be available at http://localhost:8000/