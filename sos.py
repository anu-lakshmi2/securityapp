import streamlit as st
import time

# Self-Security App - SOS Alert System
st.title("🆘 Emergency SOS Alert")

# User inputs their location
location = st.text_input("📍 Enter your location", placeholder="E.g., 123 Main Street, City, Country")

# Predefined emergency message
default_message = "🚨 EMERGENCY! I need immediate help at my location."
custom_message = st.text_area("📝 Custom Message (Optional)", value=default_message)

# SOS Button
if st.button("🚨 SEND SOS ALERT"):
    if location.strip():  # Ensure location is entered
        st.error("🚨 SOS Alert Sent!")  # Display alert
        st.write(f"**📍 Location:** {location}")
        st.write(f"**📩 Message:** {custom_message}")

        # Simulate sending alert (this can be replaced with actual API integration)
        with st.spinner("Sending SOS alert..."):
            time.sleep(2)  # Simulate delay
            st.success("✅ Alert successfully sent to emergency contacts!")

    else:
        st.warning("⚠️ Please enter your location before sending an SOS alert.")

