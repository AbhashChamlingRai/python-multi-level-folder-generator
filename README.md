# python-multi-level-folder-generator
This script takes a **text file as input** and uses the information in the file to create a folder structure with a root folder and several levels of nested subfolders. The structure of the folders is determined by the contents of the text file.

For example, the text file might contain a list of folder names, with each name indented by a certain number of tabs. The script would interpret the indentation as the folder's level in the hierarchy, with each level being a subfolder of the previous level.

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