import json
import sys
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(BASE_DIR, 'data', 'companies.json')

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_data():
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format! \n{e}")
        sys.exit(1)

    seen_names = set()
    seen_urls = set()
    has_error = False

    print("🔍 Validating data...")

    for index, company in enumerate(data):
        name = company.get('name', '').strip()
        url = company.get('careers_url', '').strip().lower()
        last_updated = company.get('last_updated', '')

        # Check Duplicates
        if name.lower() in seen_names:
            print(f"❌ Duplicate Name: '{name}'")
            has_error = True
        else:
            seen_names.add(name.lower())

        if url in seen_urls:
            print(f"❌ Duplicate URL: '{name}'")
            has_error = True
        else:
            seen_urls.add(url)
            
        # Check Date Format (YYYY-MM-DD)
        if not validate_date(last_updated):
            print(f"❌ Invalid Date Format for '{name}': {last_updated}. Expected YYYY-MM-DD.")
            has_error = True

    if has_error:
        print("\n💥 Validation FAILED.")
        sys.exit(1)
    else:
        print("\n✅ All checks passed!")
        sys.exit(0)

if __name__ == "__main__":
    validate_data()