# 🤝 How to Contribute

First off, thanks for taking the time to contribute! This project relies on community support to keep the list of visa-sponsoring companies up to date.

## 🚀 How to Add a New Company

You don't need to be a developer to contribute. Just follow these steps:

1.  **Fork** this repository to your own GitHub account.
2.  Open the file `data/companies.json`.
3.  Add a new entry inside the main list `[ ... ]`.
4.  Use the **template** below to ensure the format is correct.
5.  **Commit** your changes and submit a **Pull Request**.

> ⚠️ **IMPORTANT:** Do NOT edit `README.md` manually. The system updates it automatically.

---

## 📋 JSON Data Template

Please copy this object and fill in the details. **Remove the comments** before saving.

```json
{
  "name": "Company Name",
  "careers_url": "https://company.com/careers",
  "locations": [
    {
      "country": "Germany",
      "city": "Berlin",
      "is_hq": true
    }
  ],
  "visa_sponsorship": "YES",
  "remote_policy": "HYBRID",
  "tech_stack": [
    "TypeScript",
    "React"
  ],
  "hiring_status": "ACTIVE",
  "last_updated": "2025-01-01", 
  "meta_data": {
    "relocation_package": true,
    "language": "English"
  }
}
```

## 📝 Field Guidelines

| Field | Type | Accepted Values / Notes |
| :--- | :--- | :--- |
| `name` | String | The official name of the company. |
| `careers_url` | String | Direct link to the jobs/careers page. |
| `locations` | Array | List of office locations. Set `"is_hq": true` for the headquarters. |
| `visa_sponsorship` | String | `YES`, `NO`, `SENIOR_ONLY` |
| `remote_policy` | String | `GLOBAL`, `EU_ONLY`, `HYBRID`, `ON_SITE` |
| `tech_stack` | Array | Main technologies used. |
| `last_updated` | String | Format: `YYYY-MM-DD` (Example: "2025-12-29") |
| `hiring_status` | String | `ACTIVE`, `FREEZE` |
| `meta_data` | Object | `relocation_package`: true/false <br> `language`: Main working language. |

Thank you for helping job seekers! 🇪🇺💙
