import streamlit as st
import os
import time
import datetime
import shutil

# Directory to save recordings
SAVE_DIR = "recordings"
os.makedirs(SAVE_DIR, exist_ok=True)

# Streamlit UI
st.title("🔴 Self-Security Recording System")
st.write("This app records audio and video for emergency situations.")

# Sidebar for past recordings
st.sidebar.header("📂 Past Recordings")
recordings = os.listdir(SAVE_DIR)

if recordings:
    selected_recording = st.sidebar.selectbox("Select a recording:", recordings)
    if selected_recording:
        st.sidebar.video(os.path.join(SAVE_DIR, selected_recording)) if selected_recording.endswith(".mp4") else st.sidebar.audio(os.path.join(SAVE_DIR, selected_recording))

# Record Video
st.subheader("📹 Video Recording")
video_data = st.camera_input("Click to Record Video")

# Record Audio
st.subheader("🎤 Audio Recording")
audio_data = st.file_uploader("Upload Audio File (MP3, WAV)", type=["mp3", "wav"])

# Save Button
if st.button("Save Recording"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if video_data:
        video_path = os.path.join(SAVE_DIR, f"video_{timestamp}.mp4")
        with open(video_path, "wb") as f:
            f.write(video_data.getbuffer())
        st.success(f"✅ Video saved: {video_path}")

    if audio_data:
        audio_path = os.path.join(SAVE_DIR, f"audio_{timestamp}.{audio_data.type.split('/')[1]}")
        with open(audio_path, "wb") as f:
            f.write(audio_data.getbuffer())
        st.success(f"✅ Audio saved: {audio_path}")

    st.rerun()


# Popup for Delete Option
if recordings:
    st.subheader("🗑️ Delete a Recording?")
    delete_file = st.selectbox("Choose a file to delete", recordings)
    
    if st.button("Delete Selected Recording"):
        os.remove(os.path.join(SAVE_DIR, delete_file))
        st.warning(f"❌ Deleted: {delete_file}")
        st.rerun()
