def add_to_current_and_parents(paths_to_filesize, current_path, file_size):
    temp_path = current_path

    while temp_path:
        paths_to_filesize[temp_path] = paths_to_filesize.get(temp_path, 0) + file_size
        if len(temp_path) == 2:
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
                    if len(current_path) == 2:
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
            else:
                pass
        else:
            # either file size or directory
            file_size_or_dir, name = line.split()
            if file_size_or_dir == "dir":
                pass
            else:
                add_to_current_and_parents(
                    paths_to_filesize, current_path, int(file_size_or_dir)
                )

result = sum(
    [filesize for _, filesize in paths_to_filesize.items() if filesize <= 100000]
)
print(result)
