# Real-Time Speed Monitoring System

A full-stack real-time speed monitoring system built as an independent project. The system simulates sensor-generated speed data, processes it through a Django backend using WebSockets, stores the data in PostgreSQL, and displays live updates on a React frontend. The entire application is containerized using Docker.

---

## Setup Instructions

1. Prerequisites:
Make sure you have installed:
- Docker
- Docker Compose
- Python 3.12+ (for sensor script)

2. Environment Variables
Create a .env file in the root directory:
- DJANGO_SECRET_KEY=django-insecure-change-this
- POSTGRES_DB=db_name
- POSTGRES_USER=username
- POSTGRES_PASSWORD=your_password

3. Build and Start Containers
From the project root:
- docker compose up

4. Run database migrations:
- docker compose run --rm backend python manage.py migrate

5. Run the speed_generator:
Execute the speed_generator python file outside the docker
- python speed_generator.py

6. Open the frontend at localhost:5173
