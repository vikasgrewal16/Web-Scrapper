# Web Scraper Project

This project is a web scraper designed to extract information from websites, including emails, addresses, contact numbers, language, CMS type, and categories. The data is stored in a MySQL database and can be exported to a CSV file.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Database Setup](#database-setup)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Installation and Setup

### Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed on your machine.
2. **MySQL Server**: Make sure MySQL server is installed and running.
3. **Required Python Libraries**: Install the required libraries using pip.

   ```sh
   pip install -r requirements.txt

### Prerequisites

1. Create a MySQL database named website_info.
2. Execute the SQL script located in the scripts dbms_scripts.sql file to create the necessary tables.

### Configuration

Before running the web scraper, you need to configure the database connection in the `db.py` file.

1. **Open `db.py`**: Locate the `db.py` file in the `src` directory.

2. **Update Database Credentials**: Replace the default credentials with your MySQL server credentials.

3.     password='your_password',  # Update this line with your MySQL password
4.     database='website_info'    # Update this line if your database name is different

5. Save the File: After updating the credentials, save the db.py file.

### Usage
1. Prepare Input Data: Place your input CSV file (e.g., list.csv) in the data folder. The CSV should contain a list of websites to scrape.

2. Run the Scraper: Execute the main.py script to start the web scraping process.

    ```sh
    python src/main.py
3. Output: The extracted data will be stored in the MySQL database and exported to output.csv in the data folder.

