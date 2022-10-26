from fastapi import FastAPI
from routes import eval_router
import uvicorn

app = FastAPI()
app.include_router(eval_router, prefix="/api/v1")


@app.get("/")
@app.get("/index")
async def root():
    return "Hello, world!"


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)