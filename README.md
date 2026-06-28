# Unfolder

Simple Python tool to flatten a folder structure. It simply moves every file from all subfolders into the current directory (where the script is located).

## Features

- Recursively scans all subfolders and moves every file to the script's directory.
- Prevents overwriting by automatically renaming duplicate files.
- Leaves the folder structure intact (empty folders are not removed).

## Example

### Before

```
Project/
│
├── move_files.py
├── Folder1/
│   ├── image.jpg
│   └── notes.txt
├── Folder2/
│   ├── video.mp4
│   └── image.jpg
└── Folder3/
    └── file.zip
```

### After

```
Project/
│
├── move_files.py
├── image.jpg
├── image_1.jpg
├── notes.txt
├── video.mp4
├── file.zip
├── Folder1/
├── Folder2/
└── Folder3/
```

## Usage

1.- Place the script inside the directory you want to flatten.
2.- Run:

```bash
python main.py
```

All files from subdirectories will be moved to the current directory.

## Duplicate filenames

If multiple files share the same name, they are renamed automatically:

```
photo.jpg
photo_1.jpg
photo_2.jpg
...
```

No files are overwritten.

> [!WARNING]
> Be **CAREFUL** with **WHERE** you run this script. I'm not responsible for any damage or misuse resulting from its use.

## Requirements

- Python 3.6+
- No external dependencies.
