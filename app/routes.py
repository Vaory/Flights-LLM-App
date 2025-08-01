from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from services.flight_api import get_flight_data
from services.llm_service import ask_llm

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/")

def create_app() -> FastAPI:
    @router.post("/ask", response_class=HTMLResponse)
    async def ask_question(
        request: Request,
    ):
        # Получаем данные рейсов
        flight_data = await get_flight_data(request.airport)
    
        # Запрашиваем LLM
        answer = await ask_llm(request.question, flight_data)
    
        return answer
