![1](https://github.com/user-attachments/assets/6a9cf126-2b4b-43a3-9e56-3795a9c83dfb)
# Tire Sales Management System

## Description
This repository contains a Flask web application designed to manage tire sales. It provides functionality for adding sales records, searching through records by various criteria, and displaying all the sales data.

## Features
- **Add Sale**: Record new tire sales with details such as the tire's serial number, name, and buyer.
- **Search**: Search for sales records by tire's serial number, buyer's name, or sale date.
- **View Sales**: Display all the recorded tire sales in a tabulated format.

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask
- SQLite3

### Setup
Clone the repository to your local machine:
git clone https://github.com/your-username/your-repository.git cd your-repository

Install the required Python packages:
pip install -r requirements.txt

### Running the Application
To run the application locally, execute:
python run_flask_app.py


The script will start the Flask server and open the application in your default web browser.

## File Structure
- `app.py`: The main Flask application file with routes and configurations.
- `run_flask_app.py`: Script to run the Flask application with automatic browser opening.
- `style.css`: CSS file for styling the application.
- HTML templates:
  - `base.html`: Base template with common layout and navigation.
  - `add.html`: Template for adding new sales records.
  - `index.html`: Template displaying all sales records.
  - `menu.html`: Main menu with navigation links.
  - `search.html`: Search form for filtering records.
  - `search_results.html`: Displays results of a search.

## Database
This application uses SQLite as its database. Ensure that the `tire_shop.db` is properly set up and accessible.

## Contributing
Feel free to fork this repository and submit pull requests. You can also open issues if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
