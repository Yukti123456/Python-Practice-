def search_text(file_name, search_word):

    with open(file_name, "r") as file:
        for line_number, line in enumerate(file, start=1):

            if search_word.lower() in line.lower():
                print(
                    f"'{search_word}' found at line "
                    f"{line_number}: {line.strip()}"
                )


if __name__ == "__main__":
    search_text("employee_data.txt", "Yukti")
