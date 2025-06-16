from .__init__ import create_app
import uvicorn

app = create_app()


@app.get("/root")
def root():
    return {"message": "Root! Hello, World!"}

if __name__ == "__main__":
    uvicorn.run(
        "package.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )