# Personal Notes App 📝

A simple personal notes application built with **Python and Django** as part of my project-based learning journey.

The main goal of this project is to understand Django fundamentals, especially CRUD operations, request-response flow, forms, models, views, templates, and database interactions.

## 🎯 Learning Objectives

Through this project, I am learning how to:

- Understand Django's project and app structure.
- Create models and work with databases using Django ORM.
- Implement CRUD operations (Create, Read, Update, and Delete).
- Handle HTTP GET and POST requests.
- Create and validate forms using Django Forms.
- Connect URLs to views using URL routing.
- Render dynamic HTML using Django templates.
- Work with database migrations.
- Write basic automated tests using Django's testing framework.
- Understand how different parts of a Django application work together.

## ✨ Features

- **Create Notes** — Create notes with a title and content.
- **View Notes** — Display saved notes on the homepage.
- **View Note Details** — Open an individual note to see its full content.
- **Edit Notes** — Update existing notes.
- **Delete Notes** — Delete notes after visiting a confirmation page.
- **Search Notes** — Search notes by title.
- **Timestamps** — Track when notes are created and updated.

## 🛠️ Tech Stack

- **Language:** Python
- **Web Framework:** Django
- **Database:** SQLite
- **Frontend:** HTML and Django Templates
- **Testing:** Django Test Framework
- **Version Control:** Git and GitHub

## 📂 Project Structure

```text
personal-notes-app/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── notes/
│   ├── migrations/
│   ├── templates/
│   │   └── notes/
│   │       ├── home.html
│   │       ├── note_detail.html
│   │       ├── note_edit.html
│   │       └── note_confirm_delete.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd personal-notes-app
```

Replace `<your-repository-url>` with the URL of your GitHub repository.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

A virtual environment keeps this project's Python dependencies separate from other projects on your computer.

### 3. Activate the virtual environment

**Windows — Command Prompt**

```bash
.venv\Scripts\activate
```

**Windows — PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

This installs the Python packages listed in `requirements.txt`.

### 5. Apply database migrations

```bash
python manage.py migrate
```

Django uses migrations to create and update the database schema based on the project's migration files.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## 🧪 Running Tests

Run the project's automated tests with:

```bash
python manage.py test
```

Django's test framework checks application behavior and helps identify regressions when the code changes.

## 🧠 What I Learned

This project is helping me understand:

- How a browser request reaches a Django view through URL routing.
- How views interact with forms and database models.
- How Django ORM queries create, retrieve, update, and delete records.
- How templates display data passed from views.
- How redirects and form validation fit into the request-response cycle.
- How automated tests help verify application behavior.

## 🚀 Future Improvements

As I continue learning Django, I may extend the project with:

- User authentication and private notes.
- Note categories or tags.
- Improved UI and responsive styling.
- Search by note content.
- Pagination for larger collections of notes.

These are potential learning goals rather than features currently implemented.

## 📌 Project Purpose

This is a learning project created to practice Django through hands-on development. The focus is on understanding the fundamentals and building a strong foundation before moving on to more advanced Django concepts.

## 👨‍💻 Author

Built as part of my journey to learn Django through project-based learning.

