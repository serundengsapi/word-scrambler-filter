# Word Scrambler Guard

## Description
**Word Scrambler Guard** is a Python tool designed to help prevent the use of offensive or unwanted words across various platforms. Whether you're managing a live stream, community forum, or chat app, this tool can scramble input keywords into multiple variations, making it easy to block different forms of restricted words. By mixing characters and adding random spaces, it helps ensure that no version of a banned word slips through. It's customizable and easy to use, making it perfect for anyone who needs to maintain a safe and moderated environment.

## Features
- Scrambles words by replacing characters with symbols (e.g., "a" becomes "4", "o" becomes "0").
- Randomly inserts spaces between characters to generate even more variations.
- Fully customizable with user-inputted words.

## Requirements
- Python 3.x
- `pyfiglet` module for generating ASCII text

## How to Install Python
If you don't already have Python installed, follow these steps:

1. Download Python from the official website: [Python.org](https://www.python.org/downloads/)
2. Install Python by following the instructions for your operating system.
3. During installation, make sure to check the option **Add Python to PATH** to use it in the command line easily.
4. Verify the installation by running the following command in your terminal or command prompt:
   ```bash
   python --version

## How to Run the Tool
1. Clone this repo with command `git clone https://github.com/serundengsapi/word-scrambler-filter.git` or you can download this repo.
2. Open a terminal or command prompt in the directory where the script is saved
3. Run the following command to install `pyfiglet`:
- Windows

   ```bash
   python3 pip install -m pyfiglet
   ```
- Linux

  ```bash
  pip3 install pyfiglet
  ```
3. The tool will display the ASCII art branding and ask for user input to generate variations of a word. Follow the prompts to input your word and specify how many variations you want.

## Output

![image](https://github.com/user-attachments/assets/6a61c97f-db02-47f2-b735-a202583cb646)
