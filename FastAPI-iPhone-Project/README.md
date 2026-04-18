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

## 🛠 Tech Stack
- **Framework**: FastAPI
- **Database**: SQLite (Planned migration to PostgreSQL)
- **Container**: Docker (Upcoming)
