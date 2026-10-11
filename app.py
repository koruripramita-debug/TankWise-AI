
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TankWise AI",
    page_icon="💧",
    layout="wide"
)

st.title("💧 TankWise AI")
st.subheader("Heat & Water Risk Assistant")
st.write("Monitor household water and get heat-safety advice.")

st.info("Educational prototype. It does not use live weather data.")

tab1, tab2, tab3 = st.tabs([
    "Water Tracker", "Heat Safety", "Dashboard"
])

if "history" not in st.session_state:
    st.session_state.history = []

with tab1:
    st.header("Household Water Tracker")

    capacity = st.number_input(
        "Tank capacity (litres)", 1, 1000000, 1000
    )
    available = st.number_input(
        "Water available (litres)", 0, 1000000, 600
    )
    daily_use = st.number_input(
        "Daily water use (litres)", 1, 100000, 400
    )

    if st.button("Calculate Water Status"):
        if available > capacity:
            st.error("Water cannot exceed tank capacity.")
        else:
            percent = available / capacity * 100
            days = available / daily_use

            st.metric("Water remaining", f"{percent:.1f}%")
            st.metric("Estimated supply", f"{days:.1f} days")

            if percent <= 20:
                st.error("Low water level. Plan a refill.")
            elif percent <= 50:
                st.warning("Use water carefully and plan a refill.")
            else:
                st.success("Water level is above the low-level threshold.")

            st.session_state.history.append({
                "Capacity (L)": capacity,
                "Available (L)": available,
                "Remaining (%)": round(percent, 1),
                "Estimated days": round(days, 1)
            })

with tab2:
    st.header("Heat Safety Assistant")

    temp = st.number_input(
        "Temperature (°C)", -20.0, 60.0, 35.0
    )
    humidity = st.slider("Humidity (%)", 0, 100, 60)

    if st.button("Check Heat Conditions"):
        if temp >= 40:
            st.error("Very hot conditions. Take extra precautions.")
        elif temp >= 35:
            st.warning("High heat. Avoid strenuous outdoor activity.")
        elif temp >= 30:
            st.info("Warm conditions. Take breaks and seek shade.")
        else:
            st.success("Keep following local weather advice.")

        if temp >= 30 and humidity >= 70:
            st.warning("High humidity may make cooling harder.")

        st.write("Safety tips:")
        st.write("- Drink water regularly.")
        st.write("- Stay in shade or a cool indoor place.")
        st.write("- Avoid strenuous activity during peak heat.")
        st.write("- Follow official local heat alerts.")

with tab3:
    st.header("Water Monitoring Dashboard")

    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True)

        st.download_button(
            "Download CSV Report",
            df.to_csv(index=False).encode("utf-8"),
            "tankwise_report.csv",
            "text/csv"
        )
    else:
        st.write("Calculate water status to create a report.")

st.divider()
st.caption("TankWise AI | Environmental Hacks 2026")
