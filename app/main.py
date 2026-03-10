from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time

from app.db.database import engine
from app.db.models import Base

from app.api.auth import router as auth_router
from app.api.chat import router as chat_router
from app.api.manager import router as manager_router
from app.api.leave import router as leave_router

from app.core.logging import logger


app = FastAPI(
    title="Enterprise HR AI Platform",
    version="2.0.0"
)


# -----------------------------
# Create Database Tables
# -----------------------------
Base.metadata.create_all(bind=engine)


# -----------------------------
# CORS Middleware
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Logging Middleware
# -----------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = round((time.time() - start_time) * 1000, 2)

    logger.info(
        f"IP={request.client.host} | "
        f"{request.method} {request.url.path} | "
        f"Status={response.status_code} | "
        f"Duration={duration}ms"
    )

    return response


# -----------------------------
# Global Exception Handler
# -----------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    logger.error(
        f"Unhandled error | Path={request.url.path} | Error={str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )


# -----------------------------
# Register Routers
# -----------------------------
app.include_router(auth_router)
app.include_router(chat_router, prefix="/chat")
app.include_router(manager_router)
app.include_router(leave_router)


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def root():
    return {"status": "Enterprise HR AI Platform running"}