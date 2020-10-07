import re
import sys;


def parseData(data):
    roll1 = re.findall(r'[0-9][0-9][lL][_-][0-9][0-9][0-9][0-9]', data)
    roll2 = re.findall(r'[0-9][0-9][lL][0-9][0-9][0-9][0-9]', data)
    roll3 = re.findall(r'[lL][0-9][0-9][_-][0-9][0-9][0-9][0-9]', data)
    roll4 = re.findall(r'[lL][0-9][0-9][0-9][0-9][0-9][0-9]', data)
    return roll1 + roll2 + roll3 + roll4


def main():
    input_file = ""
    output_file = ""
    if len(sys.arg <= 1):
        input_file = input("Enter Input File : ")
        output_file = input("Enter Output File : ")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    err = False
    try:
        file_in = open(input_file, "r")
    except:
        print("Something went wrong with input file")
        err = True
    try:
        file_out = open(output_file, "w")
    except:
        print("Something went wrong with output file")
        err = True
    if err:
        return
    a = file_in.read()
    array = parseData(a)
    array.sort()
    for roll in array:
        file_out.write(roll + '\n')


if __name__ == "__main__":
    main()
