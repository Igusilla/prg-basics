###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as fileOrginal:
   content = fileOrginal.read()
   line = content.splitlines()

# write the content to the target file (copy)
with open(target_file, 'w') as fileCopy:
   for line in content:
    fileCopy.write(line)