import uvicorn
from fastapi import FastAPI
from recommend import recommend_router

app = FastAPI(title = "추천 시스템")
app.include_router(recommend_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)