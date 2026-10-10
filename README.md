# Lost and Found Management System

## Overview

The **Lost and Found Management System** is a web-based application built using Flask and MySQL to help users report, search, and manage lost and found items.

Users can create an account, securely log in, report lost or found items, view available items, search and filter listings, and manage their profile. The system also provides a dashboard with basic statistics about the reported items.

## Features

### User Management

* User registration with email, name, roll number, course, branch, and batch details.
* Secure password-based registration and login.
* Passwords are hashed using **Flask-Bcrypt**.
* Login sessions are managed using **Flask-Login**.
* Secure logout functionality.
* Profile viewing and profile information updates.

### Lost & Found Item Management

* Report a lost or found item.
* Add item name, category, location, description, and other details.
* View reported lost and found items.
* Search items by name or description.
* Filter items by category.
* View detailed information about individual items.
* Edit and manage reported items.

### Dashboard

The dashboard provides a simple overview of the system with:

* Total number of reported items.
* Number of lost items.
* Number of found items.
* Quick navigation to view items.
* Quick access to report an item.
* Logout option.

## Technologies Used

### Backend

* **Python**
* **Flask**
* **Flask-Bcrypt**
* **Flask-Login**
* **SQLAlchemy**

### Database

* **MySQL**
* **PyMySQL**

### Frontend

* **HTML**
* **CSS**
* **JavaScript**
* **Bootstrap**

### Testing & DevOps

* **Pytest** for automated testing.
* **Git & GitHub** for version control.
* **GitHub Actions** for Continuous Integration (CI).

## Project Structure

```text
Lost-Found Management/
│
├── app.py
├── models.py
├── dbs.sql
├── requirements.txt
├── test_app.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_item.html
│   ├── edit_item.html
│   ├── item_details.html
│   ├── profile.html
│   └── update_profile.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   └── images/
│
└── instance/
```

## Dashboard

The dashboard is one of the implemented features of the project.

It displays:

```text
Total Items
Lost Items
Found Items
```

It also provides navigation buttons for viewing items, reporting an item, and logging out.

## Testing

The project includes basic automated tests using **Pytest**.

Example tests verify:

* Flask application is created successfully.
* Login page is accessible.

Run the tests using:

```bash
cd "Lost-Found Management"
python -m pytest -q
```

## GitHub Actions CI

The project uses **GitHub Actions** to automatically test the application whenever changes are pushed or a Pull Request is created.

The CI pipeline performs the following steps:

```text
Checkout Code
      ↓
Set up Python 3.11
      ↓
Install Dependencies
      ↓
Check Python Syntax
      ↓
Run Pytest
      ↓
Build Passed
```

This helps ensure that new changes do not introduce basic syntax or testing errors.

## Branching & Collaboration

The project follows a feature-based Git workflow.

Example:

```text
main
 │
 ├── mamta-dashboard
 │
 ├── member-login
 │
 └── member-report-item
```

Different members can work on separate features using their own branches and then create Pull Requests to merge their changes into the `main` branch.

## Future Enhancements

* Automatic matching between lost and found items.
* User notifications when a potential match is found.
* Improved dashboard analytics.
* Image-based item matching.
* Advanced search and filtering.
* Email notifications for important item updates.
* Improved role-based access control.

## License

This project is licensed under the **MIT License**.

You are welcome to use, modify, and enhance the application.
