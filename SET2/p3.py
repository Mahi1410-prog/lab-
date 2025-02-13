def count(path):
    try:
        with open(path, 'r') as file:
            file_content = file.read()
            return f"data = {file_content.split()} \nlength of the words: {len(file_content.split())}"
    except FileNotFoundError:
        return "Please Provide a valid file path."

path = "example.txt"
print(count(path))