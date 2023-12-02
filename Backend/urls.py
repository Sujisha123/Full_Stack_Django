from django.urls import path
from .views import *

urlpatterns = [

    path('', LogIn),
    path('signup/', Signup),
    path('logout/', Logout),

    path('dashboard/', Dashboard),

    path('incomes/', Incomes),
    path('income/add/', IncomeAdd),
    path('income/update/<int:id>/', IncomeUpdate, name='income_update'),
    path('income/delete/<int:id>/', IncomeDelete, name='income_delete'),

    path('expenses/', Expenses),
    path('expense/add/', ExpenseAdd),
    path('expense/update/<int:id>/', ExpenseUpdate, name='expense_update'),
    path('expense/delete/<int:id>/', ExpenseDelete, name='expense_delete'),

]