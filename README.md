# Survey Form Application

This is a Python application built using Tkinter and PostgreSQL that allows users to fill out survey forms by selecting options from tables in a PostgreSQL database.

## Features

- Fetches table names from a PostgreSQL database and presents them as survey questions.
- Allows users to select one row from each table as their answer.
- Stores the selected answers in a PostgreSQL database table named `survey_answers`.
- Includes functionality to add predefined developer types and levels to the database tables for demonstration purposes.
- Provides a simple graphical user interface for users to interact with.

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/your_username/survey-form.git




2. Install the required dependencies:

pip install psycopg2-binary



3. Ensure you have PostgreSQL installed and running on your system.

4. Modify the database connection details (`dbname`, `user`, `password`, `host`, `port`) in the `SurveyApp` class to match your PostgreSQL setup.

## Usage

1. Run the `main.py` file to start the application:


Sure, here's a simple README template you can use for your project:

markdown
Copy code
# Survey Form Application

This is a Python application built using Tkinter and PostgreSQL that allows users to fill out survey forms by selecting options from tables in a PostgreSQL database.

## Features

- Fetches table names from a PostgreSQL database and presents them as survey questions.
- Allows users to select one row from each table as their answer.
- Stores the selected answers in a PostgreSQL database table named `survey_answers`.
- Includes functionality to add predefined developer types and levels to the database tables for demonstration purposes.
- Provides a simple graphical user interface for users to interact with.

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/your_username/survey-form.git

markdown
Copy code

2. Install the required dependencies:

pip install psycopg2-binary

markdown
Copy code

3. Ensure you have PostgreSQL installed and running on your system.

4. Modify the database connection details (`dbname`, `user`, `password`, `host`, `port`) in the `SurveyApp` class to match your PostgreSQL setup.

## Usage

1. Run the `main.py` file to start the application:

python main.py


2. Follow the on-screen instructions to fill out the survey form.

3. Click the "Next" button to move to the next question, and the "Submit" button to submit your answers.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

