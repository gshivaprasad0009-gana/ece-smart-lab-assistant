import streamlit as st

st.set_page_config(
    page_title="ECE Smart Lab Assistant",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ ECE Smart Lab Assistant")
st.write("A simple electronics toolkit for ECE students.")

st.sidebar.header("Select a Tool")

tool = st.sidebar.selectbox(
    "Choose a calculator",
    [
        "Ohm's Law",
        "LED Resistor Calculator",
        "Series Resistance",
        "Parallel Resistance"
    ]
)

if tool == "Ohm's Law":
    st.header("🔌 Ohm's Law Calculator")

    voltage = st.number_input("Voltage (V)", min_value=0.0)
    resistance = st.number_input("Resistance (Ω)", min_value=0.0)

    if st.button("Calculate Current"):
        if resistance == 0:
            st.error("Resistance cannot be zero.")
        else:
            current = voltage / resistance
            st.success(f"Current = {current:.3f} A")


elif tool == "LED Resistor Calculator":
    st.header("💡 LED Resistor Calculator")

    supply_voltage = st.number_input("Supply Voltage (V)", min_value=0.0)
    led_voltage = st.number_input("LED Forward Voltage (V)", min_value=0.0)
    led_current = st.number_input(
        "LED Current (mA)",
        min_value=0.1,
        value=20.0
    )

    if st.button("Calculate Resistor"):
        current_a = led_current / 1000

        if supply_voltage <= led_voltage:
            st.error("Supply voltage must be greater than LED voltage.")
        else:
            resistor = (supply_voltage - led_voltage) / current_a
            st.success(f"Required Resistor = {resistor:.1f} Ω")


elif tool == "Series Resistance":
    st.header("🔗 Series Resistance Calculator")

    r1 = st.number_input("R1 (Ω)", min_value=0.0)
    r2 = st.number_input("R2 (Ω)", min_value=0.0)

    if st.button("Calculate Series Resistance"):
        total = r1 + r2
        st.success(f"Total Resistance = {total:.2f} Ω")


elif tool == "Parallel Resistance":
    st.header("🔗 Parallel Resistance Calculator")

    r1 = st.number_input("R1 (Ω)", min_value=0.01)
    r2 = st.number_input("R2 (Ω)", min_value=0.01)

    if st.button("Calculate Parallel Resistance"):
        total = (r1 * r2) / (r1 + r2)
        st.success(f"Total Resistance = {total:.2f} Ω")

st.divider()

st.caption("ECE Smart Lab Assistant | Built with Python & Streamlit")