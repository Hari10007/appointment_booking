# Appointment Booking System

This is a Django-based Appointment Booking System that allows users to book appointments with available time slots.

## 🚀 Features

- Book appointments for available time slots
- Prevent double booking for the same time
- Validate phone numbers and required fields
- Fetch available slots dynamically
- Display booked appointments

---

## 📌 Installation Guide

### 1️ Clone the Repository

```bash
git clone https://github.com/your-repo/appointment-booking.git
cd appointment-booking
```

### 2️ Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️ Configure Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5 Run the Development Server

```bash
python manage.py runserver
```

Open your browser and go to: [**http://127.0.0.1:8000/**](http://127.0.0.1:8000/)

---               |

---

## 🧪 Running Tests

To run unit tests, execute:

```bash
python manage.py test
```

---

## 📌 Technologies Used

- Python 3
- Django
- Bootstrap
- SQLite

---
