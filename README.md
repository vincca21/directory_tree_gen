# RP Tree

RP Tree is a CLI tool to visualize directory structures. Display your directories and subdirectories in a tree format.

## Features

- Generate a complete directory tree from any root directory.
- Option to create a directory-only tree.
- Output the tree to a file or standard output.

## Usage

Run RP Tree with:

```sh
python tree.py [OPTIONS] ROOT_DIR
```

### Options

- `-d`, `--dir-only`: Create a directory-only tree.
- `-o`, `--output-file`: Save the tree to a file.
- `-v`, `--version`: Display the RP Tree version.

### Examples

Generate a full tree from the current directory:

```sh
python tree.py
```

Generate a directory-only tree and save it to a file:

```sh
python tree.py -d -o tree.txt
```

## Future Enhancements

- **Sorting**: Options to sort directories and files.
- **Icons**: Add icons for different file types and directories.
- **Customization**: Customize tree structure (e.g., connectors).
- **File Filtering**: Include/exclude specific file types.
- **Improved Output**: Better readability and formatting.
- **Interactive Mode**: Navigate the tree interactively.
- **Export Formats**: Export tree to formats like JSON, XML.


### Credit/Source
- Credit to the guide used to inspire the base project w/ code snippets: https://realpython.com/directory-tree-generator-python/
