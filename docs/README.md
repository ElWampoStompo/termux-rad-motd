# Termux RAD MOTD

A script to print a custom Message of the Day (MOTD) in Termux. It includes the current date and time, a random quote, a random header, device information, and dynamic elements.

## Features
- Display current date and time
- Show random quotes and headers
- Fetch device information using Termux-API
- Display battery status and storage usage
- Customizable and extendable

## File Structure
.
├── .github
│   └── workflows
│       └── ci.yml
├── docs
│   └── README.md
├── src
│   ├── config.py
│   └── utils.py
├── tests
│   ├── __init__.py
│   └── test_motd.py
├── .gitignore
├── motd.py
├── requirements.txt
└── setup.py

## Installation

### Prerequisites
- Termux
- Python 3.6 or higher

### Steps
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/termux-rad-motd.git
    cd termux-rad-motd
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
Run the script:
```sh
python src/motd.py
```
# Configuration

You can customize the MOTD by editing the config.py file in the src directory. This file contains various settings such as the format of the date and time, the source of random quotes, and more.

There are also various aliases starting with `config` that can be used to access the files in editor.
- `configzsh`: ZSH config file
- `confignvim`: Neovim config file
- `configlazy`: Lazy.nvim config file

## Development

### Running Tests
To run the tests, use the following command:
```sh
pytest
```

### Running CI
This project uses GitHub Actions for continuous integration.
The configuration file is located at .github/workflows/ci.yml.

To run the CI, use the following command:
```sh
bash .github/workflows/ci.yml
```

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgements
Termux
Python
Oh My Zsh
Powerlevel10k
