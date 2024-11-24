###
# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
file_lines=file_name.splitlines()
file_lines.sort()

# Write data to the file
with open(file_name, 'w') as file:
      for item in seven_wonders:
        file.write(f"{item}\n")