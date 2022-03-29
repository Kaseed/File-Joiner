from sys import argv, exit
import os
import pandas as pd


def main(arg):
    if len(arg) != 4:
        print("Wrong amount of arguments!")
        exit(1)

    if arg[0][-4:] != '.csv' or not os.path.exists(arg[0]):
        print(f"CSV file {arg[0]} not exist")
        exit(1)

    if arg[1][-4:] != '.csv' or not os.path.exists(arg[1]):
        print(f"CSV file {arg[1]} not exist")
        exit(1)

    csv1 = pd.read_csv(arg[0]).columns.values
    csv2 = pd.read_csv(arg[1]).columns.values

    if arg[2] not in csv1 or arg[2] not in csv2:
        print("Column doesn't exist")
        exit(1)

    if arg[3] == "inner":
        print("Inner function")
        end_csv = inner_join(arg[0], arg[1], arg[2])
        print(end_csv)
    elif arg[3] == "left":
        print("Left join function")
        end_csv = left_join(arg[0], arg[1], arg[2])
        print(end_csv)
    elif arg[3] == "right":
        print("Right join function")
        end_csv = left_join(arg[1], arg[0], arg[2])
        print(end_csv)
    else:
        print("Wrong join type")
        exit(1)


def inner_join(path1, path2, column):
    inner_csv = left_join(path1, path2, column)
    csv2 = pd.read_csv(path2)
    headers = list(csv2.columns.values)
    headers.remove(column)
    rows_to_delete = []

    for index, row in inner_csv.iterrows():
        if all(v is None for v in list(row[headers])):
            rows_to_delete.append(index)

    inner_csv = inner_csv.drop(rows_to_delete)
    inner_csv = inner_csv.reset_index(drop=True)

    return inner_csv


def left_join(path1, path2, column):
    csv1 = pd.read_csv(path1)
    csv2 = pd.read_csv(path2)
    headers = list(csv2.columns.values)
    headers.remove(column)
    csv1[headers] = None

    join_frame = pd.DataFrame(columns=csv1.columns.values)

    for index, row in csv1.iterrows():
        join = csv2.loc[csv2[column] == row[column]]

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

    for index, row in join_frame.iterrows():
        csv1.loc[len(csv1.index)] = list(row)

    return csv1


if __name__ == "__main__":
    print(argv)
    main(argv[1:])

    # temparg = ['temp', 'temp1.csv', 'temp2.csv', 'id', 'right']
    # main(temparg[1:])
