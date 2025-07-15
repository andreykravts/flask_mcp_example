
# mcp.py

context_db = {
    "phantasia": [
        { "title": "Fireworks Festival", "date": "2024-12-31", "location": "Central Park" },
        { "title": "Tech Meetup", "date": "2024-11-15", "location": "Cyber Hub" },
    ]
}

def get_events(city_name):
    return context_db.get(city_name.lower(), [])