from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="TeamFlow Workspace API",
    description="API for managing projects, team members and reports",
    version="1.0.0"
)

projects = [
    {"id": 1, "name": "Website Redesign", "status": "In Progress"},
    {"id": 2, "name": "Mobile Application", "status": "Planning"}
]

members = [
    {"id": 1, "name": "Ali", "role": "Project Manager"},
    {"id": 2, "name": "Developer", "role": "Software Engineer"}
]

@app.get("/")
def home():
    return {"message": "Welcome to TeamFlow Workspace API"}

@app.get("/api/projects")
def get_projects():
    return {"projects": projects}

@app.get("/api/projects/{project_id}")
def get_project(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            return project
    raise HTTPException(status_code=404, detail="Project not found")

@app.get("/api/members")
def get_members():
    return {"members": members}

@app.get("/api/reports")
def get_reports():
    return {
        "total_projects": len(projects),
        "total_members": len(members),
        "in_progress": sum(
            1 for project in projects
            if project["status"] == "In Progress"
        )
    }
