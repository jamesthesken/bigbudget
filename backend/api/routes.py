from fastapi import APIRouter
from services import budget_service

router = APIRouter()

@router.post("/expenses/")
async def add_expense(category_name: str, amount: float):
    return budget_service.add_expense(category_name, amount)

# Add more routes as needed
