from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from itertools import chain
from .forms import *
from .models import *

def LogIn(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['user_password']

        user = authenticate(username = username, password = password)

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

        else:

            messages.error(request, "No user found with the given credentials")
            return redirect('/')

    return render(request, 'login.html')


def Signup(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email_address']
        create_password = request.POST['create_password']
        confirm_password = request.POST['confirm_password']

        if create_password == confirm_password:

            new_user = User(username = username, email = email)

            new_user.set_password(create_password)

            new_user.save()

            messages.success(request, "Your account is created.")

            return redirect('/')
        
        else:

            messages.error(request, "Password didn't match.")

    return render(request, 'signup.html')

def Logout(request):

    logout(request)

    messages.success(request, "Logged Out Successfully")

    return redirect('/')


def Dashboard(request):
     
      total_income = Income.objects.all().aggregate(models.Sum('amount'))['amount__sum'] or 0

      total_expense = Expense.objects.all().aggregate(models.Sum('amount'))['amount__sum'] or 0

      total_balance = total_income - total_expense
      
      recent_incomes = Income.objects.order_by('-date')[:3]

      recent_expenses = Expense.objects.order_by('-date')[:3        ]

      combined_history = sorted(
          
        chain(recent_incomes, recent_expenses),

        key=lambda record: record.date,

        reverse=True
    )
      return render(request,'dashboard.html', {'username':request.user,'combined_history': combined_history, 'total_income': total_income,  'total_expense': total_expense,'total_balance': total_balance,})

def Incomes(request):

    all_incomes = Income.objects.all()

    total_income = all_incomes.aggregate(total=models.Sum('amount'))['total']
    
    return render(request, 'incomes.html', {'income_data': all_incomes, 'total_income': total_income})


def IncomeAdd(request):

    if request.method == 'POST':

        income_form = IncomeForm(request.POST)

        if income_form.is_valid():

            income_form.save()

            return redirect('/incomes/')

    return render(request, 'add_income.html', {'income_form': IncomeForm})

def IncomeUpdate(request, id):

    income = Income.objects.get(id = id)

    if request.method == 'POST':

        income_form = IncomeForm(request.POST, instance=income)

        if income_form.is_valid():

            income_form.save()

            return redirect('/incomes/')


    income_form = IncomeForm(instance=income)

    return render(request, 'add_income.html', {'income_form': income_form})

def IncomeDelete(request, id):

    income = Income.objects.get(id = id)

    income.delete()

    return redirect('/incomes/')


def Expenses(request):

    all_expenses = Expense.objects.all()

    total_expense = all_expenses.aggregate(total=models.Sum('amount'))['total']

    return render(request, 'expenses.html', {'expense_data': all_expenses, 'total_expense': total_expense})


def ExpenseAdd(request):

    if request.method == 'POST':

        expense_form = ExpenseForm(request.POST)

        if expense_form.is_valid():

            expense_form.save()

            return redirect('/expenses/')

    return render(request, 'add_expense.html', {'expense_form': ExpenseForm})

def ExpenseUpdate(request, id):

    expense = Expense.objects.get(id = id)

    if request.method == 'POST':

        expense_form = ExpenseForm(request.POST, instance=expense)

        if expense_form.is_valid():

            expense_form.save()

            return redirect('/expenses/')


    expense_form = ExpenseForm(instance=expense)

    return render(request, 'add_expense.html', {'expense_form': expense_form})

def ExpenseDelete(request, id):

    expense = Expense.objects.get(id = id)

    expense.delete()

    return redirect('/expenses/')



