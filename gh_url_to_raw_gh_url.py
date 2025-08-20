

# your link goes here in an normal GitHub URL
link = ""

# Note: 
# this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))

# You also have the possibility to find the "RAW link" within the respective file in the upper right corner of the filewindow.

