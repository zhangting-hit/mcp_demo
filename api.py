# api.py
from fastapi import FastAPI
from helper import get_kpi_summary, get_kpi_trend
import uvicorn
from constant import API_HOST, API_PORT

app = FastAPI(title="KPI Dashboard API", version="1.0")

@app.get("/kpi/summary")
def kpi_summary():
    return get_kpi_summary()

@app.get("/kpi/trend/{kpi_name}")
def kpi_trend(kpi_name: str):
    return get_kpi_trend(kpi_name)

if __name__ == "__main__":
    uvicorn.run("api:app", host=API_HOST, port=API_PORT, reload=True)