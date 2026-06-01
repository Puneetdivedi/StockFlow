# StockFlow – Inventory & Order Management System

## 📖 Project Overview
StockFlow is a **full‑stack, production‑ready** inventory and order management system built with:
- **Backend:** FastAPI, SQLAlchemy, PostgreSQL, Alembic, Pydantic
- **Frontend:** React (JavaScript), React Router, Context API, Axios
- **Containerization:** Docker & Docker‑Compose
- **Deployments:** Render (backend) and Vercel (frontend)

It provides CRUD operations for **products**, **customers**, and **orders**, enforces key business rules (unique SKU/email, inventory checks, automatic total calculation), and offers a lightweight dashboard with key metrics.

---

## 🏗️ Architecture Diagram (ASCII)
```
+-------------------+      +---------------------+      +-------------------+
|   Frontend (React) | <-- |   Backend (FastAPI) | <-- | PostgreSQL DB      |
|  http://localhost |      |  http://localhost:8 |      |  pg://postgres:16 |
+-------------------+      +---------------------+      +-------------------+
        |   ^                         |   ^
        |   |                         |   |
        v   |                         v   |
   API calls (Axios)            SQLAlchemy ORM
```

---

## ⚙️ Setup & Development
### Prerequisites
- Docker Desktop (or Docker Engine)
- Node 20 (for local React dev)
- Python 3.11

### Local Development
```bash
# Clone the repo (already done)
cd StockFlow

# Backend – create virtualenv and install deps
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r backend/requirements.txt

# Frontend – install deps
cd frontend
npm install
```

### Run with Docker‑Compose (recommended)
```bash
docker compose up --build
```
- Backend: <http://localhost:8000>
- API docs: <http://localhost:8000/docs>
- Frontend: <http://localhost:3000>

---

## 📦 Docker
- `backend/Dockerfile` – Python 3.11‑slim, installs deps, runs `uvicorn app.main:app`.
- `frontend/Dockerfile` – Node 20‑alpine, builds the React app and serves with `serve`.
- `docker-compose.yml` – orchestrates `frontend`, `backend`, and `postgres` services.
- `.dockerignore` – excludes node_modules, dist, .env, __pycache__.

---

## 📚 API Documentation
FastAPI automatically generates OpenAPI docs at **/docs**. Key endpoints:
- **/products/** – create, read, update, delete products
- **/customers/** – CRUD for customers
- **/orders/** – place orders (inventory validation, total amount calc)
- **/dashboard/** – aggregated metrics (total products/customers/orders, low‑stock list)
- **/health** – health‑check endpoint used by Render.

---

## 🚀 Deployment Guides
### Backend – Render
- Use `render.yaml` (included) – Docker build, start command `uvicorn app.main:app --host 0.0.0.0 --port 8000`.
- Set environment variables (`DATABASE_URL`, `SECRET_KEY`).
- Health‑check: `/health`.

### Frontend – Vercel
- Deploy the `frontend` directory.
- `vercel.json` configures the build output (`frontend/build`).
- Connect Vercel to the same backend URL (set `REACT_APP_API_URL` in Vercel Environment Variables).

---

## 📸 Screenshots (placeholders)
![Dashboard screenshot](./frontend/public/dashboard.png)
![Products page screenshot](./frontend/public/products.png)
![Customers page screenshot](./frontend/public/customers.png)
![Orders page screenshot](./frontend/public/orders.png)

---

## 🔮 Future Improvements
- Role‑based access control (admin vs. regular staff).
- Email notifications on low‑stock or order confirmation.
- Pagination & search filters for large data sets.
- Unit & integration test suite with pytest & React Testing Library.
- CI/CD pipelines (GitHub Actions) for automated builds & deployments.

---


