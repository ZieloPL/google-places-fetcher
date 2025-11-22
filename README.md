# Google Places Data Fetcher

Part of the **Foodie** project – this module collects and structures restaurant data from external sources (starting with Google Places API) to support the core application database.

Modular tool for fetching structured restaurant data using the Google Places API.  
Designed as a base for the **Foodie** project, with support for validation, pagination, deduplication and clean JSON export. The code is modular and allows easy future extension (e.g., TripAdvisor, Yelp).

---

## ✅ Features

- 📍 Fetch restaurant data from Google Places API  
- 🔁 Pagination support via `next_page_token`  
- 🔎 Detailed place data fetching (`place/details`)  
- ✅ Record validation (required + optional fields)  
- ♻️ Deduplication based on `place_id`  
- 🧾 Structured JSON export  
- 📓 Logging of warnings, errors and flow  
- 🧱 Abstract base class for future sources

---

## 📦 Project Structure

```
scraper/
├── base_scraper.py        # Abstract base class (logging, validation, saving)
├── google_places.py       # Implementation for Google Places API
├── main.py                # Entry point with example query
.env.example               # Example for setting up API key
requirements.txt           # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/google-places-fetcher.git
cd google-places-fetcher
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file based on the provided example:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

## 🧪 Example Usage

```python
from data_fetchers.google_places import GooglePlaces

# Sample query to fetch restaurant data in Krakow
fetcher = GooglePlaces()
fetcher.run("restaurants+in+Krakow")
```

This will create a JSON file like:

```json
[
  {
    "name": "Pizza Garden",
    "address": "Kalwaryjska 24, Krakow",
    "phone": "+48 123 456 789",
    "website": "https://pizzagarden.pl",
    "latitude": 50.043,
    "longitude": 19.942,
    "image": "https://maps.googleapis.com/..."
  }
]
```

---

## 🛠 Future Plans

- [ ] Integrate with Foodie project's PostgreSQL DB  
- [ ] Enable periodic runs (e.g., CRON, Celery beat)  
- [ ] Add support for TripAdvisor and Yelp  
- [ ] Dockerize the project

---

## ⚠️ Notes

- Google Places API returns a maximum of 60 results per query (3 pages, 20 per page)
- `place/details` endpoint may consume additional quota
- `.env` is excluded from version control — make sure to set your key

---

## 📄 License

MIT License — free for personal and commercial use.

---

## 🤝 Contributing

Feel free to fork, open issues, or suggest improvements via pull requests.
