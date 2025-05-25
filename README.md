# Delivery Distance Calculator

A web-based prototype application that calculates the distance between two addresses (in kilometers, miles, or both), stores the queries, and displays historical search data.

---

## 🌐 Live URLs

* **Frontend (Vercel)**: [https://address-mapping.vercel.app](https://address-mapping.vercel.app)
* **Backend API (Render)**: [https://address-mapping.onrender.com/docs](https://address-mapping.onrender.com/docs)
* **PostgreSQL Database (Render Dashboard)**: [https://dashboard.render.com/d/dpg-d0paroemcj7s73duehig-a/info](https://dashboard.render.com/d/dpg-d0paroemcj7s73duehig-a/info)
* **GitHub Repository**: [https://github.com/dj800879/Address-Mapping/tree/main](https://github.com/dj800879/Address-Mapping/tree/main)

---

## 📦 Technologies Used

| Layer    | Tech            | Description                            |
| -------- | --------------- | -------------------------------------- |
| Frontend | SvelteKit       | Lightweight, modern frontend framework |
| Backend  | FastAPI         | High-performance Python API            |
| Database | PostgreSQL      | Cloud-hosted DB on Render              |
| Hosting  | Vercel / Render | Free-tier friendly deployment          |

---

## 💻 How to Run Locally

### ✅ Backend Setup (FastAPI)

1. Clone the repo and navigate to `backend/`
2. Create a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend:

   ```bash
   uvicorn app.main:app --reload
   ```

   * Access Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

### ✅ Frontend Setup (SvelteKit)

1. Navigate to `frontend/`
2. Install dependencies:

   ```bash
   npm install
   ```
3. Run the frontend dev server:

   ```bash
   npm run dev
   ```

   * Access the app at [http://localhost:5173](http://localhost:5173)

---

## 🔐 Environment Variables

In your backend root (`backend/`), create a `.env` file:

```env
DATABASE_URL=your_postgres_or_sqlite_connection_string
```

Render will also require this in the **Environment Settings**.

---

## 🧪 Test Data Examples

Use these sample addresses to test the calculator:

| Source Address                               | Destination Address                      |
| -------------------------------------------- | ---------------------------------------- |
| 415 Mission St Suite 4800, San Francisco, CA | 3223 Hanover St Suite 110, Palo Alto, CA |
| 1600 Amphitheatre Pkwy, Mountain View, CA    | 1 Infinite Loop, Cupertino, CA           |

* Units: Miles, Kilometers, or Both
* The result should be returned and stored in history.

---

## 🔐 Test Data + Expected Output

### ✅ Valid Request

```json
{
  "source": "Chicago, IL",
  "destination": "Bloomington, IL"
}
```

**Expected Output:**

```json
{
  "kilometers": 211.76,
  "miles": 131.56
}
```

### ❌ Invalid Input (Empty Fields)

```json
{
  "source": "",
  "destination": ""
}
```

**Expected Output:** `422 Unprocessable Entity`

### ❌ Injection Attempt

```json
{
  "source": "Chicago'; DROP TABLE users;--",
  "destination": "New York"
}
```

**Expected:** `400 Bad Request`, input sanitized, no crash

### 🔁 Retry Test

```json
{
  "source": "ZZZZZZZZZ",
  "destination": "New York"
}
```

**Expected:**

* 400 error: "No geocoding result for address"
* Retries logged

### 🚫 Rate Limit Test

> Send more than 5 requests within one minute from the same IP.

**Expected:** `429 Too Many Requests`

---

## 🗃 Features

* ✅ Distance calculation using coordinates
* ✅ Unit selection: km, miles, or both
* ✅ Stores queries to a database
* ✅ View/delete historical entries (🗑️ Delete feature added)
* ✅ Deployed on cloud (Vercel + Render)
* ✅ Rate-limited API with input sanitization

---

## 📌 Folder Structure

```
project-root/
├── backend/       # FastAPI backend
├── frontend/      # SvelteKit frontend
```

---

## AI-Powered Address Correction (Future Scope)

We plan to add:

* Google Maps Autocomplete API integration
* Optional ML-based correction with confidence scoring

---