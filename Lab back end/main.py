from fastapi import FastAPI
from router.emprestimo_router import router as emprestimo_router

app = FastAPI()

app.include_router(emprestimo_router)