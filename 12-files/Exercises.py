"""File operations."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip('\n') for line in file]


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    with open(filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w", newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerows(data)

def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    names_order = []
    dates_dict = {}
    towns_dict = {}

    for line in read_file_contents_to_list(dates_filename):
        if ":" in line:
            name, date = line.split(":", 1)
            if name not in names_order:
                names_order.append(name)
            dates_dict[name] = date if date else "-"

    for line in read_file_contents_to_list(towns_filename):
        if ":" in line:
            name, town = line.split(":", 1)
            if name not in names_order:
                names_order.append(name)
            towns_dict[name] = town if town else "-"

    final_data = [["name", "town", "date"]]
    for name in names_order:
        town = towns_dict.get(name, "-")
        date = dates_dict.get(name, "-")
        final_data.append([name, town, date])

    write_csv_file(csv_output_filename, final_data)


if __name__ == '__main__':
    print(read_file_contents("myfile.txt"))
    print(read_file_contents_to_list("myfile.txt"))
    print(read_csv_file("info.txt"))
    write_contents_to_file("newfile.txt", "Hello world")

    # lines = ["This is a line", "This is a second line"]
    # write_lines_to_file("newfile.txt", lines)
    #
    # data = [["name", "age"], ["john", "11"], ["mary", "15"]]
    # write_csv_file("data.csv", data)

    merge_dates_and_towns_into_csv("names_dates.txt", "names_cities.txt", "output.csv")