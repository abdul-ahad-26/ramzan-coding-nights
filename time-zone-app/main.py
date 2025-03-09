# Imports 
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("Time Zone App")

selected_timezones = st.multiselect("Select Timezones",TIME_ZONES, default=["UTC","Asia/Karachi"])

st.subheader("Selected Timezones")
for tz in selected_timezones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert time between timezones")
current_time= st.time_input("Current Time", value=datetime.now().time())
from_tz=st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz=st.selectbox("TO Timezone", TIME_ZONES, index=1)


if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_tz))
    converted_time= dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted time in {to_tz}: {converted_time}")