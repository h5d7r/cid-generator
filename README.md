# CID Generator

A simple Python CLI tool that generates random CIDs in this format:

`UP0000-CUSA00000_00-XXXXXXXXXXXXXXX`

It runs in the terminal, asks how many CIDs you want, prints them cleanly, and copies the full result to your clipboard automatically.

## Format

Each CID looks like this:

- `UP` + 4 random digits
- `-`
- `CUSA` + 5 random digits
- `_00-`
- 15 random uppercase letters and digits

Example:

```text
UP4821-CUSA10437_00-7KQ9M2X8B1T4ZRP
```

## Features

- Terminal only
- Clean output
- One CID per line
- Auto copy to clipboard
- Simple and readable code

## Requirements

- Python 3
- `pyperclip`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python cid_generator.py
```

Then enter how many CIDs you want to generate.

## Output

The generated CIDs will:

- show directly in the terminal
- be printed one per line
- be copied to your clipboard automatically

## Notes

If clipboard copy does not work on your system, make sure `pyperclip` is installed correctly and your OS clipboard tools are available.

## Author

**Mr. Velox**  
GitHub: https://github.com/h5d7r
