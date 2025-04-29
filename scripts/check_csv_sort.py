import csv
import sys
from natsort import natsorted

def is_sorted_column(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)
        column = [row[0] for row in reader if row]
        return column == natsorted(column)

if __name__ == "__main__":
    csv_path = sys.argv[1]
    if is_sorted_column(csv_path):
        print(f"✅ {csv_path} is sorted by the first column.")
    else:
        print(f"❌ {csv_path} is NOT sorted by the first column.")
        sys.exit(1)
