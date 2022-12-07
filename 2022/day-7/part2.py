def add_to_current_and_parents(paths_to_filesize, current_path, file_size):
    temp_path = current_path
    
    while temp_path:
        paths_to_filesize[temp_path] = paths_to_filesize.get(temp_path, 0) + file_size
        if temp_path.count("/") == 1 and len(temp_path) > 1:
            temp_path = "/"
        else:
            temp_path = "/".join(temp_path.split("/")[:-1])


puzzle_input_list = list()
paths_to_filesize = dict()
paths_to_dirs = dict()
current_path = ""
result = None

with open("input.txt", "r") as puzzle_input:
    
    for line in puzzle_input:
        line = line.strip()
        if line.startswith("$"):
            line = line[2:]
            if line.startswith("cd"):
                line = line[3:]
                if line == "..":
                    if current_path.count("/") == 1:
                        current_path = "/"
                    else:
                        current_path = "/".join(current_path.split("/")[:-1])
                else:
                    if line == "/":
                        current_path = line
                    elif current_path.endswith("/"):
                        current_path += f"{line}"
                    else:
                        current_path += f"/{line}"
                print(current_path)
            else:
                pass
        else:
            # either file size or directory
            file_size_or_dir, name = line.split()
            if file_size_or_dir == "dir":
                pass
            else:
                add_to_current_and_parents(paths_to_filesize, current_path, int(file_size_or_dir))

print(paths_to_filesize)
total_disk_space = 70000000
required_space = 30000000
remaining_disk_space = total_disk_space - paths_to_filesize["/"]
print(remaining_disk_space)
space_to_delete = required_space - remaining_disk_space
print(space_to_delete)

possible_deletions = [path for path in paths_to_filesize if paths_to_filesize[path] >= space_to_delete]
print(possible_deletions)

minimal_space_deletion = paths_to_filesize[possible_deletions[0]]
for possible_deletion in possible_deletions:
    minimal_space_deletion = min(minimal_space_deletion, paths_to_filesize[possible_deletion])

print(minimal_space_deletion)