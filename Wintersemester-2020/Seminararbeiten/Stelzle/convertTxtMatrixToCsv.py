def convert_to_csv():
    file_reader = open("TheMatrix2003_dash.txt")

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
    matrix_csv_file = open('TheMatrix2003.csv', 'w')

    for line in file_reader_2:
        if ' ' in line:
            line = line.replace(" ", '')
        if '""' in line:
            line = line.replace('""', '\n')
        matrix_csv_file.write(line)


if __name__ == "__main__":
    convert_to_csv()