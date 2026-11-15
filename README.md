# Expense Tracking System

A full-stack personal finance and expense management application built with a **Streamlit** interactive frontend, a **FastAPI** REST backend, and a **MySQL** relational database. Users can log daily expenses, update existing records, and visualize spending patterns by category and month.

---

## Key Features

- **Add & Update Daily Expenses**: Select any date to view, add, or update up to 5 expense entries at a time with amount, category (`Rent`, `Food`, `Shopping`, `Entertainment`, `Other`), and custom notes.
- **Analytics by Category**: Filter expenses across a custom date range (`start_date` to `end_date`) to view total spend, percentage breakdown, and an interactive bar chart sorted by highest spending category.
- **Analytics by Month**: Automatically aggregate historical expenses by month with visual bar charts and summary tables to track monthly spending trends.
- **RESTful API Backend**: Decoupled FastAPI service with Pydantic schema validation and automatic OpenAPI/Swagger documentation.
- **Structured Logging & Testing**: Custom file-based logging for database operations and unit testing configured with `pytest`.

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | Streamlit, Pandas, Requests |
| **Backend** | FastAPI, Uvicorn, Pydantic |
| **Database** | MySQL (`mysql-connector-python`) |
| **Testing & Logging** | Pytest, Python `logging` |

---

## Project Structure

```text
Expense Tracking System/
├── backend/
│   ├── server.py               # FastAPI application and REST API endpoints
│   ├── db_helper.py            # MySQL connection context manager and CRUD queries
│   ├── logging_setup.py        # Custom file logger configuration
│   └── expense_tracking_system.log
├── frontend/
│   ├── app.py                  # Main Streamlit entry point with tab navigation
│   ├── add_update_ui.py        # UI tab for logging and editing daily expenses
│   ├── analytics_ui.py         # UI tab for date-range category breakdown
│   └── analytics_by_month_ui.py# UI tab for monthly aggregation charts
├── tests/
│   ├── conftest.py             # Pytest path configuration
│   └── backend/
│       └── test_db_helper.py   # Unit tests for database helper functions
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## API Endpoints

| Method | Endpoint | Description | Request Body / Params |
| :--- | :--- | :--- | :--- |
| `GET` | `/expenses/{expense_date}` | Fetch all recorded expenses for a specific date (`YYYY-MM-DD`). | Path param: `expense_date` |
| `POST` | `/expenses/{expense_date}` | Replace/update expenses for a specific date. | JSON array of `{amount, category, notes}` |
| `POST` | `/analytics/` | Get total spend and percentage breakdown by category for a date range. | JSON: `{start_date, end_date}` |
| `GET` | `/analytics_by_month` | Get aggregated total expenses grouped by month. | None |

---

## Getting Started

### 1. Prerequisites

- **Python 3.10+**
- **MySQL Server** running locally

### 2. Database Setup

Create the `expense_manager` database and `expenses` table in your local MySQL instance:

```sql
CREATE DATABASE IF NOT EXISTS expense_manager;
USE expense_manager;

CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    amount FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL,
    notes TEXT
);
```

> **Note:** Update the database connection credentials (`host`, `user`, `password`, `database`) in `backend/db_helper.py` if your local MySQL setup differs from the default (`localhost` / `root`).

### 3. Installation & Virtual Environment Setup

Clone the repository, create and activate a virtual environment, and install the required packages:

```bash
git clone <your-repo-url>
cd "Expense Tracking System"

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS / Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Running the Application

Start the **FastAPI backend server** first (from the `backend/` directory):

```bash
cd backend
uvicorn server:app --reload
```

- Backend API will run at: http://localhost:8000
- Interactive Swagger API Docs: http://localhost:8000/docs

In a separate terminal, launch the **Streamlit frontend** (from the `frontend/` directory):

```bash
cd frontend
streamlit run app.py
```

- Streamlit UI will open in your browser at: http://localhost:8501

---

## Running Tests

Execute the test suite from the project root directory using `pytest`:

```bash
pytest
```
