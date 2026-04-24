## 🚀 Progress Log

### Day 1: Foundation
- Bootstrapped FastAPI framework.
- Implemented basic CRUD with in-memory storage.
- Resolved CORS issues for frontend integration.

### Day 2: Persistence & Scalability (Current)
- **Database**: Migrated from dictionaries to **SQLite** for data persistence.
- **Architecture**: Refactored into a modular structure (`main.py`, `models.py`, `database.py`) to enhance maintainability.
- **Data Modeling**: Extended Pydantic models to include `phoneNumber` and `birthDay`.
- **Error Handling**: Implemented custom `HTTPException` for robust API responses.

### Day 3 - 4: Infrastructure Modernization & Frontend (Current)
- **PostgreSQL Migration**: Upgraded from SQLite to an enterprise-grade **PostgreSQL** database via SQLAlchemy ORM.
- **Containerization**: Implemented **Docker Compose** to orchestrate independent containers for the FastAPI app and PostgreSQL.
- **Frontend Integration**: Established a dynamic connection between the HTML/JS frontend and backend using the **Fetch API**.
- **Robust Engineering**: Implemented **Database Rollbacks** and guard clauses to ensure system stability and data integrity during failures.

## 🛠 Tech Stack
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL (Containerized)
- **Container**: Docker / Docker Compose
- **Frontend**: JavaScript (ES6+), HTML5
