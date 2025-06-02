from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def welcome():
    try:
        return {"message": "Welcome to the FastAPI application!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test")   
async def Bienvenu():
    try:
        return {"message": "Welcome to /test route!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


