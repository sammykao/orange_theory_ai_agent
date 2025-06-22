from fastapi import FastAPI
from api import sms
import uvicorn # Import uvicorn

app = FastAPI()

app.include_router(sms.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Server is running"}

# Encoding fix 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080) 