import zipfile
import rarfile
import os

__author__ = 'tristanhaffenden'


directory_path = os.path.abspath(
    "{a}\\Downloads\\Music".format(a=os.environ["USERPROFILE"]))
list_of_files = []
unzipped_files_list = []
rarfile.UNRAR_TOOL = "C:/Program Files/WinRAR/WinRAR.exe"

for file_name in os.listdir(directory_path):
    if file_name.endswith(".zip") or file_name.endswith(".rar"):
        list_of_files.append(file_name)

print(list_of_files)

for file in list_of_files:
    original_file_path = os.path.join(directory_path, file)

    if zipfile.is_zipfile(original_file_path) or \
            rarfile.is_rarfile(original_file_path):

        if file[-16:-4] == " (mp3boo.me)":
            formatted_name = file[:-16]
        else:
            formatted_name = file[:-4]

        new_file_path = "{a}\\{b}".format(a=directory_path, b=formatted_name)

        if file[-4:] == ".zip":
            extraction_object = zipfile.ZipFile(original_file_path)

        elif file[-4:] == ".rar":
            extraction_object = rarfile.RarFile(original_file_path)

        extraction_object.extractall(path=new_file_path)
        extraction_object.close()
        print("Extraction Complete:", formatted_name)

        os.remove(original_file_path)

        unzipped_files_list.append(formatted_name)

print('Extraction Process Complete')
print(unzipped_files_list)

