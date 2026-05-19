from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth_router,profile_router,search_router,analysis_router,buy_router
from app.db.base import Base
from app.db.session import engine
from app.routers import saved_rouer
from app.models import user


#  Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

#  ADD CORS HERE (RIGHT AFTER app = FastAPI())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development (allow frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router.router)
app.include_router(profile_router.router)
app.include_router(search_router.router)
app.include_router(analysis_router.router)
app.include_router(buy_router.router)
app.include_router(saved_rouer.router)

@app.get("/")
def root():
    return {"message": "API is Running Successfully"}

# This serves all your HTML, JS, and images directly from the frontend folder
app.mount("/", StaticFiles(directory="../Frontend/login", html=True), name="frontend")
# run command # uvicorn app.main:app --reload    
