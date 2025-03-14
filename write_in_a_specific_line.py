line_number = 3  # Line to modify (1-based index)
new_text = "This is the new content for line 3\n"


with open("file.txt", 'r+') as file:
    lines = file.readlines()
if 0 <= line_number - 1 <len(lines):
    lines[line_number - 1] = ''
with open("file.txt", 'w') as file:
    file.writelines(lines)