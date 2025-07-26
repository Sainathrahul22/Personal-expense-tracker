# Personal Expense Tracker

A full-stack Django web application for managing and tracking personal expenses with secure authentication, a modern UI, and RESTful API backend.

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [API Endpoints](#api-endpoints)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

## Project Overview

Personal Expense Tracker is a comprehensive expense management system built with Django and Django REST Framework. It enables users to register, log in securely using token-based authentication, and manage their expenses—adding, editing, deleting, and viewing them in a full-screen dashboard. The project adopts best practices in backend development and frontend design for a seamless and responsive user experience.

## Features

- User Registration and Token-Based Authentication  
- Modern, Responsive UI with Full-Screen Dashboard  
- Create, Read, Update, Delete (CRUD) Operations on Expenses  
- Filter and View Expenses by Categories and Date  
- Clean Codebase following MVT architecture  
- RESTful APIs for frontend-backend interaction  

## Tech Stack

- Python 3.x  
- Django 5.x  
- Django REST Framework  
- SQLite (development) / PostgreSQL (recommended for production)  
- HTML5, CSS3 (custom styling)  
- JavaScript (Fetch API for async operations)

## Installation

### Prerequisites

- Python 3.x installed  
- Git installed  
- (Optional) Virtual environment tool (venv, virtualenv)

### Setup Steps

1. **Clone the Repository**

https://github.com/Sainathrahul22/Personal-expense-tracker
cd personal-expense-tracker

2. **Create and Activate Virtual Environment**

python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

3. **Install Dependencies**

pip install -r requirements.txt

4. **Run Migrations**

python manage.py migrate

5. **Create a Superuser (Optional, for Admin Access)**

python manage.py createsuperuser


6. **Run the Development Server**

python manage.py runserver

7. **Open the App in Browser**

Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Visit the landing page (`/`)
- Register as a new user with a unique username, secure password, and email.
- Log in and manage your expenses via the dashboard.
- Add new expenses, edit or delete existing entries.
- Use password reset if you forget your password.
- Admin users can manage users and expenses via Django admin at `/admin/`.

## API Endpoints

All API routes are prefixed with `/api/`:

| Endpoint               | Method | Description                        |
|------------------------|--------|----------------------------------|
| `/api/auth/register/`  | POST   | Register new user                 |
| `/api/auth/login/`     | POST   | Obtain auth token                 |
| `/api/auth/logout/`    | POST   | Logout user                      |
| `/api/expenses/`       | GET    | List logged-in user's expenses    |
| `/api/expenses/`       | POST   | Add a new expense                |
| `/api/expenses/{id}/`  | PUT    | Update expense by ID             |
| `/api/expenses/{id}/`  | DELETE | Delete expense by ID             |

## Contributing

Contributions are welcome!  
Please fork the repository, create your feature branch, and submit a pull request.  
Make sure to follow coding conventions and test your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Created by Your Name – [sainath.rahul2004@gmail.com](mailto:sainath.rahul2004@gmail.com)  
Find me on GitHub: [https://github.com/Sainathrahul22](https://github.com/Sainathrahul22)  


