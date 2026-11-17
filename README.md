# teamflow-workspace

A collaborative workspace for managing team projects and tasks.

## Technologies
- Python 3.12
- FastAPI
- Uvicorn
- Docker

## Project Structure

```text
teamflow-workspace/
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Build Docker Image

Build the Docker image:

```bash
docker build -t teamflow-workspace .
```

## Run Docker Container

Start the container:

```bash
docker run -d -p 8000:8000 --name teamflow-api teamflow-workspace
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Welcome message |
| GET | /api/projects | List all projects |
| GET | /api/projects/{project_id} | Get project details |
| GET | /api/members | List team members |
| GET | /api/reports | View project reports |

## API Documentation

After starting the application, open:

http://localhost:8000/docs

## Stop Docker Container

Stop the running container:

```bash
docker stop teamflow-api
```
