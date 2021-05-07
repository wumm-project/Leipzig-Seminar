import csv
import sys

turtle_header = """@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix cc: <http://creativecommons.org/ns#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix od: <http://opendiscovery.org/rdf/Model#> .
@prefix odq: <http://opendiscovery.org/rdf/Principle/> .
@prefix odr: <http://opendiscovery.org/rdf/Parameter/> .
@prefix tc: <http://opendiscovery.org/rdf/Concept/> .

<http://opendiscovery.org/rdf/TheMatrix-Old/>
    cc:attributionName "The Open Discovery Project" ;
    cc:attributionURL <http://opendiscovery.org> ;
    cc:license <http://www.apache.org/licenses/LICENSE-2.0> ;
    dcterms:source <http://www.i-sim.org/Altshuller_Matrix.xls>,
    <https://www.triz-consulting.de/triz-matrix> ;
    a owl:Ontology ;
    owl:imports <http://opendiscovery.org/rdf/TheParameters/>; 
    rdfs:label "TRIZ Matrix - The Old Version" .

od:MatrixEntry
    a owl:Class ;
    rdfs:label "A Entry within the Matrix" .
    
"""


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


def create_two_paramter_lookup(file: str, second_parameter: dict):
    file_reader = open(file)
    lookup = {}

    for line in file_reader:
        if "\n" in line:
            line = line.replace("\n", "")
        line_dict = {}
        splitted_by_name_line = line.split(":")
        splitted_parameter_line = splitted_by_name_line[0].split(".")
        if splitted_parameter_line[1] not in lookup.keys():
            line_dict['second_parameter'] = second_parameter[splitted_parameter_line[0]]
            line_dict['name'] = splitted_by_name_line[1]
            lookup[splitted_parameter_line[1]] = line_dict

    return lookup


def read_matrix(file_name: str):
    matrix = []
    with open(file_name, newline='') as matrix_csv:
        reader = csv.reader(matrix_csv, delimiter=',')
        for row in reader:
            matrix.append(row)

    return matrix


def print_matrix(matrix: list):
    for entry in matrix:
        print(entry)


def build_matrix_ttl(matrix: list, principle_lookup: dict, two_parameter_lookup: dict):
    ttl_writer = open("created_matrix.ttl", "a")

    entry_prefix = "<http://opendiscovery.org/rdf/Matrix/E"
    matrix_entry = "a od:MatrixEntry ."

    ttl_writer.write(turtle_header)

    for row in range(0, len(matrix)):

        parameter_row = row + 1
        increasing_dict = two_parameter_lookup[str(parameter_row)]
        upper_increasing_parameter = "od:upperIncreasingParameter tc:" + increasing_dict["second_parameter"] + " ;"
        increasing_parameter = "od:increasingParameter tc:" + increasing_dict["name"] + " ;"
        for column in range(0, len(matrix[row])):
            ttl_entry = ""
            parameter_column = column + 1
            decreasing_dict = two_parameter_lookup[str(parameter_column)]
            upper_decreasing_parameter = "od:upperDecreasingParameter tc:" + decreasing_dict["second_parameter"] + " ;"
            decreasing_parameter = "od:decreasingParameter tc:" + decreasing_dict["name"] + " ;"
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
            ttl_entry += add_tab() + upper_decreasing_parameter + add_newline()
            ttl_entry += add_tab() + decreasing_parameter + add_newline()
            ttl_entry += add_tab() + upper_increasing_parameter + add_newline()
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
    parameter_file_name = ""

    if len(sys.argv) < 1:
        print("No file name specified.")
    else:
        parameter_file_name = sys.argv[1]

    matrix = read_matrix(parameter_file_name)
    print_matrix(matrix)

    principle_lookup = create_lookup('principles.txt')
    print(principle_lookup)

    upper_parameter_lookup = create_lookup('upperParameters.txt')
    print(upper_parameter_lookup)

    parameter_lookup = create_two_paramter_lookup('parameters.txt', upper_parameter_lookup)
    print(parameter_lookup)

    build_matrix_ttl(matrix, principle_lookup, parameter_lookup)
