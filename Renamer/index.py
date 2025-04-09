import os

# Get directory where you need to rename file
path = input("Enter the directory where files are located: ")

os.chdir(path)

print("Current Path: " + path)

# List All files in the current directory
files = os.listdir(path)

# Get the common name present in all files
common_name = input("List the common word that all files has: ")

print("Your common word in all files is : "  + common_name)

print("If file name is _tom_jerry_01.jpg")
print("Enter the index where your new file name should start and end. Eg: 0 at index 11 and 1 at index 12 in above case")

# Get the start index
start_index = input("Enter the new filename where the index starts: ")

# Get the end index
end_index = input("Enter the new file name end index: ")

# Get the file extension
temp_file_name = files[0].rfind(".")
extension = files[0][temp_file_name:]

print("Your current file extension is : " + extension)

# Loop over files and rename it
for file_name in files:
    if file_name.__contains__(common_name):
        new_file_name = file_name[int(start_index):int(end_index)] + extension
        os.rename(file_name,new_file_name)

print("Files Renamed")