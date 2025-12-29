import json
import os
import requests

# تنظیم مسیرها
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(BASE_DIR, 'data', 'companies.json')
REPORT_PATH = os.path.join(BASE_DIR, 'broken_links_report.md')

# هدر برای اینکه شبیه مرورگر واقعی باشیم (جلوگیری از مسدودی)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def check_links():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        companies = json.load(f)

    broken_links = []
    print("🔍 Checking links...")

    for company in companies:
        url = company.get('careers_url')
        name = company.get('name')
        
        if not url:
            continue

        try:
            response = requests.get(url, headers=HEADERS, timeout=10, allow_redirects=True)
            
            if response.status_code >= 400:
                print(f"❌ {name}: {response.status_code}")
                broken_links.append(f"| {name} | {url} | {response.status_code} |")
            else:
                print(f"✅ {name}: OK")

        except requests.exceptions.RequestException as e:
            print(f"❌ {name}: Connection Error")
            broken_links.append(f"| {name} | {url} | Connection Error |")

    if broken_links:
        with open(REPORT_PATH, 'w', encoding='utf-8') as f:
            f.write("# 🚨 Dead Links Report\n\n")
            f.write("The following career pages seem to be broken or inaccessible:\n\n")
            f.write("| Company | URL | Status |\n")
            f.write("|---|---|---|\n")
            for line in broken_links:
                f.write(line + "\n")
        print("\n⚠️ Broken links found. Report generated.")
    else:
        if os.path.exists(REPORT_PATH):
            os.remove(REPORT_PATH)
        print("\n✅ All links are healthy.")

if __name__ == "__main__":
    check_links()