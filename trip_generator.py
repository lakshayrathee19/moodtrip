import json
import random
from playlist_outfit_generator import generate_playlist, recommend_outfit

# Load destinations from JSON
with open("destinations.json", "r", encoding="utf-8") as f:
    DESTINATIONS = json.load(f)

# Mapping for moods and energy levels
def get_mood_category(mood_score):
    if isinstance(mood_score, str):
        mood_score = mood_score.lower()
        mood_map = {
            "sad": "relaxed",
            "romantic": "romantic",
            "excited": "party",
            "angry": "adventurous",
            "happy": "party",
        }
        return mood_map.get(mood_score, "relaxed")
    else:
        if mood_score <= 2:
            return "relaxed"
        elif mood_score == 3:
            return "romantic"
        elif mood_score == 4:
            return "adventurous"
        else:
            return "party"

def get_energy_level(energy_score):
    if isinstance(energy_score, str):
        energy_score = energy_score.lower()
        if energy_score in ["low", "1", "2", "3"]:
            return "low"
        elif energy_score in ["medium", "4", "5", "6", "7"]:
            return "medium"
        else:
            return "high"
    else:
        if energy_score <= 3:
            return "low"
        elif energy_score <= 7:
            return "medium"
        else:
            return "high"

def generate_itinerary(mood, energy, budget, destination, destination_type="nature", weather="mild", days=3):
    mood_category = get_mood_category(mood)
    energy_level = get_energy_level(energy)

    itinerary_text = f"""
**Day 1**: Arrive at {destination}, explore local attractions and enjoy a relaxing evening by the {destination_type}.

**Day 2**: Based on your mood (*{mood_category}*) and energy (*{energy_level}*), enjoy a mix of adventure and chill — like hiking, local cafes, or music spots.

**Day 3**: Visit scenic locations nearby, do light shopping, and unwind with local cuisine and sunset views.
    """

    playlist = generate_playlist(mood_category, energy_level)
    outfit = recommend_outfit(mood_category, destination_type, weather)

    return {
        "name": destination,
        "itinerary": itinerary_text.strip(),
        "playlist": playlist,
        "outfit": outfit
    }

def suggest_trip(mood, energy, budget):
    # Ensure numerical
    mood_score = int(mood) if not isinstance(mood, int) else mood
    energy_score = int(energy) if not isinstance(energy, int) else energy
    budget = int(budget)

    # Filter destinations with matching mood/energy/budget ranges
    filtered = [
        dest for dest in DESTINATIONS
        if dest["min_mood"] <= mood_score <= dest["max_mood"] and
           dest["min_energy"] <= energy_score <= dest["max_energy"] and
           dest["budget_value"] <= budget
    ]

    if not filtered:
        return None

    selected = random.choice(filtered)
    return generate_itinerary(
        mood, energy, budget,
        destination=selected["name"],
        destination_type=selected.get("type", "nature"),
        weather=selected.get("weather", "mild"),
        days=3
    )
