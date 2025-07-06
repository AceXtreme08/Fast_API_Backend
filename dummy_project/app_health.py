from fastapi import FastAPI
from core.log import get_logger
from core.auth import register_user, authenticate_user, RegisterRequest, LoginRequest, TokenResponse


app = FastAPI()


logger = get_logger()
db_logger = get_logger("Database check",True)


@app.get("/health")
def health_check():
    logger.debug("Health check.")
    db_logger.debug("DB Health check.")
    return {"status": "ok"}


@app.post("/register")
def register(data: RegisterRequest):
    return register_user(data)

@app.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    return authenticate_user(data)