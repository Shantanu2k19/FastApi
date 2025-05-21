# FastAPI Mastery Roadmap
---

## ✅ Phase 1: FastAPI Fundamentals

### 🚀 Getting Started
- Setting up FastAPI with `uvicorn`
    - ASGI server that runs FastAPI (or other ASGI-compatible) applications.
    - receives http request, process them asynchronously, calls fastapi app, returns response 
- Understanding ASGI vs WSGI 
        
    | Feature            | **WSGI** (Web Server Gateway Interface)                  | **ASGI** (Asynchronous Server Gateway Interface)     |
    | ------------------ | -------------------------------------------------------- | ---------------------------------------------------- |
    | Introduced For     | Synchronous Python web apps                              | Asynchronous **and** synchronous Python web apps     |
    | Core Limitation    | No support for async IO (e.g., WebSockets, long polling) | Built for async-first apps                           |
    | Example Frameworks | Django, Flask, Pyramid                                   | **FastAPI**, Starlette, Django 3.0+ (with `asgiref`) |
    | Concurrency        | Limited to threading/processes                           | Supports **async/await**, event loops                |
    | Real-Time Support  | ❌ No native support for WebSockets                       | ✅ WebSockets, HTTP2, Server-Sent Events              |
    | Performance        | Good                                                     | **Better** under async I/O workloads                 |
    | Servers            | Gunicorn (sync)                                          | **Uvicorn**, Daphne, Hypercorn (async)               |

### 🧩 Routing
- Path parameters - passed inside url, Automatically type-validated by FastAPI using pydantic 
- Query parameters - Parameters passed after the ? in the URL, ex-/search/?name=shan&age=25
- Request bodies - Data sent as JSON payload in the body of request. Used to send structured data.
- Route grouping with `APIRouter`

### 🛡️ Pydantic
- `BaseModel` for validation
- Type coercion and default values
- Field-level validation and metadata

### 📄 Auto-Documentation
- Swagger UI (`/docs`)
- ReDoc (`/redoc`)
- Adding descriptions, examples, metadata

### 🚨 Error Handling
- `HTTPException`
- Custom error handlers
- Validation error handling (`RequestValidationError`)

### 🔌 Dependency Injection
- Using `Depends()`
- Common use: DB sessions, authorization, shared logic

### ⚙️ Config Management
- Environment variables using `BaseSettings`
- Using `.env` files and `python-dotenv`

---

## ⚙️ Phase 2: Intermediate to Advanced FastAPI

### 🔐 Authentication & Authorization
- OAuth2 with Password flow
- JWT-based auth
- Scopes and roles
- Optional: FastAPI Users

### 🗃️ Database Integration
- SQLAlchemy (sync & async)
- Alembic for migrations
- Tortoise ORM / GINO (for async DB)

### 🕸️ Async/Await in FastAPI
- Declaring `async def` routes
- Working with async DB and HTTP clients

### ⏳ Background Tasks
- Using `BackgroundTasks`
- Long-running jobs or notifications

### 🧱 Middleware
- CORS
- Custom middleware (e.g., logging)

### 🧪 Testing
- `TestClient` from Starlette
- Using `pytest`
- Dependency overrides for testing

### 📡 WebSockets
- Real-time features (chat, notifications)
- WebSocket endpoints

### 🗂️ File Handling
- File uploads and downloads
- Serving static files

---

## 🤖 Phase 3: AI/ML with FastAPI

### 🧠 ML Model Serving
- Loading ML models (`joblib`, `pickle`, `onnxruntime`)
- Creating prediction endpoints with Pydantic

### 📡 Streaming & Performance
- Stream responses for large outputs
- Async file processing

### ⏱️ Background Task Queues
- Using Celery / RQ + Redis
- Queueing long-running ML jobs

### 🔐 API Security for ML
- Token-based auth
- Rate limiting
- Abuse prevention

### 📦 Model Versioning
- Multiple model versions as endpoints
- Model lifecycle in CI/CD pipelines

---

## 💼 Interview-Focused Topics

- Designing RESTful APIs with FastAPI(with validation, pagination, filters)
- OAuth2/JWT explanation
- FastAPI vs Django/DRF
- Pydantic model validation edge cases
- Writing unit/integration tests

---

## 🧪 Project Ideas (AI + FastAPI)

| Project Idea | Description | ML Integration |
|--------------|-------------|----------------|
| 🧠 ML Prediction API | Serve a tabular model (e.g., house price) | Scikit-learn, Pydantic |
| 📸 Image Classifier | Upload image, return predicted label | TensorFlow/PyTorch CNN |
| 🎙️ Speech-to-Text API | Upload audio, return transcript | OpenAI Whisper |
| 🩺 Disease Diagnosis | Input symptoms, return diagnosis | Tabular ML/CNN |
| 📊 AutoML Dashboard | Upload CSV, train model, show metrics | AutoSklearn, Streamlit |
| 🤖 AI Chatbot API | Q&A or conversational LLM | OpenAI/LangChain |
| 🎞️ Video Processing | Upload video, return frame-based results | CV model + FFmpeg |

---

## 📚 Bonus Tools & Practices

- 🐳 Docker: Containerize FastAPI apps
- 🔀 NGINX / Traefik: Reverse proxies
- 🛠️ Gunicorn + Uvicorn workers
- ⚙️ GitHub Actions: CI/CD pipelines
- ☁️ Deploy on: Render, Vercel, Railway, or Kubernetes (advanced)

---

## ✅ Final Tips

- Build multiple small projects before scaling
- Explore both sync and async approaches
- Focus on testing and documentation
- Compare concepts to Django for clarity
- Use FastAPI docs + community-driven tutorials

---