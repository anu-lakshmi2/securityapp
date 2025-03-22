import streamlit as st
import time
import random

# Self-Security App - Fake Call Feature
st.title("📞 Fake Emergency Call")

# Predefined emergency contacts
emergency_contacts = [
    {"name": "Mom", "number": "+1234567890"},
    {"name": "Dad", "number": "+0987654321"},
    {"name": "Police", "number": "911"},
    {"name": "Best Friend", "number": "+1122334455"},
]

# Select contact to fake a call from
contact_names = [contact["name"] for contact in emergency_contacts]
selected_contact = st.selectbox("📲 Choose an emergency contact", contact_names)

# Function to simulate incoming call
def fake_call():
    # Find the selected contact details
    contact = next((c for c in emergency_contacts if c["name"] == selected_contact), None)
    
    if contact:
        st.warning(f"📞 Incoming call from {contact['name']} ({contact['number']})...")
        with st.spinner("☎️ Phone ringing..."):
            time.sleep(random.randint(3, 5))  # Simulate ringing duration
        st.success("✅ Call Connected! (Pretend to talk)")
    else:
        st.error("⚠️ Contact not found.")

# Button to trigger fake call
if st.button("📲 Trigger Fake Call"):
    fake_call()
