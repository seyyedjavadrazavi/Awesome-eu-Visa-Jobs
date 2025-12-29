# 🤝 How to Contribute

First off, thanks for taking the time to contribute! This project relies on community support to keep the list of visa-sponsoring companies up to date.

## 🚀 How to Add a New Company

You don't need to be a developer to contribute. Just follow these steps:

1.  **Fork** this repository to your own GitHub account.
2.  Open the file `data/companies.json`.
3.  Add a new entry inside the main list `[ ... ]`.
4.  Use the **template** below to ensure the format is correct.
5.  **Commit** your changes and submit a **Pull Request**.

> ⚠️ **IMPORTANT:** Do NOT edit `README.md` or `index.html` manually. The system updates them automatically when you change the JSON file.

---

## 📋 JSON Data Template

Please copy this object and fill in the details. **Remove the comments** (lines starting with `//`) before saving, as standard JSON does not support them.

```json
{
  "name": "Company Name",
  "careers_url": "https://company.com/careers",
  "locations": [
    {
      "country": "Germany",
      "city": "Berlin",
      "is_hq": true
    },
    {
      "country": "Netherlands",
      "city": "Amsterdam",
      "is_hq": false
    }
  ],
  "visa_sponsorship": "YES",
  "remote_policy": "HYBRID",
  "tech_stack": [
    "TypeScript",
    "React",
    "Go"
  ],
  "hiring_status": "ACTIVE",
  "meta_data": {
    "relocation_package": true,
    "language": "English"
  }
}