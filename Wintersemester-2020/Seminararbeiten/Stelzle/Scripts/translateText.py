import sys

from deep_translator import (GoogleTranslator)


def read_turtle_file(file_name: str):
    turtle_file = open(file_name)

    content = turtle_file.readlines()

    translated_turtle_file = open("translated_" + file_name, 'w+')

    for line in content:
        if "@" in line and "@prefix" not in line:
            if "@de" not in line or "@en" not in line or "@ru" not in line:
                quote_split = line.split('"')
                first_word = quote_split[1]
                first_language = ""

                if not first_word:
                    print('Empty Value!')
                    continue

                if "@de" in quote_split[2]:
                    first_language = "de"
                elif "@en" in quote_split[2]:
                    first_language = "en"
                elif "@ru" in quote_split[2]:
                    first_language = "ru"

                if "@de" not in line:
                    line = translate(first_word, first_language, line, "de")
                if "@en" not in line:
                    line = translate(first_word, first_language, line, "en")
                if "@ru" not in line:
                    line = translate(first_word, first_language, line, "ru")

        translated_turtle_file.write(line)


def translate(first_word: str, first_language: str, line: str, destination_language):
    translation = GoogleTranslator(source=first_language, target=destination_language).translate(text=first_word)
    translation_ttl = ", \"" + translation + "\"@" + destination_language
    line = line[:-2] + translation_ttl + line[-3:]

    print(first_word + " -> " + translation)

    return line


if __name__ == "__main__":

    parameter_file_name = ""

    if len(sys.argv) <= 1:
        print('Missing Turtle filename!')
        exit()
    else:
        parameter_file_name = sys.argv[1]

    read_turtle_file(parameter_file_name)
