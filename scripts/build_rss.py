import json
from datetime import datetime
import os
from xml.sax.saxutils import escape  # <- important for escaping XML chars

# Ensure the folder exists
os.makedirs("generated_feeds", exist_ok=True)

# Load tagged articles
with open("tagged_articles.json") as f:
    articles = json.load(f)

# Start RSS
rss = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Cyber Threat Intel Feed</title>
<link>https://isamuel.dev</link>
<description>Aggregated cybersecurity news</description>
"""

# Build items
for a in articles:
    title = escape(a["title"])
    link = escape(a["link"])
    summary = escape(a["summary"])

    # Convert datetime to RFC 822 format for RSS
    pub_date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    rss += f"""
    <item>
        <title>{title}</title>
        <link>{link}</link>
        <description><![CDATA[{summary}]]></description>
        <pubDate>{pub_date}</pubDate>
    </item>
    """

# Close RSS
rss += "</channel></rss>"

# Write file
with open("generated_feeds/all.xml", "w", encoding="utf-8") as f:
    f.write(rss)
