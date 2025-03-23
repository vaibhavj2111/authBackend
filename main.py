from fastapi import FastAPI, APIRouter, Depends, HTTPException
from routes.authRoutes import router

app = FastAPI()

app.include_router(router, prefix="/auth")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

