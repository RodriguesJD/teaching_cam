import os
import csv


def write_to_file(data_to_write):
    with open('playing_with_data_types.csv', mode='w') as employee_file:
        file_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        header = "data_type"
        file_header = file_writer.writerow([header])
        print(header)
        for line_to_write in data_to_write:
            file_writer.writerow(line_to_write)
            print(line_to_write)



