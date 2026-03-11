import requests
import json
import os

API_KEY = os.environ["OPENROUTER_API_KEY"]

with open("articles.json") as f:
    articles = json.load(f)

tagged = []

for a in articles:

    prompt = f"""
    Categorize this cybersecurity article.

    Return JSON with:
    category (ransomware, vulnerability, malware, threat-intel, general)

    Title: {a['title']}
    Summary: {a['summary']}
    """

    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "anthropic/claude-3-haiku",
            "messages":[{"role":"user","content":prompt}]
        }
    )

    result = r.json()

    a["tag"] = result["choices"][0]["message"]["content"]

    tagged.append(a)

with open("tagged_articles.json","w") as f:
    json.dump(tagged,f)
