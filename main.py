import pandas as pd
import os
import shutil

def getInput(prompt = ""):
    return input(f"{prompt}\n> ")

def getList(filename):
    return pd.read_csv(filename, header=0)


def main():
    filename = getInput("Enter the path to the CSV file from root. Ensure it follows the proper formatting.")
    list = getList(filename)
    print(list)

    desiredFoldeur = getInput("---\n\nEnter path from root to the directory to search.")

    if os.path.isdir(desiredFoldeur):
        print(f"Directory {desiredFoldeur} found.")
        outputFoldeurPath = getInput("Where would you like the images to be output? Enter a folder path from root. If the path does not exist, a folder will be created there.")

        if not os.path.exists(outputFoldeurPath):
            os.makedirs(outputFoldeurPath)
            print(f"Directory '{outputFoldeurPath}' has been created.")
        else:
            print(f"Directory '{outputFoldeurPath}' already exists, continuing...")

        # Check for duplicate image IDs in the dataframe
        duplicate_check = list['IMG ID'].duplicated(keep='first')
        duplicates = list[duplicate_check]['IMG ID'].tolist()
        if duplicates:
            print(f"Found {len(duplicates)} duplicate image IDs: {', '.join(duplicates)}")
            print("Only the first occurrence of each duplicate will be processed.")

        # Get unique image IDs to process
        unique_list = list.drop_duplicates(subset=['IMG ID'])
        total_files = len(unique_list)
        processed_files = 0

        for index, row in unique_list.iterrows():
            # This function iterates through the items in the pandas dataframe, locates the file in the input foldeur, and copies it into the destination folder.
            file_name = row['IMG ID']
            source_path = os.path.join(desiredFoldeur, file_name)
            destination_path = os.path.join(outputFoldeurPath, file_name)

            print(f"Finding {file_name}")

            if os.path.exists(source_path):
                shutil.copy2(source_path, destination_path)
                processed_files += 1
                percent_done = round((processed_files / total_files) * 100, 2)
                print(f"Copied {file_name} to {destination_path} ({processed_files}/{total_files} complete, {percent_done}% done)")
            else:
                print(f"File {file_name} not found in {desiredFoldeur}")

    else:
        print(f"Unable to find foldeur with path {desiredFoldeur}. Did you get the path to the foldeur from system root?", end="\n\n")
        main()

main()
