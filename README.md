# Student Report Card Management System

## Description
This is a Python-based GUI application for managing student report cards. The system allows users to input student details, calculate their grades, generate report cards, and store data in a MySQL database. The application is built using Tkinter for the user interface and MySQL for data storage.

## Features
- **User Authentication:** Login and registration system.
- **Student Information Storage:** Save student details in a MySQL database.
- **Report Card Generation:** Automatically calculate grades and generate report cards.
- **CSV & Text Export:** Export student data into CSV and text files.
- **Database Integration:** Uses MySQL to manage and retrieve student records.
- **GUI Interface:** Built with Tkinter for an easy-to-use experience.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- MySQL Server
- Required Python packages:
  ```sh
  pip install mysql-connector-python
  ```

### Steps to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Run the Python script:
   ```sh
   python main.py
   ```
3. Follow the on-screen instructions to enter student details and generate report cards.

## Usage
- Run `main.py` to start the application.
- Enter student details and grades.
- Generate and export the report card.
- View and manage records using MySQL.

## Database Setup
1. Ensure MySQL is running.
2. Create a database:
   ```sql
   CREATE DATABASE student_records;
   ```
3. Update `main.py` with your MySQL credentials if needed.

## File Structure
- `main.py` - Main application script.
- `README.md` - Documentation.
- `.gitignore` - Ignores unnecessary files.

## License
This project does not have an open-source license. Unauthorized use, reproduction, or distribution is prohibited.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author
Nishant Sreekumar

## Acknowledgments
- Python community
- MySQL documentation

