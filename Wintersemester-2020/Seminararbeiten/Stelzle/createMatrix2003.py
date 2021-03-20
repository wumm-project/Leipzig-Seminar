import csv


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


def create_lookup(file: str):
    file_reader = open(file)
    lookup = {}

    for line in file_reader:
        if "\n" in line:
            line = line.replace("\n", "")
        splitted_line = line.split(':')
        if splitted_line[0] not in lookup.keys():
            lookup[splitted_line[0]] = splitted_line[1]

    return lookup


def read_matrix():
    matrix = []
    with open("TheMatrix2003.csv", newline='') as matrix_csv:
        reader = csv.reader(matrix_csv, delimiter=',')
        for row in reader:
            matrix.append(row)

    return matrix


def print_matrix(matrix: list):
    for entry in matrix:
        print(entry)


def build_matrix_ttl(matrix: list, principle_lookup: dict, parameter_lookup: dict):
    ttl_writer = open("TheMatrix2003.ttl", "a")

    entry_prefix = "<http://opendiscovery.org/rdf/Matrix/E"
    matrix_entry = "a od:MatrixEntry ."

    for row in range(0, len(matrix)):

        parameter_row = row + 1
        increasing_parameter = "od:increasingParameter tc:" + parameter_lookup[str(parameter_row)] + " ;"
        for column in range(0, len(matrix[row])):
            ttl_entry = ""
            parameter_column = column + 1
            decreasing_parameter = "od:decreasingParameter tc:" + parameter_lookup[str(parameter_column)] + " ;"
            recommended_principles = "od:recommendedPrinciple "
            splitted_principle = matrix[row][column].split('-')
            for principle in range(0, len(splitted_principle)):
                if splitted_principle[principle] == '':
                    recommended_principles += "tc:NoPrinciple"
                elif principle == len(splitted_principle) - 1:
                    recommended_principles += "tc:" + principle_lookup[splitted_principle[principle]]
                else:
                    recommended_principles += "tc:" + principle_lookup[splitted_principle[principle]] + ", "
            recommended_principles += " ;"

            ttl_entry += entry_prefix + "." + prefix_zero(parameter_row) + "." + prefix_zero(
                parameter_column) + ">" + add_newline()
            ttl_entry += add_tab() + decreasing_parameter + add_newline()
            ttl_entry += add_tab() + increasing_parameter + add_newline()
            ttl_entry += add_tab() + recommended_principles + add_newline()
            ttl_entry += add_tab() + matrix_entry + add_newline()
            ttl_entry += add_newline()

            ttl_writer.write(ttl_entry)


def prefix_zero(number: int):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)


def add_tab():
    return "\t"


def add_newline():
    return "\n"


if __name__ == '__main__':
    convert_to_csv()

    matrix = read_matrix()
    print_matrix(matrix)

    principle_lookup = create_lookup('principles.txt')
    print(principle_lookup)

    parameter_lookup = create_lookup('parameters.txt')
    print(parameter_lookup)

    build_matrix_ttl(matrix, principle_lookup, parameter_lookup)
