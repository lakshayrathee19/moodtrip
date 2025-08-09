import streamlit as st
import json
from trip_generator import suggest_trip
from playlist_outfit_generator import generate_playlist, recommend_outfit
from style import inject_custom_css

# Page config
st.set_page_config(page_title="🌍 MoodTrip AI", layout="centered")

# Inject custom CSS
inject_custom_css()

# Load destination data
with open("destinations.json", "r") as f:
    destinations = json.load(f)

# Start of main container
st.markdown('<div class="custom-container">', unsafe_allow_html=True)

# Animated Heading
st.markdown('<h1 class="custom-header animated-underline">MoodTrip AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="custom-sub">Curated trips based on your mood, energy & vibe</p>', unsafe_allow_html=True)

# Inputs
mood = st.slider("🌈 Mood (1 = sad, 5 = excited)", 1, 5, 3)
energy = st.slider("⚡ Energy (1 = tired, 10 = super active)", 1, 10, 5)
budget = st.number_input("💰 Budget (₹)", min_value=500, max_value=50000, value=5000, step=500)

# Mapping functions
def map_mood_num_to_str(mood_num):
    return ["relaxed", "relaxed", "romantic", "adventurous", "party"][mood_num - 1]

def map_energy_num_to_str(energy_num):
    if energy_num <= 3:
        return "low"
    elif energy_num <= 7:
        return "medium"
    return "high"

def map_mood_num_to_mood_detector_str(mood_num):
    return ["sad", "calm", "romantic", "adventurous", "happy"][mood_num - 1]

# Action button
if st.button("✨ Generate My MoodTrip"):
    trip = suggest_trip(mood, energy, budget)

    if trip:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)

        st.subheader(f"✈️ Destination: {trip['name']}")
        st.markdown(f"<p>{trip['itinerary']}</p>", unsafe_allow_html=True)

        # Outfit
        outfit = recommend_outfit(
            map_mood_num_to_mood_detector_str(mood),
            trip.get("destination_type", "city"),
            trip.get("weather", "sunny")
        )

        if outfit:
            st.markdown("**👕 Outfit Suggestion:**")
            st.markdown("<ul>", unsafe_allow_html=True)
            for item in outfit.split(","):
                st.markdown(f"<li>{item.strip()}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)
        else:
            st.write("Wear anything you vibe with 😎")

        # Playlist
        st.markdown("**🎶 Your MoodTrip Playlist:**")
        st.markdown('<div class="playlist">', unsafe_allow_html=True)
        if trip.get("playlist"):
            st.markdown("<ul>", unsafe_allow_html=True)
            for item in trip["playlist"]:
                if isinstance(item, dict):
                    name = item.get("title") or item.get("name")
                    url = item.get("link") or item.get("url")
                    if name and url:
                        st.markdown(f"<li><a href='{url}' target='_blank'>{name}</a></li>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)
        else:
            st.warning("No playlist available for this combo.")
        
        st.markdown('</div>', unsafe_allow_html=True)  # End result box

    else:
        st.error("No destination found. Try adjusting mood/energy/budget.")

# Close custom container
st.markdown('</div>', unsafe_allow_html=True)
