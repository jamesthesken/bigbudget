class Category:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def add_amount(self, amount):
        self.amount += amount

    def display_info(self):
        return f"{self.name}: {self.amount}"

class BudgetCategory(Category):
    def get_balance(self):
        return self.amount

class IncomeCategory(Category):
    pass

class TotalBudget:
    def __init__(self):
        self.expense_categories = {}
        self.income_categories = {}

    def add_expense_category(self, name, budgeted_amount):
        self.expense_categories[name] = BudgetCategory(name, budgeted_amount)

    def add_income_category(self, name, amount=0):
        self.income_categories[name] = IncomeCategory(name, amount)

    def add_expense(self, category, amount):
        if category in self.expense_categories:
            self.expense_categories[category].add_amount(-amount)
        else:
            print(f"Expense Category '{category}' not found.")

    def add_income(self, category, amount):
        if category in self.income_categories:
            self.income_categories[category].add_amount(amount)
        else:
            print(f"Income Category '{category}' not found.")

    def get_total_balance(self):
        total_income = sum(cat.amount for cat in self.income_categories.values())
        total_expenses = sum(cat.amount for cat in self.expense_categories.values())
        return total_income + total_expenses

    def display_category_info(self):
        print("Expenses:")
        for category in self.expense_categories.values():
            print(category.display_info())

        print("Income:")
        for category in self.income_categories.values():
            print(category.display_info())

# Example Usage
my_budget = TotalBudget()
my_budget.add_expense_category("Groceries", 300)
my_budget.add_expense_category("Utilities", 100)
my_budget.add_income_category("Salary")
my_budget.add_income_category("Freelance")

my_budget.add_expense("Groceries", 50)
my_budget.add_expense("Utilities", 75)
my_budget.add_income("Salary", 2000)
my_budget.add_income("Freelance", 500)

print(f"Total Budget Balance: {my_budget.get_total_balance()}")
my_budget.display_category_info()
