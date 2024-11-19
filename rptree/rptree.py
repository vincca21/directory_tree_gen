# rptree.py 

"""Module provides RP Tree main module."""

import os
import pathlib
import sys

# Constants for tree drawing
PIPE = "|"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

class DirectoryTree:
    # Initialize the class w/ root_dir passed to it
    def __init__(self, root_dir, dir_only=False, output_file=sys):
        self._output_file = output_file
        self._generator = _TreeGenerator(root_dir, dir_only)
        
    # call the build_tree method of the generator from '_TreeGenerator' class
    def generate(self):
        tree = self._generator.build_tree()
        if self._output_file != sys.stdout:
            # wrap tree in markdown code block
            tree.insert(0, "```")
            tree.append("```")
            self._output_file = open(self._output_file, "w", encoding="utf-8")
        with self._output_file as stream:
            for entry in tree:
                print(entry, file=stream)
        
# _TreeGenerator class -> builds the tree structure
class _TreeGenerator:
    
    # Initialize the class w/ root_dir passed to it
    def __init__(self, root_dir, dir_only=False):
        self.root_dir = pathlib.Path(root_dir)
        self.dir_only = dir_only
        self._tree = [] # list to store the tree structure
        
    # Build the tree structure
    def build_tree(self):
        self._tree_head() # call the _tree_head method
        self._tree_body(self.root_dir)
        return self._tree

    # Recursive method to build the tree structure
    def _tree_head(self):
        self._tree.append(f"{self.root_dir}{os.sep}") # append the root directory to the tree (with separator)
        self._tree.append(PIPE) # append the PIPE to the tree
        
    def _tree_body(self, dir, prefix=""):
        entries = self._prepare_entries(dir) # get the entries of the directory
        entries_count = len(entries) # get the count of entries
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE # set the connector
            if entry.is_dir():
                self._add_directory(entry, index, entries_count, prefix, connector) # add the directory to the tree
            else:
                self._add_file(entry, prefix, connector) # add the file to the tree
    
    def _prepare_entries(self, dir):
        entries = dir.iterdir() # get the entries of the directory
        if self.dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file()) # sort the entries
        return entries                      
    
    # Add the directory to the tree - (note: directory goes to 'dir' in "tree_body" method, bad naming)
    def _add_directory(self, directory, index, entries_count, prefix, connector):
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}") # append the directory to the tree
        # set the prefix for the next level of the tree
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(dir=directory, prefix=prefix)
        self._tree.append(prefix.rstrip())
    
    # Add the file to the tree
    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector} {file.name}")