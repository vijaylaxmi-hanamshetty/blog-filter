from fastapi import FastAPI
from routes import router as post_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the blog API!"}

app.include_router(post_router)

# If running directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
