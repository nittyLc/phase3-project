Library Management System

Overview

This Library Management System is a CLI-based application built with Python and SQLAlchemy to handle key functionalities like managing books, members, and book borrow records in a library. It features object-oriented programming principles, database migrations with Alembic, and persistent data storage with SQLite.

Features

Book Management: Add, view, and list books.

Member Management: Register members and view member details.

Borrow Management: Record book borrowing and ensure copies are updated accordingly.

Persistent Storage: All data is stored in an SQLite database.


Installation

Clone the repository:

git clone https://github.com/yourusername/CLI-project.git
cd CLI-project

Install dependencies:

pipenv install

Activate the virtual environment:

pipenv shell

Set up the database:

alembic upgrade head



Usage

Run the CLI:

python -m lib.cli

Follow the on-screen prompts to:

Add a new book

Register a new member

Borrow a book

Database Management

Generate a new migration:

alembic revision --autogenerate -m "Migration message"

Apply migrations:

alembic upgrade head



Technologies Used

Python

SQLAlchemy

Alembic

SQLite
