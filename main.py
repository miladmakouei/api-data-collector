
import json
from pathlib import Path

import requests


API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = Path("data") / "users.json"


def fetch_users():
    """Get users from the API."""

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        users = response.json()

        if not isinstance(users, list):
            print("Error: Unexpected API response.")
            return None

        return users

    except requests.RequestException as error:
        print(f"API request failed: {error}")
        return None

    except ValueError:
        print("Error: The API returned invalid JSON.")
        return None


def clean_users(users):
    """Keep useful fields and remove duplicate emails."""

    valid_users = [
        user for user in users
        if isinstance(user, dict)
    ]

    cleaned_users = []
    seen_emails = set()

    for user in valid_users:
        name = str(user.get("name", "")).strip()
        email = str(user.get("email", "")).strip().lower()

        address = user.get("address", {})
        if not isinstance(address, dict):
            address = {}

        city = str(address.get("city", "")).strip()

        if not name or not email:
            continue

        if email in seen_emails:
            continue

        seen_emails.add(email)

        cleaned_users.append({
            "id": user.get("id"),
            "name": name,
            "email": email,
            "city": city
        })

    return cleaned_users


def save_users(users):
    """Save processed users to a JSON file."""

    try:
        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(
                users,
                file,
                ensure_ascii=False,
                indent=4
            )

        print(f"Saved {len(users)} users to {OUTPUT_FILE}")

    except OSError as error:
        print(f"Could not save the file: {error}")


def main():
    print("Starting API Data Collector...")

    users = fetch_users()

    if users is None:
        print("The project stopped because data could not be fetched.")
        return

    cleaned_users = clean_users(users)

    save_users(cleaned_users)

    print("Finished successfully!")


if __name__ == "__main__":
    main()
