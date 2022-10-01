

# your link goes here in an normal GitHub URL
link = ""

# Note: 
# this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))



