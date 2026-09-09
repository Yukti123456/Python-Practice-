def compare_files(file1, file2):

    with open(file1, "r") as f1:
        data1 = f1.read()

    with open(file2, "r") as f2:
        data2 = f2.read()

    if data1 == data2:
        print("Both files contain the same data.")
        return True
    else:
        print("Files contain different data.")
        return False


if __name__ == "__main__":
    compare_files("file1.txt", "file2.txt")
