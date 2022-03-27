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
    #     inner_join(arg)
    elif arg[3] == "left":
        print("Left join function")
    #     TODO Left join function
        left_join(arg)
    elif arg[3] == "right":
        print("Right join function")
    #     TODO right join function
        right_join(arg)
    else:
        print("Wrong join type")
        exit(1)

    print("Good data")


def inner_join(arg):
    path1, path2, column, join_type = arg
    csv1 = pd.read_csv(path1)
    csv2 = pd.read_csv(path2)
    print(csv1[column])


def left_join(arg):
    path1, path2, column, join_type = arg
    csv1 = pd.read_csv(path1)
    csv2 = pd.read_csv(path2)
    # print(csv1)
    headers = list(csv2.columns.values)
    headers.remove(column)
    # print(headers)
    # print(type(csv1))
    csv1[headers] = None

    join_frame = pd.DataFrame(columns=csv1.columns.values)

    # print(join_frame)

    # print(csv1)

    for index, row in csv1.iterrows():
        # print(index, row)
        # print(row[column])
        # print(csv2.loc(csv2[column] == 1))
        join = csv2.loc[csv2[column] == row[column]]

        # print(join.shape[0])
        if join.shape[0] == 1:
            for header in headers:
                csv1.at[index, header] = join.iloc[0][header]
        elif join.shape[0] > 1:
            is_add = False
            for i in range(join.shape[0]):
                if not is_add:
                    for header in headers:
                        csv1.at[index, header] = join.iloc[i][header]
                        is_add = True
                else:
                    for header in headers:
                        row[header] = join.iloc[i][header]
                    join_frame.loc[len(join_frame.index)] = list(row)

    # print(join_frame)

    for index, row in join_frame.iterrows():
        csv1.loc[len(csv1.index)] = list(row)

    print(csv1)


def right_join(arg):
    path1, path2, column, join_type = arg
    csv1 = pd.read_csv(path1)
    csv2 = pd.read_csv(path2)

    headers = list(csv1.columns.values)
    headers.remove(column)
    csv2[headers] = None

    join_frame = pd.DataFrame(columns=csv2.columns.values)

    for index, row in csv2.iterrows():
        join = csv1.loc[csv1[column] == row[column]]
        if join.shape[0] == 1:
            for header in headers:
                csv2.at[index, header] = join.iloc[0][header]
        elif join.shape[0] > 1:
            is_add = False
            for i in range(join.shape[0]):
                if not is_add:
                    for header in headers:
                        csv2.at[index, header] = join.iloc[i][header]
                        is_add = True
                else:
                    for header in headers:
                        row[header] = join.iloc[i][header]
                    join_frame.loc[len(join_frame.index)] = list(row)

    for index, row in join_frame.iterrows():
        csv2.loc[len(csv2.index)] = list(row)

    print(csv2)


if __name__ == "__main__":
    # print(argv)
    # main(argv[1:])

    temparg = ['temp', 'temp1.csv', 'temp2.csv', 'id', 'right']
    main(temparg[1:])
