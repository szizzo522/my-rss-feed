# Cyber Intel Aggregator

A lightweight workflow that collects cybersecurity intelligence from multiple RSS feeds and generates a consolidated feed for easier monitoring and research.

Automatically pulls updates from trusted security sources, processes them, and outputs clean RSS feeds that can be consumed by feed readers, dashboards, or threat intelligence platforms.

---

# Features

- Aggregates multiple cybersecurity RSS feeds
- Automatically generates combined feeds
- Runs automatically using GitHub Actions
- Outputs standardized RSS files
- Easy to extend with additional intelligence sources

---

# Repository Structure

```
.github/workflows/   → automation that runs the feed aggregator
generated_feeds/     → output directory where RSS feeds are generated
scripts/             → Python scripts that build the RSS feeds
sources/             → configuration for intelligence sources (feeds.json)
requirements.txt     → Python dependencies
```

---

# How It Works

1. RSS sources are defined in:

```
sources/feeds.json
```

2. The aggregation script collects articles from each source.

3. The script processes and merges the feeds.

4. Clean RSS feeds are generated inside:

```
generated_feeds/
```

5. GitHub Actions runs the process automatically to keep feeds updated.

---

# Installation (Local Development)

Clone the repository:

```bash
git clone https://github.com/szizzo522/cyber-intel-aggregator.git
cd cyber-intel-aggregator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the aggregator:

```bash
python scripts/build_rss.py
```

---

# Adding New Intelligence Sources

Edit the configuration file:

```
sources/feeds.json
```

Add additional RSS feeds to expand coverage.

Example:

```json
{
  "feeds": [
    "https://example.com/rss",
    "https://securitynews.example/rss"
  ]
}
```

---

# Use Cases

This project can be used for:

- cybersecurity news aggregation
- threat intelligence monitoring
- vulnerability tracking
- research feeds
- SOC analyst dashboards

---

# License

This project is released under the MIT License.
