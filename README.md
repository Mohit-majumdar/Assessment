# Django Chat App

A simple and scalable chat application built with Django. This project allows users to register, log in, and chat in real time. It also supports Docker for easy deployment.

---

## Features

- User authentication (sign up, log in, log out)
- Real-time messaging
- Group chats
- Scalable backend with Django

---

## Requirements

- Python 3.8+
- Django 4.x
- SQLite (default) or PostgreSQL
- Redis (for message queueing)
- Docker (optional)
- Node.js and npm (for WebSocket front-end, if needed)

---

## Local Installation

### Step 1: Clone the Repository
```bash
$ git clone https://github.com/Mohit-majumdar/Assessment.git
$ cd django-chat-app
```

### Step 2: Create a Virtual Environment
```bash
$ python3 -m venv env
$ source env/bin/activate  # Linux/macOS
$ env\Scripts\activate   # Windows
```

### Step 3: Install Dependencies
```bash
$ pip install -r requirements.txt
```

### Step 4: Configure the Database
By default, SQLite is used. To switch to PostgreSQL, update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chat_db',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Then apply migrations:
```bash
$ python manage.py migrate
```

### Step 5: Start the Development Server
```bash
$ python manage.py runserver
```
Visit `http://127.0.0.1:8000` to view the app.

---

## Docker Installation

### Step 1: Clone the Repository
```bash
$ git clone https://github.com/Mohit-majumdar/Assessment.git
$ cd django-chat-app
```

### Step 2: Build and Run the Docker Containers
Ensure Docker and Docker Compose are installed.

```bash
$ docker-compose up --build
```

### Step 3: Access the Application
Visit `http://127.0.0.1:8000` to view the app.

---

## Environment Variables

Set the following environment variables in a `.env` file or Docker Compose:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://user:password@db:5432/chat_db
REDIS_URL=redis://redis:6379/0
```

---



