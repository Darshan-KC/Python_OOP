# Shutil Module in Python
# Shutil is a python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories. 

import shutil

shutil.copy("_24_shutil_module.py","test.py") # shutil.copy(src,dst)

# This function copies the file located at src to a new location specified by dist. If the destination file already exists, the original file will be overwritten.

shutil.copytree("_9_KBC","test-folder") # shutil.copytree(src,dst)

# This function recursively copies the directory located at src to a new location specified by dst. If the destination already exists, the original directory will be merge with it

shutil.move("_9_KBC/test.txt","test.txt")