import sys

def convert_to_csv(file_name:str):
    file_reader = open(file_name)

    temporary_file = open("temporary.txt", "w")

    for line in file_reader:
        if "\n" in line:
            line = line.replace("\n", '')

        if '",,"' in line:
            line = line.replace('",,"', ',,')
        elif '","' in line:
            line = line.replace('","', ',')
        elif ',"' in line:
            line = line.replace(',"', ',')
        elif '",' in line:
            line = line.replace('",', ',')

        if '"' in line:
            line = line.replace(',"', '\n')

        temporary_file.write(line)

    temporary_file.close()
    file_reader.close()

    file_reader_2 = open("temporary.txt")
    matrix_csv_file = open('createdMatrix.csv', 'w')

    for line in file_reader_2:
        if ' ' in line:
            line = line.replace(" ", '')
        if '""' in line:
            line = line.replace('""', '\n')
        matrix_csv_file.write(line)


if __name__ == "__main__":
    parameter_file_name = ""

    if len(sys.argv) < 1:
        print("No file name specified.")
    else:
        parameter_file_name = sys.argv[1]

    convert_to_csv(parameter_file_name)