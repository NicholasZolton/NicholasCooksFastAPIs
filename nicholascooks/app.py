from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from nicholascooks.routers import example_router, user_info_router
from nicholascooks.routers import example_router
from nicholascooks.utils.logger import log
import os


load_dotenv(override=True)
app = None
if os.getenv("LOCALLY_TESTING") == "1":
    log.info("Running locally...")
    app = FastAPI(title="NicholasCooksAPIs", docs_url="/docs")

    origins = [
        "http://127.0.0.1:8000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def root(request: Request):
        return {"message": f"{request.base_url}/docs"}
elif os.getenv("DEV_ENV") == "1":
    log.info("Running in development environment...")
    app = FastAPI(title="NicholasCooksAPIs")
else:
    log.info("Running in production environment...")
    app = FastAPI(title="NicholasCooksAPIs", docs_url=None, redoc_url=None)

app.include_router(user_info_router.router)
app.include_router(example_router.router)
