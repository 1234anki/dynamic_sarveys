import tkinter as tk
from tkinter import ttk
import psycopg2

class SurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Survey Form")
        self.root.geometry("800x600")

        self.table_names = self.fetch_table_names()
        self.current_table_index = 0

        self.question_frame = ttk.Frame(self.root)
        self.question_frame.pack(fill='both', expand=True)

        self.question_label = ttk.Label(self.question_frame, text="")
        self.question_label.pack(anchor='w', padx=5, pady=10)

        self.option_canvas = tk.Canvas(self.question_frame)
        self.option_canvas.pack(side="left", fill="both", expand=True)

        self.option_frame = ttk.Frame(self.option_canvas)
        self.option_frame.pack(fill='both', expand=True)

        self.option_scroll = ttk.Scrollbar(self.question_frame, orient="vertical", command=self.option_canvas.yview)
        self.option_scroll.pack(side="right", fill="y")

        self.option_canvas.configure(yscrollcommand=self.option_scroll.set)
        self.option_canvas.bind("<Configure>", lambda e: self.option_canvas.configure(scrollregion=self.option_canvas.bbox("all")))
        self.option_canvas.create_window((0, 0), window=self.option_frame, anchor="nw")

        self.option_frame.bind("<Configure>", lambda e: self.option_canvas.configure(scrollregion=self.option_canvas.bbox("all")))

        self.option_var = tk.StringVar()
        self.option_buttons = []

        self.submit_button = ttk.Button(self.question_frame, text="Submit", command=self.submit_answer, state="disabled")
        self.submit_button.pack(pady=10)

        self.next_button = ttk.Button(self.question_frame, text="Next", command=self.next_question, state="disabled")
        self.next_button.pack(pady=10)

        self.load_next_question()
        self.add_developer_types()
        self.add_developer_levels()

    def fetch_table_names(self):
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="student_information",
            user="postgres",
            password="ANKITA",
            host="localhost",
            port="5432"
        )

        # Create a cursor object to execute SQL queries
        cur = conn.cursor()

        # Execute the SQL query to fetch table names
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

        # Fetch all rows from the result set
        tables = cur.fetchall()

        # Close the cursor and connection
        cur.close()
        conn.close()

        return [table[0] for table in tables]  # Extract table names from the result

    def fetch_column_names(self, table_name):
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="student_information",
            user="postgres",
            password="ANKITA",
            host="localhost",
            port="5432"
        )

        # Create a cursor object to execute SQL queries
        cur = conn.cursor()

        # Execute the SQL query to fetch column names from the specified table
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")

        # Fetch all rows from the result set
        columns = cur.fetchall()

        # Close the cursor and connection
        cur.close()
        conn.close()

        return [column[0] for column in columns]  # Extract column names from the result

    def load_next_question(self):
        if self.current_table_index < len(self.table_names):
            # Clear previous question and options
            for widget in self.option_frame.winfo_children():
                widget.destroy()

            table_name = self.table_names[self.current_table_index]
            self.current_table_index += 1
            columns = self.fetch_column_names(table_name)
            question = f"Select one row from table '{table_name}':"
            self.question_label.config(text=question)

            # Fetch row data
            conn = psycopg2.connect(
                dbname="student_information",
                user="postgres",
                password="ANKITA",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table_name}")
            rows = cur.fetchall()
            conn.close()

            # Display column names with radiobuttons
            column_radios = ttk.LabelFrame(self.option_frame, text="Columns")
            column_radios.pack(fill='both', expand=True)
            self.column_var = tk.StringVar()
            for column_name in columns:
                ttk.Radiobutton(column_radios, text=column_name, variable=self.column_var, value=column_name).pack(anchor='w', padx=5, pady=2)

            # Display row data with radiobuttons
            row_radios = ttk.LabelFrame(self.option_frame, text="Rows")
            row_radios.pack(fill='both', expand=True)
            self.row_var = tk.StringVar()
            for row_index, row in enumerate(rows):
                ttk.Radiobutton(row_radios, text=str(row), variable=self.row_var, value=str(row)).pack(anchor='w', padx=5, pady=2)

            self.submit_button.config(state="enabled")  # Enable submit button
            self.next_button.config(state="enabled")  # Enable next button
        else:
            self.question_label.config(text="End of Survey")
            self.next_button.config(state="disabled")  # Disable next button

    def next_question(self):
        self.load_next_question()

    def submit_answer(self):
        selected_column = self.column_var.get()
        selected_row = self.row_var.get()
        if selected_column and selected_row:
            answer = f"{selected_column}: {selected_row}"
            self.process_answer(answer)
            self.submit_button.config(state="disabled")  # Disable submit button after submission
            self.next_button.config(state="enabled")  # Enable next button
        else:
            print("Please select a column and a row.")

    def process_answer(self, answer):
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="student_information",
            user="postgres",
            password="ANKITA",
            host="localhost",
            port="5432"
        )

        # Create a cursor object to execute SQL queries
        cur = conn.cursor()

        try:
            # Insert the selected answer into the database
            cur.execute("INSERT INTO survey_answers (answer) VALUES (%s)", (answer,))
            conn.commit()
            print("Answer submitted successfully:", answer)
        except psycopg2.Error as e:
            conn.rollback()
            print("Error:", e)
        finally:
            # Close the cursor and connection
            cur.close()
            conn.close()

    def add_developer_types(self):
        developer_types = [
            'Frontend Developer',
            'Backend Developer',
            'Full-stack Developer',
            'Mobile App Developer',
            'DevOps Engineer'
        ]
        conn = psycopg2.connect(
            dbname="student_information",
            user="postgres",
            password="ANKITA",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        try:
            for dev_type in developer_types:
                cur.execute("INSERT INTO DeveloperTypes (TypeName) VALUES (%s)", (dev_type,))
            conn.commit()
            print("Developer types added successfully.")
        except psycopg2.Error as e:
            conn.rollback()
            print("Error:", e)
        finally:
            cur.close()
            conn.close()

    def add_developer_levels(self):
        developer_levels = [
            'Junior Developer',
            'Intermediate Developer',
            'Senior Developer',
            'Lead Developer'
        ]
        conn = psycopg2.connect(
            dbname="student_information",
            user="postgres",
            password="ANKITA",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        try:
            for dev_level in developer_levels:
                cur.execute("INSERT INTO DeveloperLevels (LevelName) VALUES (%s)", (dev_level,))
            conn.commit()
            print("Developer levels added successfully.")
        except psycopg2.Error as e:
            conn.rollback()
            print("Error:", e)
        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()
