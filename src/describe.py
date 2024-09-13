import numpy as np
import sys
from csv import DictReader 



def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def read_csv(csv_file:str) -> dict:
    data = {}
    with open(csv_file, 'r')  as file:
        reader = DictReader(file)    
        for row in reader:
            for feature in row:
                if row[feature]
                
def main(argv:list[str]):
    if len(argv) != 2:
        print("Invalid arguments")
        exit(1)
    read_csv(argv[1])
    




if __name__ == '__main__':
    main(sys.argv)
