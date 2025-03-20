import streamlit as st
from transformers import pipeline
from geopy.distance import geodesic

# Initialize AI model
generator = pipeline("text-generation", model="gpt4")

# App title and header
st.title("Ask Emily")
st.header("Ask Emily - Your AI Travel Companion")

# User Inputs for travel planner
destination = st.text_input("Enter your destination:")
origin = st.text_input("Enter your starting point:",)
activities = st.text_input("What activities are you interested in?")
travel_days = st.slider("How many days is your trip?", 1, 14, 7)

# Calculate Distance and Display Map Link
if st.button("Show Route and Generate Itinerary"):
    try:
        
        origin_coords = (51.5074, -0.1278)  # London
        dest_coords = (48.8566, 2.3522)    # Paris

        # Calculate distance
        distance = geodesic(origin_coords, dest_coords).km
        st.write(f"Distance from {origin} to {destination}: {distance:.2f} km")
        
        # Generate Google Maps link
        map_url = f"https://www.google.com/maps/dir/{origin}/{destination}"
        st.markdown(f"[View route on Google Maps]({map_url})")

        # Generate Itinerary
        prompt = f"I am planning a {travel_days}-day trip to {destination}. I enjoy {activities}. What are some recommendations?"
        trip_plan = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
        st.subheader("Your Trip Itinerary:")
        st.write(trip_plan)

    except Exception as e:
        st.error(f"Error calculating route: {e}")

st.subheader("Find Nearby Amenities")
amenity = st.selectbox("Choose what you want to find nearby:", ["Hotel", "Lounge", "Mall"])

if st.button("Find Nearby"):
    google_maps_url = f"https://www.google.com/maps/search/{amenity}+near+{destination}"
    st.markdown(f"[View nearby {amenity} on Google Maps]({google_maps_url})")

# TaskRabbit-like RV Repair Service Directory
st.subheader("Need RV Repairs? Find Nearby Technicians!")
repair_location = st.text_input("Enter your current location for RV repair:", "San Francisco")
repair_type = st.text_area("Describe your repair needs:", "e.g., engine trouble, flat tire")

if st.button("Find RV Technicians"):
    st.write("Finding available technicians near you...")
    # Dummy technician list
    technicians = [
        {"name": "John's RV Repairs", "location": "San Francisco", "contact": "555-1234"},
        {"name": "EZ RV Repair", "location": "San Francisco", "contact": "555-5678"},
    ]

    st.subheader("Available Technicians:")
    for tech in technicians:
        st.write(f"**{tech['name']}**")
        st.write(f"Location: {tech['location']}")
        st.write(f"Contact: {tech['contact']}")
        st.write("---")
