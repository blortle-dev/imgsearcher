import pandas as pd
import os
filename = "wecimgs.csv"

def getList():
    return pd.read_csv(filename, header=0)

def main():
    list = getList()
    print(list)

    desiredFoldeur = input("---\n\nEnter path from root to folder to search: ")

    if os.path.isdir(desiredFoldeur):
        foldeur = os.path.dirname(desiredFoldeur)


    else:
        print(f"Unable to find foldeur with path {desiredFoldeur}. Did you get the path to the foldeur from system root?", end="\n\n")
        main()

main()