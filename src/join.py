from sys import argv, exit
import os
import pandas as pd


def main(arg):
    if len(arg) != 4:
        print("Wrong amount of arguments!")
        exit(1)

    if arg[0][-4:] != '.csv' or not os.path.exists(arg[0]):
        print(arg[0])
        print(f"CSV file {arg[0]} not exist")
        exit(1)

    if arg[1][-4:] != '.csv' or not os.path.exists(arg[1]):
        print(arg[1])
        print(f"CSV file {arg[1]} not exist")
        exit(1)

    csv1 = pd.read_csv(arg[0]).columns.values
    csv2 = pd.read_csv(arg[1]).columns.values

    if arg[2] not in csv1 or arg[2] not in csv2:
        print("Column doesn't exist")
        exit(1)

    if arg[3] == "inner":
        print("Inner function")
    #     TODO Inner join function
    elif arg[3] == "left":
        print("Left join function")
    #     TODO Left join function
    elif arg[3] == "right":
        print("Right join function")
    #     TODO right join function
    else:
        print("Wrong join type")
        exit(1)

    print("Good data")

if __name__ == "__main__":
    print(argv)
    main(argv[1:])
