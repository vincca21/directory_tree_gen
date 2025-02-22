# cli.py
"""Module provides RP Tree command line interface."""
import argparse
import pathlib
import sys 
from . import __version__
from .rptree import DirectoryTree

def main():
    args = parse_cmd_line_args()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit(1)
    tree = DirectoryTree(root_dir, dir_only=args.dir_only, output_file=args.output_file)
    tree.generate()
    
def parse_cmd_line_args():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="RP Tree, a directory tree generator"
    )
    parser.version = f"RP Tree version {__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR"
    )
    parser.add_argument(
        "-d", "--dir-only",
        action="store_true",
        help="Generate a directory-only tree"
    )
    parser.add_argument(
        "-o", "--output-file",
        metavar="OUTPUT_FILE",
        default=sys.stdout,
        help="Output the tree to a file"
    )
    return parser.parse_args()
