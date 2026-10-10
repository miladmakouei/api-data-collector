# API Data Collector

A small Python project that fetches user data from a public API, keeps the fields I need, removes duplicate email addresses, and saves the results to a JSON file.

I built this project to practice working with APIs, handling JSON data, and organizing files in Python.

## What it does

- Fetches user records from JSONPlaceholder
- Extracts each user's name, email, city, and ID
- Skips records with missing names or email addresses
- Removes duplicate email addresses
- Saves the cleaned data to `data/users.json`
- Handles common API and file errors

## Requirements

- Python 3
- The `requests` library
- An internet connection

## Installation

Install the required library on Linux Mint or Ubuntu:

```bash
sudo apt update
sudo apt install python3-requests
```

## Run the project

Clone the repository or download the project files, then open a terminal in the project directory and run:

```bash
python3 main.py
```

The program fetches the data and creates the output file automatically.

## Output

The cleaned records are saved in `data/users.json`. Each record contains the following fields:

```json
{
    "id": 1,
    "name": "Leanne Graham",
    "email": "Sincere@april.biz",
    "city": "Gwenborough"
}
```

The actual output depends on the data returned by the API.

## Project structure

```text
api-data-collector/
├── main.py
├── README.md
├── .gitignore
└── data/
    └── users.json
```

The `data` directory and `users.json` file are created when the program runs.

## Notes

This project uses the public JSONPlaceholder API for testing. It does not require an API key, but it does need an internet connection.

The project is intended for learning and can be extended to work with other APIs.

## License

This project is available for personal learning and practice.
