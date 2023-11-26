from db.database import get_db
from db.models import Expense

def add_expense(category_name, amount):
    db = next(get_db())
    new_expense = Expense(category_name=category_name, amount=amount)
    db.add(new_expense)
    db.commit()
    return new_expense

