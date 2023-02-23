# PEEK

A basic program that "takes a peek" at the contents of the specified directory.

Nothing serious for now.

Peek requires the tabulate and rich libraries.

## USAGE

```
usage: peek [-h] -p PATH [--list] [--list-dir] [--list-file]

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path you wish to explore. (default: None)
  --list                list ALL files & directories under the requested path. (default: False)
  --list-dir            list ALL directories under the requested path. (default: False)
  --list-file           list ALL files under the requested path. (default: False)
```

Will show the user all files and directories.

```
src python peek -p [DIR] --list 
```

Will show the user directories only.

```
src python peek -p [DIR] --list-dir 
```

Will show the user files only.

```
src python peek -p [DIR] --list-file
```