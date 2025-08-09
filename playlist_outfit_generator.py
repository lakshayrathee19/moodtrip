def generate_playlist(mood_category, energy_level):
    playlists = {
        "relaxed": [
            ("Lo-Fi Chill Beats", "https://open.spotify.com/playlist/37i9dQZF1DX3PIPIT6lEg5"),
            ("Sunset Acoustic", "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj"),
            ("Cafe Jazz Vibes", "https://open.spotify.com/playlist/37i9dQZF1DX1s9knjP51Oa")
        ],
        "romantic": [
            ("Indie Love Vibes", "https://open.spotify.com/playlist/37i9dQZF1DWXq91oLsHZvy"),
            ("Late Night Romance", "https://open.spotify.com/playlist/37i9dQZF1DXcCnTAt8CfNe"),
            ("Dreamy Bollywood Love", "https://open.spotify.com/playlist/37i9dQZF1DX1tyCD9QhIWF")
        ],
        "adventurous": [
            ("Wanderlust Drive", "https://open.spotify.com/playlist/37i9dQZF1DX4E3UdUs7fUx"),
            ("Mountain Trails", "https://open.spotify.com/playlist/37i9dQZF1DWV3CigBsy3wZ"),
            ("Indie Travel Mix", "https://open.spotify.com/playlist/37i9dQZF1DWVY9d0FQIDAo")
        ],
        "party": {
            "high": [
                ("EDM Festival Bangers", "https://open.spotify.com/playlist/37i9dQZF1DX4dyzvuaRJ0n"),
                ("Bollywood Banger Nights", "https://open.spotify.com/playlist/37i9dQZF1DXaYUxGZU7vnR"),
                ("Afterparty Vibes", "https://open.spotify.com/playlist/37i9dQZF1DX8xfQHE5pGur")
            ],
            "medium": [
                ("Feel Good Friday", "https://open.spotify.com/playlist/37i9dQZF1DXdxcBWuJkbcy"),
                ("Urban Chill Party", "https://open.spotify.com/playlist/37i9dQZF1DWVlLVXKTOAYa"),
                ("Tropical House Sunset", "https://open.spotify.com/playlist/37i9dQZF1DX9uKNf5jGX6m")
            ],
            "low": [
                ("Chill Night House", "https://open.spotify.com/playlist/37i9dQZF1DXb8e4TqyaXnT"),
                ("Laidback Lounge", "https://open.spotify.com/playlist/37i9dQZF1DWUcpsTLQUV0y"),
                ("Slow Vibes", "https://open.spotify.com/playlist/37i9dQZF1DWYxwmBaMqxsl")
            ]
        },
        "default": [
            ("Eclectic Explorer", "https://open.spotify.com/playlist/37i9dQZF1DX3Fzl4v4w9Zp"),
            ("Mood Blender", "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U"),
            ("Morning Chill Boost", "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd")
        ]
    }

    if mood_category == "party":
        return playlists["party"].get(energy_level, playlists["party"]["medium"])
    return playlists.get(mood_category, playlists["default"])


def recommend_outfit(mood_category, destination_type, weather):
    base_outfit = {
        "relaxed": "Oversized cotton shirt, linen trousers, sliders",
        "romantic": "Soft pastel dress or crisp white shirt with tailored pants",
        "adventurous": "Dri-fit T-shirt, cargo pants, hiking boots",
        "party": "Statement jacket, dark jeans, stylish sneakers or a sleek dress",
    }

    extras_by_destination = {
        "beach": " + sunglasses, straw hat, and flip-flops",
        "mountain": " + fleece jacket, thermal layers, and gloves",
        "city": " + crossbody bag and white sneakers",
        "desert": " + lightweight scarf and UV-protective sunglasses"
    }

    extras_by_weather = {
        "cold": " + a puffer coat or layered hoodie",
        "hot": " + a cap and portable water bottle",
        "rainy": " + a waterproof windbreaker or umbrella"
    }

    outfit = base_outfit.get(mood_category, "Comfy travel wear")
    outfit += extras_by_destination.get(destination_type, "")
    outfit += extras_by_weather.get(weather, "")
    return outfit
