def copy_file(source, destination):

    with open(source, "r") as source_file:
        data = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(data)

    print("File copied successfully.")


if __name__ == "__main__":
    copy_file("file1.txt", "file_copy.txt")
