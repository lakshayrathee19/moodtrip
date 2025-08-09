# mood_detector.py

def detect_mood(user_input):
    mood_keywords = {
        "happy": ["excited", "joyful", "cheerful", "smiling"],
        "sad": ["down", "unhappy", "blue", "crying"],
        "adventurous": ["thrill", "explore", "adventure", "spontaneous"],
        "romantic": ["love", "romantic", "date", "candlelight"],
        "calm": ["relaxed", "calm", "peaceful", "chill"],
    }

    for mood, keywords in mood_keywords.items():
        if any(word in user_input.lower() for word in keywords):
            return mood

    return "neutral"


def recommend_playlist(mood, energy):
    playlists = {
        "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "sad": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "adventurous": "https://open.spotify.com/playlist/37i9dQZF1DWYBO1MoTDhZI",
        "romantic": "https://open.spotify.com/playlist/37i9dQZF1DWXnscMH24yOc",
        "calm": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY",
        "neutral": "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6"
    }

    return playlists.get(mood, playlists["neutral"])


def recommend_outfit(mood, destination_type="city"):
    if destination_type == "beach":
        base = {
            "happy": "Bright shorts, tank top, flip-flops, sunglasses",
            "sad": "Comfy t-shirt, shorts, sandals, sunhat",
            "adventurous": "Swimwear, rashguard, water shoes, beach backpack",
            "romantic": "Flowy dress or linen shirt with loafers, straw hat",
            "calm": "Loose shirt, cotton pants, open sandals, shades",
        }
    elif destination_type == "mountain":
        base = {
            "happy": "Colorful hoodie, trekking pants, hiking boots",
            "sad": "Warm jacket, fleece pants, boots",
            "adventurous": "Thermal wear, windbreaker, gloves, hiking gear",
            "romantic": "Woolen scarf, long coat, snow boots",
            "calm": "Neutral hoodie, joggers, beanie",
        }
    else:  # Default/city
        base = {
            "happy": "Bright t-shirt, jeans, sneakers",
            "sad": "Oversized hoodie, joggers, comfy shoes",
            "adventurous": "Tactical pants, tee, sneakers, backpack",
            "romantic": "Stylish top/shirt, chinos or skirt, accessories",
            "calm": "Neutral tones, soft fabrics, slip-ons",
        }

    return base.get(mood, "Casual, comfortable wear with your favorite touch.")
