import numpy as np
import sys
from csv import DictReader 


MAX_ALINMENT = 0


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def read_csv(csv_file:str) -> dict:
    global MAX_ALINMENT
    data = {}
    feature_not_num = set()
    with open(csv_file, 'r')  as file:
        reader = DictReader(file)
        for row in reader:
            for feature in row:
                MAX_ALINMENT = max(MAX_ALINMENT, len(feature))
                if feature in feature_not_num:
                    continue
                try:
                    if len(row[feature]) == 0:
                        continue
                    float(row[feature])
                    MAX_ALINMENT = max(MAX_ALINMENT, len(row[feature]))
                except:
                    feature_not_num.add(feature)
                    continue
                value = np.float64(row[feature])
                data[feature] = np.append(data.get(feature, np.empty(1)) , np.array([value]))


    return data


def printMesurement(m,  vect):
    if m == 'Count':
        print(str(vect.size).ljust(MAX_ALINMENT), end='')




def printData(data):
    list_of_features = []
    mesurements = ['Count', 'Mean', 'Std', 'Min', '25%' , '50%', '75%', 'Max']

    for i, feature in enumerate(data):
        if len(list_of_features) == 4 or len(data) == i + 1:
            print(MAX_ALINMENT * ' ', end='')
            for f in list_of_features:
                print(f.ljust(MAX_ALINMENT) + '  ', end='')
            print('')
            for m in mesurements:
                print(m.ljust(MAX_ALINMENT) + ' ', end='')

                for f in list_of_features:
                    printMesurement(m, data[f])
                print('')
            print('')
            list_of_features = []
        list_of_features.append(feature)


def main(argv:list[str]):
    if len(argv) != 2:
        print("Invalid arguments")
        exit(1)
    data = read_csv(argv[1])
    printData(data)
    




if __name__ == '__main__':
    main(sys.argv)
