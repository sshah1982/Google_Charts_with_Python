from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routes.readers.CsvDataReader import CsvDataReader

chart_renderer = APIRouter()

@chart_renderer.get("/chart_data/{chart_type}")
async def chart_data(chart_type: str):
    
    _chart = CsvDataReader(chart_type)
    
    res = JSONResponse(content=jsonable_encoder(_chart._chart_data))
    
    return res

