import csv

def read_login_csv(file_path):
    login_data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            login_data.append(row)
    return login_data