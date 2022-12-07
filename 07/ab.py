import re

dir_sizes = []


class Node:
    def __init__(self, parent, name, size):
        self.parent = parent
        self.name = name
        self.size = size
        self.children = {}

    def get_full_size(self):
        if not self.children:  # file, or empty dir (in both cases, size = 0)
            return self.size
        else:  # non-empty dir
            full_size = sum(child.get_full_size() for child in self.children.values())
            dir_sizes.append(full_size)
            return full_size


root = Node(parent=None, name="/", size=0)

with open("input", "r") as f:
    lines = f.read().splitlines()

for line in lines:
    if ro := re.search(r"^\$ cd (.*)$", line):
        dest = ro.group(1)
        if dest == "..":
            cwd = cwd.parent
        elif dest == "/":
            cwd = root
        else:
            cwd = cwd.children[dest]
    elif ro := re.search(r"^dir (.*)$", line):
        dirname = ro.group(1)
        if dirname in cwd.children.keys():
            continue
        new = Node(parent=cwd, name=dirname, size=0)
        cwd.children[dirname] = new
    elif ro := re.search(r"^(\d+) (.*)$", line):
        filesize = int(ro.group(1))
        filename = ro.group(2)
        if filename in cwd.children.keys():
            continue
        new = Node(parent=cwd, name=filename, size=filesize)
        cwd.children[filename] = new

rootsize = root.get_full_size()
total = 70_000_000
unused = total - rootsize
needed = 30_000_000
tofree = needed - unused

print(sum(ds for ds in dir_sizes if ds <= 100_000))  # part 1
print(min(ds for ds in dir_sizes if ds >= tofree))  # part 2
