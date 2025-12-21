# Azure Haven Hotel Management System

A command-line–based Hotel Management System designed for staff and administrators to manage table bookings, food orders, payments, and invoice generation with role-based access control.

---

## Features

- Display available menu items  
- Table booking for customers  
- View and manage all bookings  
- Take and manage food orders  
- View all orders  
- Process payments (Cash, Card, UPI)  
- Generate invoices  
- Cancel table bookings  
- **Admin functionalities:**  
  - Update menu prices (increase/decrease)  
  - Add or remove dishes  
  - Add or delete categories  
  - Apply discounts on menu items  
  - Manage staff members (add/remove)  
  - View sales reports (most sold items)  
- Error logging for issue tracking  
- **Role-based access:** Menus and available functionalities depend on whether the user is Staff or Admin

---

## Technologies Used

- Python 3.12.4  
- JSON for data storage  
- `re` (Regular Expressions) for input validation  
- `getpass` for secure password input  
- `collections` for tracking most ordered items  
- `colorama` for colored terminal output  
- Text files for error logging  
- `Loging.py` module handles appending errors to `log/error.txt`

---

## Project Structure

authentication/
authentication_menu.py
users_details.py

database/
booked_table.json
customer_orders.json
menu.json
payment_file.json
price_update.json
user_data.json

domain/
Admin_menu.py
identify_user.py
Loging.py
Report_menu.py
Show_menu.py
Staff_menu.py
Table_booking.py
Update_menu.py
Update_price.py
Update_staff_details.py

log/
error.txt

report/
Report.py

validation/
Valid_date.py
Valid_email.py
Valid_name.py
Valid_password.py
Valid_table.py
Valid_time.py

main.py
README.md

---

## How to Use

### Staff Menu  
After logging in as **Staff**, the following menu options are available:


- **Show Menu** – Displays all available dishes.  
- **Book Table** – Reserve a table for a customer.  
- **View Booking** – View all current bookings.  
- **Take Order** – Record a customer’s food order.  
- **View Orders** – See all active orders.  
- **Take Payment** – Process payment via Cash, Card, or UPI.  
- **Show Invoice** – Generate and display the invoice.  
- **Cancel Booked Table** – Cancel a table reservation.  
- **Log Out** – Exit the staff menu.

---

### Admin Menu  
After logging in as **Admin**, the following menu options are available:


- **Menu** – Display all available dishes.  
- **Delete Dish / Add Dish** – Remove or add a dish to the menu.  
- **Add New Category / Delete Category** – Manage menu categories.  
- **Update Dish Price** – Change the price of existing dishes.  
- **Price and Discount Management** – Apply discounts or modify prices dynamically.  
- **Add / Remove Staff Member** – Manage staff users.  
- **Show Staff** – Display all staff members.  
- **Report** – Displays a sub-menu with sales and booking statistics, including total bookings, current month bookings, total earnings, current month earnings, average booking duration, most ordered items, and payment methods.  
- **Log Out** – Exit the admin menu.

---


