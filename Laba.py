import csv
import json

def write_to_csv(file_name):
    try:
        with open(file_name, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(['Name', 'Age', 'City'])

            while True:
                name = input("Enter name (or type 'stop' to finish): ")
                if name.lower() == 'stop':
                    break
                age = input("Enter age: ")
                city = input("Enter city: ")

                writer.writerow([name, age, city])

        print(f"Data successfully written to {file_name}")

    except IOError as e:
        print(f"An I/O error occurred: {e}")

def csv_to_json(csv_file_name, json_file_name):
    try:
        data = []
        with open(csv_file_name, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open(json_file_name, mode='w', encoding='utf-8') as json_file:
            json.dump({"data": data}, json_file, indent=4)

        print(f"Data successfully converted to {json_file_name}")

    except FileNotFoundError:
        print(f"File {csv_file_name} not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

csv_file = 'data.csv'
json_file = 'data.json'

write_to_csv(csv_file)
csv_to_json(csv_file, json_file)
