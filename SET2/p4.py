import csv

def calculate_average(csv_file, column_name):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            if column_name not in reader.fieldnames:
                print(f"Column '{column_name}' not found.")
                return None

            total, count = 0, 0
            for row in reader:
                try:
                    total += float(row[column_name])
                    count += 1
                except ValueError:
                    print(f"Skipping row {reader.line_num}: Invalid value.")

            return total / count if count else None

    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
        return None

csv_file_path = 'file.csv'
column_to_calculate = 'ENGLISH'

result = calculate_average(csv_file_path, column_to_calculate)
if result is not None:
    print(f"Average value in '{column_to_calculate}': {result}")