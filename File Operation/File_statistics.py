def file_statistics(file_name):

    with open(file_name, "r") as file:
        data = file.read()

    lines = data.splitlines()
    words = data.split()

    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", len(data))


if __name__ == "__main__":
    file_statistics("employee_data.txt")
