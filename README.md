# Indixpert-July2025-Batch
# Azure Haven Hotel Management System

A command-line based Hotel Management System for managing table bookings, food orders, payments, and invoices. Designed for staff use with role-based access.

## Features

- Show available menu items
- Book tables for customers
- View all bookings
- Take food orders
- View all orders
- Process payments (Cash, Card, UPI)
- Generate invoices
- Cancel booked tables
- Error logging to track issues

## Technologies Used

- Python 3.12.4 and #(Python 3.4.4 sometimes)
- JSON for data storage
- RE for validation
- Getpass for password masking
- Colorama for colored terminal output
- Txt file for log storage

## Project Structure

hotel-management/
├─ authentication/ # User/admin authentication modules
│ ├─ authentication_menu.py
│ ├─ users_details.py
│ └─ init.py
├─ database/ # Stores JSON data files
│ ├─ booked_table.json
│ ├─ customer_orders.json
│ ├─ menu.json
│ ├─ payment_file.json
│ └─ user_data.json
├─ domain/ # Core classes and functions
│ ├─ Admin_menu.py
│ ├─ identify_user.py
│ ├─ Logging.py
│ ├─ Show_menu.py
│ ├─ Show_staff.py
│ ├─ Staff_menu.py
│ ├─ Table_booking.py
│ ├─ Update_menu.py
│ └─ Update_staff_details.py
├─ log/ # Stores error logs
│ └─ error.txt
├─ validation/ # Input validation functions
│ ├─ valid_date.py
│ ├─ valid_email.py
│ ├─ valid_name.py
│ ├─ valid_password.py
│ ├─ valid_table.py
│ └─ valid_time.py
└─ README.md