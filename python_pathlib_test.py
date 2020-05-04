import pathlib
import collections


# print(pathlib.Path.cwd())
# print(pathlib.Path.home())
# path = pathlib.Path.home().joinpath('browser-fav', 'link-pac')
# print(path.parent)

# print(collections.Counter(p.suffix for p in pathlib.Path.home().iterdir()))

# for i in pathlib.Path.cwd().rglob('*.txt'):
#     print(i.name)


def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')
tree(pathlib.Path.cwd())