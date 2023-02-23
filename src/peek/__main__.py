from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import datetime
import errno
import os
from pathlib import Path

from rich.console import Console
from tabulate import tabulate


def create_parser():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-p", "--path", help="path you wish to explore.", required=True, type=str
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="list ALL files & directories under the requested path.",
    )
    parser.add_argument(
        "--list-dir",
        action="store_true",
        help="list ALL directories under the requested path.",
    )
    parser.add_argument(
        "--list-file",
        action="store_true",
        help="list ALL files under the requested path. ",
    )
    return parser


def get_file_info(path):
    def calculate_size(file_size: float):
        suffix = "B"
        # KB
        if file_size > 1024:
            file_size = file_size / 1024
            suffix = "KB"
        # MB
        if file_size > 1024:
            file_size = file_size / 1024
            suffix = "MB"
        # GB
        if file_size > 1024:
            file_size = file_size / 1024
            suffix = "GB"
        # TB
        if file_size > 1024:
            file_size = file_size / 1024
            suffix = "TB"

        return f"{round(file_size)}{suffix}"

    file_info = os.stat(path)
    meta_data = [
        os.path.basename(path),
        file_info.st_uid,
        file_info.st_gid,
        calculate_size(file_info.st_size),
        datetime.datetime.fromtimestamp(file_info.st_mtime).strftime("%m-%d %H:%M"),
    ]
    return meta_data


def main():
    parser = create_parser()
    args = parser.parse_args()
    console = Console()
    console.print(f"[bold green]Requesting directory:[/bold green] [underline]{args.path}")
    p = Path(args.path)

    try:
        if not p.exists():
            raise FileNotFoundError
    except FileNotFoundError:
        console.print("[red]Sorry, the requested location doesn't exist.")
        exit(1)

    try:
        open(args.path)
    except IOError as ie:
        try:
            if ie.errno == errno.EACCES:
                raise PermissionError("Sorry, I can't read from this directory.")
        except PermissionError as pe:
            console.print(f"[red]{pe}")
            exit(1)

    path_list = [x for x in p.iterdir()]
    results_table = list()

    if args.list:
        pass
    elif args.list_dir:
        path_list = [f for f in path_list if f.is_dir()]
    elif args.list_file:
        path_list = [f for f in path_list if f.is_file()]

    for path in path_list:
        results_table.append(get_file_info(path))
    results_table.sort()

    print("")
    table = tabulate(
        results_table,
        headers=[
            "Directory/File Name",
            "UID",
            "GID",
            "Size",
            "Last Modified",
        ],
    )
    console.print(f"[green]{table}")


if __name__ == "__main__":
    main()
