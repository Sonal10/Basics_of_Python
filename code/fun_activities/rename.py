import os

def rename_files():
    # get names from the files
    file_list = os.listdir(r"C:\Users\Sonal Somani\Downloads\prank\prank")
    print(file_list)
    Current_dir=os.getcwd()
    print(Current_dir)
    os.chdir(r"C:\Users\Sonal Somani\Downloads\prank\prank")
    # for each file, rename the filename
    
    for filename in file_list:
        print("Original file name is: "+filename)
        os.rename(filename,filename.translate(None, "0123456789"))
        print("New file name is : "+filename.translate(None, "0123456789"))

                         
rename_files()
