#Basic steps:
#1. is it an image?
#2. when was it taken?
#3. rename it

#1a. Scan through 
# use os.listdir
#1b. Make a list of files
#1c. deicde if its an image 
#1d. Add images to new list

#2a. Look in the metadata for the file
#2b. Find metatdata about file creation date

import os
import string
import os.path, time

#1a. & 1b.
def directory_scan (directory):
	files = os.listdir (directory)
	return files

#1c. &1d.
def image_sort (files):
	images = []
	for currentelement in files:
		currentelement2 = string.lower(currentelement)
		end = string.rfind(currentelement, ".")
		if (currentelement2)[end:] == ".gif":
			images.append (currentelement)
		elif (currentelement2)[end:] == ".png":
			images.append (currentelement)
		elif (currentelement2)[end:] == ".jpg":
			images.append (currentelement)
		elif (currentelement2)[end:] == ".jpeg":
			images.append (currentelement)
		elif (currentelement2)[end:] == ".tiff":
			images.append (currentelement)
		elif (currentelement2)[end:] == ".raw":
			images.append (currentelement)
		elif (currentelement2)[end:] == ".bmp":	
			images.append (currentelement)
	return images

#2a. & 2b. & 3.
def find_created (images):
	for currentelement in images:
		end = string.rfind(currentelement, ".")
		full_name = "/home/charles/Pictures (copy)/%s" %currentelement
		new_name = "/home/charles/Pictures (copy)/%s" %time.ctime(os.path.getctime(full_name)) + (currentelement)[end:]
		print full_name
		print new_name
		#os.rename (full_name, new_name)

find_created (image_sort (directory_scan ("/home/charles/Pictures (copy)")))
