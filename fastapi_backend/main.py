import api
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title='Test',
    version='1.0.0',
)
instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
async def _on_startup():
    instrumentator.expose(app)


app.include_router(api.router, prefix="/api/v1")