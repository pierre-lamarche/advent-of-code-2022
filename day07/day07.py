import re

input = "/home/pierre/Documents/codes/advent of code/advent-of-code-2022/day07/input.txt"

with open(input, mode='r') as f:
    terminal_outputs = f.read().split('\n')

directories = dict()
list_dir = False
dir = ''

for term in terminal_outputs:
    if term == '$ cd ..':
        dir = '/'.join(dir.split('/')[:-1])
    cd_cmd = re.match(r'\$ cd ([^\.]+)$', term)
    if cd_cmd:
        list_dir = False
        dir += '/' + cd_cmd.group(1)
        pass
    if term == '$ ls':
        list_dir = True
        directories[dir] = {'files': {}, 'directories': []}
        pass
    if list_dir:
        ls_file = re.match(r'(\d+) (.+)', term)
        ls_dir = re.match(r'dir (.+)', term)
        if ls_file:
            directories[dir]['files'][ls_file.group(2)] = int(ls_file.group(1))
        elif ls_dir:
            directories[dir]['directories'] += [ls_dir.group(1)]
        pass

directories = {re.sub(r'/+', '/', k): v for k, v in directories.items()}

def compute_size_dir(dir, dict_directories):
    size = 0
    if len(dict_directories[dir]['directories']) > 0:
        size += sum([compute_size_dir(re.sub(r'/+', '/', dir + "/" + d), dict_directories) for d in dict_directories[dir]['directories']])
    if len(dict_directories[dir]['files']) > 0:
        size += sum([s for s in dict_directories[dir]['files'].values()])
    return size

size_directories = {k: compute_size_dir(k, directories) for k in directories.keys()}

sum([v for v in size_directories.values() if v <= 100000])

space_to_free = (size_directories['/'] + 30000000) - 70000000
min([v for v in size_directories.values() if v >= space_to_free])