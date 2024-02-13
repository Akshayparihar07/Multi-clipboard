# MultiClipboard

**Author:** [Akshay Parihar](https://github.com/Akshayparihar07)

## Description
MultiClipboard is a simple Python command-line utility that allows users to save multiple pieces of text to their clipboard under unique keys. This tool is particularly useful for storing frequently used text snippets for quick access.

## Features
- Save text to clipboard under a custom key
- Copy text from clipboard using a saved key
- List all saved keys and corresponding text snippets
- Persistent storage of saved data using JSON format

## Dependencies
- Python 3.x
- `clipboard` library (to interact with the system clipboard)
- `json` library (for data serialization)
- `time` library (for adding delays)
- `sys` library (for accessing command-line arguments)

## Installation
1. Clone or download the repository.
2. Make sure you have Python 3.x installed on your system.
3. Install the required libraries using pip:
   ```
   pip install clipboard
   ```
4. Run the `main.py` file using Python:
   ```
   python main.py [command]
   ```

## Usage
MultiClipboard supports the following commands:
- **save**: Save text to clipboard under a custom key.
- **copy** or **load**: Copy text from clipboard using a saved key.
- **list**: List all saved keys and corresponding text snippets.

When executing the script, provide one of the above commands as an argument.

### Example Usage:
1. **Save Text:**
   ```
   python main.py save
   ```
   Enter a key and the text will be saved to your clipboard under that key.

2. **Copy Text:**
   ```
   python main.py copy
   ```
   Enter the key of the text you want to copy, and it will be copied to your clipboard.

3. **List Saved Items:**
   ```
   python main.py list
   ```
   Displays a list of all saved keys and corresponding text snippets.

## Persistence
Saved data is stored in a JSON file named `clipboard.json`. This file will be created in the same directory as the script.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgments
- This project was inspired by the need for a simple, command-line clipboard manager.
- Special thanks to the developers of the `clipboard` library for providing easy clipboard access in Python.
