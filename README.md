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

Peek installation.

```
git clone https://github.com/mtttech/peek.git

cd peek/src
```

Example program run.

```
src python peek -p /home/mtaylor3121/Dev/black --list
Requesting directory: /home/mtaylor3121/Dev/black

Directory/File Name        UID    GID  Size    Last Modified
-----------------------  -----  -----  ------  ---------------
.coveragerc               1000   1000  106B    01-27 12:52
.flake8                   1000   1000  360B    01-27 12:52
.git                      1000   1000  138B    01-27 12:52
.github                   1000   1000  158B    01-27 12:52
.gitignore                1000   1000  272B    01-27 12:52
.pre-commit-config.yaml   1000   1000  2KB     01-27 12:52
.pre-commit-hooks.yaml    1000   1000  523B    01-27 12:52
.prettierrc.yaml          1000   1000  49B     01-27 12:52
.readthedocs.yaml         1000   1000  220B    01-27 12:52
AUTHORS.md                1000   1000  8KB     01-27 12:52
CHANGES.md                1000   1000  43KB    01-27 12:52
```