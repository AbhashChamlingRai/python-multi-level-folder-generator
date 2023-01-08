import os
import re

def input_txt_file_generator():
    """
    This function generates the 'input.txt' file only if it is declared to be not present in the same folder as the script (generator.py).
    
    Returns:
        None
    """
    text = "root\n\tlevel1_folder1\n\t\tlevel2_folder1\n\t\tlevel2_folder2\n\tlevel1_folder2\n\t\tlevel2_folder3\n\t\t\tlevel3_folder1"
    with open("input.txt", "w") as file:
        file.write(text)

def input_txt_file_checker():
    """
    This function checks if the 'input.txt' file is present in the same folder as the script (generator.py). If the file is not present, the function creates it, then terminates the program.
    
    Returns:
        None
    """
    print("\nChecking folder system integrity...")
    if os.path.exists("input.txt"):
        print("\nInput.txt found!")
    else:
        input_txt_file_generator() # Generating txt file if not present in the folder system
        print("input.txt not found!\ninput.txt is generated.\nEdit the contents of input.txt to your requirments and run generator.py again.")
        quit()

def text_file_parser(txt_file_path):
    """
    This function parses a text file into a Python dictionary that includes the folder hierarchy.
    
    Parameters:
        txt_file_path (str): The path to the text file to be parsed. The file should contain a list of folder names, each indented by a certain number of tabs to indicate the folder's level in the hierarchy.
    
    Returns:
        dict: A dictionary that represents the folder hierarchy as described in the text file. Each key in the dictionary represents a folder and its value is a list of its subfolders.
    
    Example:
        Given the following input in the text file:
        root
            level1_folder1
                level2_folder1
                level2_folder2
            level1_folder2
                level2_folder3
                    level3_folder1
        The function would return the following dictionary:
        {
            'root': [
                {'level1_folder1': ['level2_folder1', 'level2_folder2']},
                {'level1_folder2': {'level2_folder3' : 'level3_folder1'}}
            ]
        }
    """

def multi_level_folder_generator(folder_hierarchy_dictionary):
    """
    This function takes a dictionary representing a folder hierarchy and converts it into a multi-level nested folder structure.
    
    Parameters:
        folder_hierarchy_dictionary (dict): A dictionary that represents the folder hierarchy. Each key in the dictionary represents a folder and its value is a list of its subfolders.
    
    Returns:
        None
    
    Example:
        Given the following input dictionary:
        {
            'root': ['level1_folder1', 'level1_folder2'],
            'level1_folder1': ['level2_folder1', 'level2_folder2'],
            'level1_folder2': {'level2_folder3' : 'level3_folder1'}
        }
        The function would create the following folder structure:
        root
            level1_folder1
                level2_folder1
                level2_folder2
            level1_folder2
                level2_folder3
                    level3_folder1
    """