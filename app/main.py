from app.core.database import engine, Base
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.router import router
import uvicorn
import time
import logging

# ========================
# CONFIG LOGGING
# ========================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ========================
# APP INIT
# ========================
app = FastAPI(
    title="API prediction prix immobilier",
    version="1.0.0"
)

# ========================
# ROUTES
# ========================
app.include_router(router)

# ========================
# DATABASE INIT
# ========================
Base.metadata.create_all(bind=engine)

# ========================
# MIDDLEWARE LOGGING
# ========================
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    try:
        response = await call_next(request)

        duration = time.time() - start_time

        logger.info(
            f"{request.method} {request.url} - "
            f"Status: {response.status_code} - "
            f"Time: {duration:.3f}s"
        )

        return response

    except Exception as e:
        logger.error(f"Erreur middleware: {str(e)}")
        raise e

# ========================
# GLOBAL ERROR HANDLER
# ========================
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Erreur globale: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "message": "Erreur interne du serveur",
            "detail": str(exc)
        }
    )

# ========================
# RUN SERVER
# ========================
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)