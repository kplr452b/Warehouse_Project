import json
import os

# Function to generate data
def generate_data():
    # Replace with your data generation logic
    data = {"example": "data"}
    return data

# Function to save data
def save(data=None, filename="warehouse"):
    """Save the mocked data into a json file."""
    if data:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        initial_dir = os.path.join(script_dir, "sample", "initial")

        if not os.path.exists(initial_dir):
            os.makedirs(initial_dir)

        file_path = os.path.join(initial_dir, f"{filename}.json")
        with open(file_path, "w") as file:
            file.write(json.dumps(data))

        solution_dir = os.path.join(script_dir, "sample", "solution")
        if not os.path.exists(solution_dir):
            os.makedirs(solution_dir)

        solution_file_path = os.path.join(solution_dir, f"{filename}.json")
        with open(solution_file_path, "w") as file:
            file.write(json.dumps(data))

# Function to create and save data
def create_and_save(filename="warehouse"):
    data = generate_data()
    save(data, filename)

    # Optional: Query the saved data
    query_data(filename)

# Function to query data
def query_data(filename):
    # Replace with your query logic
    print(f"Querying data from {filename}.json")

# Main entry point of the script
if __name__ == "__main__":
    print("This will replace the data in the exercise. Are you sure you want to proceed?(y/n)", end=" ")
    choice = input()
    if choice.lower() == "y":
        create_and_save(filename="warehouse1")