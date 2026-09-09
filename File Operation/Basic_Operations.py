import os

FILE_NAME = "employee_data.txt"


# Create and write data
def create_file():
    with open(FILE_NAME, "w") as file:
        file.write("Yukti\n")
        file.write("Rahul\n")
        file.write("Amit\n")
        file.write("Priya\n")

    print("File created and data written successfully.")


# Read complete file
def read_file():
    with open(FILE_NAME, "r") as file:
        data = file.read()

    print("\nFile Content:")
    print(data)


# Append data
def append_data():
    with open(FILE_NAME, "a") as file:
        file.write("Neha\n")

    print("Data appended successfully.")


# Check file exists
def check_file_exists():
    if os.path.exists(FILE_NAME):
        print(f"{FILE_NAME} exists.")
    else:
        print(f"{FILE_NAME} does not exist.")


# Rename file
def rename_file():
    new_name = "employee_data_updated.txt"

    if os.path.exists(FILE_NAME):
        os.rename(FILE_NAME, new_name)
        print(f"File renamed to {new_name}")


if __name__ == "__main__":
    create_file()
    read_file()
    append_data()
    check_file_exists()
