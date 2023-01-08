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
    print("Checking folder system integrity...")
    if os.path.exists("input.txt"):
        print("\nInput.txt found!")
    else:
        input_txt_file_generator() # Generating txt file if not present in the folder system
        print("input.txt not found!\ninput.txt is generated.\nEdit the contents of input.txt to your requirments and run generator.py again.")
        quit()

def generated_folder_system_report(toal_folders, total_level):
    """
    Prints a report on the generated folder system to the terminal.

    Parameters:
        total_folders (int): The total number of folders generated in the system.
        total_levels (int): The total number of levels in the generated folder system.
        
    Returns:
        None
    """

    report_text = f"\n- Total numbers of folders generated: {toal_folders}\n- Total numbers of levels generated: {total_level}"
    print(report_text)

def multi_level_folder_generator(txt_file_path):
    """
    This function parses a text file into a multi-layer folder system.
    
    Parameters:
        txt_file_path (str): The path to the text file to be parsed. The file should contain a list of folder names, each indented by a certain number of tabs to indicate the folder's level in the hierarchy.
    
    Returns:
        tuple: A tuple containing two integers, the maximum level of the generated folder system, and the total number of folders in the system.
    """

    # Initialize variables to store the maximum level of the generated folder system and the total number of folders in the system
    max_level_of_generated_folder_system = 0
    total_folders_in_generated_folder_system = 1 # Keep 1 because root folder is considered as the first level

    def make_folder_and_chdir_into_it(name):
        '''
        Creates a folder, gives a report on the creation of each folder, and changes the current directory into it.
        
        Parameters:
            name (str): The name of the folder to be created.
            
        Returns:
            None
        '''
        try:
            os.mkdir(name)
        except:
            print(f"'{name}' is not a valid name for a folder! Change it in the 'input.txt' file.")
        else:
            print(f"Folder '{folder_name}' created successfully! ")
            os.chdir(f"./{name}")

    # Get the directory of the current script file
    script_dir = os.path.dirname(os.path.realpath(__file__))

    with open(txt_file_path, "r") as txt:

        # Initialize variables to store the previous level and the path to the current folder
        previous_level = 0
        path = []

        for counter, line in enumerate(txt):

            if counter == 0: # When root folder is created
                level = len(re.findall(r"\t", line))
                previous_level = level
                folder_name = line.strip()
                path.append(folder_name)

                if os.path.exists(folder_name): # If a folder with root name already exists then inform user and terminalte program
                    print(f"\nA folder with the root name '{folder_name}' already exists. Either delete it or change the root folder name in 'input.txt' file.")
                    quit()

                make_folder_and_chdir_into_it(folder_name)
                total_folders_in_generated_folder_system += 1

            elif counter > 0: # When folder branches from the root folder into multi layer sub-folders
                level = len(re.findall(r"\t", line))
                if level > max_level_of_generated_folder_system:
                    max_level_of_generated_folder_system = level
                folder_name = line.strip()

                if level > previous_level:
                    # If the level of the current folder is greater than the previous level, create a subfolder and change the current directory into it
                    previous_level = level
                    path.append(folder_name)
                    make_folder_and_chdir_into_it(folder_name)
                    total_folders_in_generated_folder_system += 1

                elif level == previous_level:
                    # If the level of the current folder is equals to the previous level, change the current directory a level backwards. Then, create a subfolder and change the current directory into it
                    os.chdir("../")
                    make_folder_and_chdir_into_it(folder_name)
                    total_folders_in_generated_folder_system += 1

                elif level < previous_level:
                    # If the level of the current folder is less than the previous level, change the current directory to the root directory and then traverse to the specified path by changing the current directory into each folder in the path, before creating the current folder as a subfolder and changing the current directory into it
                    path = path[:level]
                    os.chdir(script_dir)
                    for folder in path:
                        os.chdir(folder)
                    previous_level = level
                    path.append(folder_name)
                    make_folder_and_chdir_into_it(folder_name)
                    total_folders_in_generated_folder_system += 1

    return max_level_of_generated_folder_system, total_folders_in_generated_folder_system

def main():
    introduction_text = "python-multi-level-folder-generator\n\nThis script generates a multi-level folder system based on the contents of a text file. This script can be useful for creating and maintaining a large and complex folder system with multiple levels.\n\nGithub repo link: https://github.com/AbhashChamlingRai/python-multi-level-folder-generator\nCreated by: Abhash Rai"
    print("\n-----------------------------------\n") # Adding this to make the output more readable
    print(introduction_text)
    print("\n-----------------------------------\n") # Adding this to make the output more readable
    print()
    input_txt_file_checker()
    total_folders, total_folder_levels = multi_level_folder_generator("./input.txt")
    generated_folder_system_report(total_folders, total_folder_levels)
    print()

if __name__ == "__main__":
    main()