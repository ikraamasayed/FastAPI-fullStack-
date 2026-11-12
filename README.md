# Product Inventory Management API

A beginner-level backend development project built using **FastAPI, SQLAlchemy, Pydantic, and MySQL**.

The project demonstrates how to build a REST API that manages product records through standard CRUD operations, with MySQL as the persistent data store.

> **Project status:** Learning project / prototype. CRUD functionality is implemented, while authentication, error handling, automated testing, and frontend integration require further development.

## Technologies Used

- **Python** – Core programming language
- **FastAPI** – REST API development
- **Pydantic** – Request validation and data schemas
- **SQLAlchemy** – Object-relational mapping (ORM)
- **MySQL** – Relational database
- **MySQL Connector/Python** – Database connectivity
- **Uvicorn** – ASGI development server

## Features

- Create new product records.
- Retrieve all available products.
- Retrieve an individual product by ID.
- Update existing product information.
- Partially update selected product fields.
- Delete product records.
- Automatically create the product table if it does not exist.
- Insert sample products when the database is empty.
- Configure CORS for a local frontend origin.

## API Endpoints

| Method | Endpoint | Operation |
|---|---|---|
| GET | `/products/` | Retrieve all products |
| GET | `/products/{id}` | Retrieve a product |
| POST | `/products/` | Create a product |
| PUT | `/products/{id}` | Update a product |
| PATCH | `/products/{id}` | Partially update a product |
| DELETE | `/products/{id}` | Delete a product |
| GET | `/users/me` | Demonstration of bearer-token user dependency |

## What Can Users Do?

Clients can interact with the API using HTTP requests to manage product information, including product names, descriptions, prices, and quantities.

FastAPI also provides an interactive API documentation interface through Swagger UI, allowing developers to explore and test available endpoints.

## How I Built It

The project was developed incrementally while learning backend development concepts:

1. Created a Python virtual environment and installed the required dependencies.
2. Set up the FastAPI application and defined API routes.
3. Created SQLAlchemy database models for product records.
4. Configured a MySQL database connection and session management.
5. Created Pydantic models for request validation.
6. Implemented database initialization and sample data insertion.
7. Developed GET, POST, PUT, PATCH, and DELETE endpoints.
8. Added CORS middleware for local frontend communication.
9. Explored FastAPI's OAuth2 bearer-token dependency mechanism.

## Concepts I Explored

- REST API architecture and HTTP methods.
- Path parameters and request bodies.
- Pydantic validation and serialization.
- SQLAlchemy ORM and database sessions.
- Dependency injection using FastAPI's `Depends()`.
- MySQL connectivity and relational database operations.
- CORS configuration.
- Basic exploration of OAuth2 bearer-token dependencies.

## Keyboard Shortcuts

This is a backend API project rather than a standalone desktop application. It does not implement custom keyboard shortcuts.

Developers can use Swagger UI to interact with the API through a browser.

## How to Run Locally

### Prerequisites

- Python 3.10+
- MySQL Server
- Git

### 1. Clone the repository

```bash
git clone https://github.com/ikraamasayed/FastAPI-fullStack-.git
cd FastAPI-fullStack-
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Configure MySQL

Create a database:

```sql
CREATE DATABASE telusko;
```

Configure the database connection in `db/database.py` with your local MySQL credentials.

**Security note:** Move credentials into environment variables before sharing or deploying the project. Do not commit real credentials.

### 5. Start the application

```bash
uvicorn main:app --reload
```

### 6. Explore the API

Open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Potential Improvements

- Implement proper JWT-based authentication and authorization.
- Introduce environment-based configuration using `pydantic-settings`.
- Improve HTTP status codes and exception handling.
- Add database constraints and duplicate-record handling.
- Introduce Alembic for database migrations.
- Add automated tests using Pytest and FastAPI's TestClient.
- Improve project structure by separating routes, schemas, services, and database configuration.
- Verify and integrate a functional frontend.
- Add Docker support and deployment configuration.

## Project Status

This project represents my initial practical exploration of backend development with FastAPI and relational databases.

It is a foundation for further learning and improvement, rather than a finished production application.

**Author:** [Ikraama Sayed](https://github.com/ikraamasayed)
