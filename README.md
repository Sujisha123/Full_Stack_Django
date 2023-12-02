# Expense Tracker Django Project



> A Django web application for tracking expenses and income.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Description

The Expense Tracker Django Project is a web application built with Django, designed to help users manage their financial activities effectively. It enables users to record both expenses and income, categorize transactions, and maintain an organized overview of their financial history.

## Features

- User authentication and authorization
- Record both expenses and income transactions
- Categorize transactions for better organization
- View transaction history and summaries
- Responsive design for a seamless user experience on various devices

## Technologies Used

- Django
- HTML/CSS
- JavaScript (optional, for enhanced interactivity)
- Bootstrap (optional, for styling)

## Installation

1. **Clone the repository:**

   ```bash
    https://github.com/Sujisha123/Full_Stack_Django/

2. **Change into the project directory:**

   ```bash
   cd Full_Stack_Django

3. **Create a virtual environment:**

   ```bash
   py -3 -m venv .venv

4. **Activate the virtual environment:**
   
   ```bash
   .venv/scripts/activate

5. **Apply database migrations:**

   ```bash
   python manage.py makemigrations

6.   
   ```bash
   python manage.py migrate

7. **Create a superuser account:**

   ```bash
   python manage.py createsuperuser

8. **Start the development server:**

   ```bash
   python manage.py runserver


## Usage
1. Visit http://localhost:8000/admin and log in with the superuser account created.
2. Create categories for transactions (expenses and income).
3. Navigate to http://localhost:8000 to access the Expense Tracker application.
4. Log in with your superuser account or register a new account.
5. Start adding and managing your expenses and income transactions.



