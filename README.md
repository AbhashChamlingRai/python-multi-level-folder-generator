# python-multi-level-folder-generator
This script takes a **text file (input.txt) as input** and uses the information in the file to create a folder structure with a root folder and several levels of nested subfolders. The structure of the folders is determined by the contents of the text file.

## Text file format
The text file should contain one folder name per line, with each subfolder being indented by one tab character. The root folder should not be indented.

For example, the text file might contain a list of folder names, with each name indented by a certain number of tabs <span style="color:red">(NOTE: Use only Tabs)</span>. The script would interpret the indentation as the folder's level in the hierarchy, with each level being a subfolder of the previous level.

The script reads the text file line by line and creates a folder for each line. It uses the indentation of the line to determine the folder's level and creates the necessary subfolders to place the folder at the correct level in the hierarchy.

For example, if the text file contained the following lines:

~~~~
root
    level1_folder1
        level2_folder1
        level2_folder2
    level1_folder2
        level2_folder3
            level3_folder1   	
~~~~

- The script would create a root folder and two subfolders inside it, called level1_folder1 and level1_folder2.
- It would then create two more subfolders inside level1_folder1, called level2_folder1 and level2_folder2.
- Finally, it would create a single subfolder called level2_folder3 inside level1_folder2, and a single subfolder called level3_folder1 inside level2_folder3.

# How to Use
## Prerequisites
- You must have Python 3 installed on your system.
- You must have git installed on your system.

## Running the script
1. Clone the repository **(In terminal)**:
~~~~
git clone https://github.com/AbhashChamlingRai/python-multi-level-folder-generator.git
~~~~
2. Edit the file **'input.txt'** according to **Text file format**.
3. Open a terminal or command prompt window and navigate to the directory where the script and text file are located.
4. Run the script using the following command:
~~~~
python generate.py
~~~~
5. The script will use the information in the text file to create the folder structure in the current directory.
