import streamlit as st

def render_header():
    st.title("🌍 MoodTrip AI")
    st.markdown("**Plan a trip based on your vibe, energy, and budget.**")

def render_inputs():
    mood = st.slider("Mood (1 = sad, 5 = excited)", 1, 5, 3)
    energy = st.slider("Energy (1 = tired, 10 = super active)", 1, 10, 5)
    budget = st.number_input("Budget (₹)", min_value=500, max_value=50000, value=5000, step=500)
    return mood, energy, budget

def render_destination_info(trip):
    st.subheader(f"✈️ Destination: {trip['name']}")
    st.write(trip["itinerary"])

def render_outfit(outfit_text):
    if outfit_text:
        st.markdown("**👕 Outfit Suggestion:**")
        st.markdown("<ul>", unsafe_allow_html=True)
        for item in outfit_text.split(","):
            st.markdown(f"<li>{item.strip()}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
    else:
        st.write("Wear anything you vibe with 😎")

def render_playlist(playlist):
    st.markdown("**🎶 Your MoodTrip Playlist:**")
    st.markdown('<div class="playlist">', unsafe_allow_html=True)
    if playlist:
        st.markdown("<ul>", unsafe_allow_html=True)
        for item in playlist:
            if isinstance(item, dict):
                name = item.get("title") or item.get("name")
                url = item.get("link") or item.get("url")
                if name and url:
                    st.markdown(f"<li><a href='{url}' target='_blank'>{name}</a></li>", unsafe_allow_html=True)
            else:
                st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
    else:
        st.warning("No playlist available.")
    st.markdown('</div>', unsafe_allow_html=True)
