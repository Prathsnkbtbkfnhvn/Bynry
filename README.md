# Gas-Utility-Project
This Django application provides consumer services for gas utilities, allowing customers to submit service requests online, track the status of their requests, and view their account information. It also includes a customer support tool for managing requests.
# Gas Utility Django Application

This Django application provides consumer services for gas utilities. It allows customers to submit service requests online, track the status of their requests, and view their account information. Additionally, it provides customer support representatives with a tool to manage requests and provide support to customers.

## Features

- **Service Requests:** Customers can submit service requests online, including selecting the type of service request, providing details, and attaching files.
- **Request Tracking:** Customers can track the status of their service requests, including submission and resolution timestamps.
- **Account Information:** Customers can view their account information.
- **Customer Support Tool:** Customer support representatives can manage service requests and provide support to customers.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vishalbagal/gas-utility-django.git
2.Navigate to the project directory:
  cd gas-utility-django
3.Create a virtual environment (optional but recommended):
  python -m venv venv
4.Activate the virtual environment:
  venv\Scripts\activate
5.Install dependencies:
  pip install -r requirements.txt
6.Apply migrations:
  python manage.py migrate
7. Run the development server:
  python manage.py runserver
8. Access the application at http://localhost:8000.
