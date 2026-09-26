import streamlit as st
import math
import requests
# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ECE Smart Lab Assistant",
    page_icon="⚡",
    layout="wide"
)

# ============================================================
# HEADER
# ============================================================

st.title("⚡ ECE Smart Lab Assistant")
st.write("Interactive electronics toolkit for ECE students.")

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

section = st.sidebar.selectbox(
    "Choose a section",
    [
        "🏠 Smart Lab Home",
        "🔌 Circuit Calculators",
        "📡 ECE Calculators",
        "📚 Learn ECE",
        "🤖 ECE AI Assistant"
    ]
)

if section == "🏠 Smart Lab Home":

    st.header("⚡ Welcome to ECE Smart Lab")

    st.write(
        "An interactive electronics toolkit for ECE students "
        "to calculate, learn, and explore engineering concepts."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔌 Circuit Calculators")
        st.write("Solve common electrical and circuit calculations.")
        st.info("Ohm's Law • LED Resistor • Resistance • Power • Voltage Divider")

    with col2:
        st.subheader("📡 ECE Calculators")
        st.write("Explore useful electronics and communication formulas.")
        st.info("Wavelength • dB • RC Time Constant • Resonance")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📚 Learn ECE")
        st.write("Review important concepts across major ECE subjects.")
        st.info("Basic Electronics • Analog • Digital • Communication • EM")

    with col4:
        st.subheader("🤖 ECE AI Assistant")
        st.write("Ask your local AI assistant ECE-related questions.")
        st.info("Powered by local Ollama AI")

    st.divider()

    st.success("🚀 Select a section from the sidebar to get started.")

# ============================================================
# CIRCUIT CALCULATORS
# ============================================================

elif section == "🔌 Circuit Calculators":



    st.header("🔌 Circuit Calculators")

    calculator = st.selectbox(
        "Select calculator",
        [
            "Ohm's Law",
            "LED Resistor",
            "Series Resistance",
            "Parallel Resistance",
            "Power Calculator",
            "Voltage Divider"
        ]
    )

    # --------------------------------------------------------
    # OHM'S LAW
    # --------------------------------------------------------

    if calculator == "Ohm's Law":

        st.subheader("⚡ Ohm's Law Calculator")

        col1, col2 = st.columns(2)

        with col1:
            voltage = st.number_input(
                "Voltage (V)",
                min_value=0.0,
                value=12.0
            )

        with col2:
            resistance = st.number_input(
                "Resistance (Ω)",
                min_value=0.01,
                value=100.0
            )

        if st.button("Calculate Current", key="ohm"):

            current = voltage / resistance

            st.success(
                f"Current = {current:.4f} A"
            )

            st.info(
                f"Formula: I = V / R = {voltage} / {resistance}"
            )

    # --------------------------------------------------------
    # LED RESISTOR
    # --------------------------------------------------------

    elif calculator == "LED Resistor":

        st.subheader("💡 LED Resistor Calculator")

        col1, col2, col3 = st.columns(3)

        with col1:
            supply_voltage = st.number_input(
                "Supply Voltage (V)",
                min_value=0.0,
                value=5.0
            )

        with col2:
            led_voltage = st.number_input(
                "LED Forward Voltage (V)",
                min_value=0.0,
                value=2.0
            )

        with col3:
            led_current = st.number_input(
                "LED Current (mA)",
                min_value=0.1,
                value=20.0
            )

        if st.button("Calculate Resistor", key="led"):

            if supply_voltage <= led_voltage:

                st.error(
                    "Supply voltage must be greater than LED forward voltage."
                )

            else:

                current_a = led_current / 1000

                resistor = (
                    supply_voltage - led_voltage
                ) / current_a

                st.success(
                    f"Required Resistor = {resistor:.1f} Ω"
                )

                st.info(
                    "Formula: R = (Vs - Vf) / I"
                )

    # --------------------------------------------------------
    # SERIES RESISTANCE
    # --------------------------------------------------------

    elif calculator == "Series Resistance":

        st.subheader("🔗 Series Resistance Calculator")

        count = st.number_input(
            "Number of resistors",
            min_value=2,
            max_value=10,
            value=2,
            step=1
        )

        resistors = []

        for i in range(int(count)):

            value = st.number_input(
                f"R{i + 1} (Ω)",
                min_value=0.0,
                value=100.0,
                key=f"series_{i}"
            )

            resistors.append(value)

        if st.button("Calculate Series Resistance"):

            total = sum(resistors)

            st.success(
                f"Total Resistance = {total:.2f} Ω"
            )

            st.info(
                "Formula: Rtotal = R1 + R2 + R3 + ..."
            )

    # --------------------------------------------------------
    # PARALLEL RESISTANCE
    # --------------------------------------------------------

    elif calculator == "Parallel Resistance":

        st.subheader("🔗 Parallel Resistance Calculator")

        count = st.number_input(
            "Number of resistors",
            min_value=2,
            max_value=10,
            value=2,
            step=1
        )

        resistors = []

        for i in range(int(count)):

            value = st.number_input(
                f"R{i + 1} (Ω)",
                min_value=0.01,
                value=100.0,
                key=f"parallel_{i}"
            )

            resistors.append(value)

        if st.button("Calculate Parallel Resistance"):

            inverse_total = sum(
                1 / r for r in resistors
            )

            total = 1 / inverse_total

            st.success(
                f"Total Resistance = {total:.2f} Ω"
            )

            st.info(
                "Formula: 1/Rtotal = 1/R1 + 1/R2 + ..."
            )

    # --------------------------------------------------------
    # POWER CALCULATOR
    # --------------------------------------------------------

    elif calculator == "Power Calculator":

        st.subheader("⚡ Electrical Power Calculator")

        method = st.selectbox(
            "Choose calculation",
            [
                "Voltage × Current",
                "Current² × Resistance",
                "Voltage² ÷ Resistance"
            ]
        )

        if method == "Voltage × Current":

            voltage = st.number_input(
                "Voltage (V)",
                min_value=0.0,
                value=12.0
            )

            current = st.number_input(
                "Current (A)",
                min_value=0.0,
                value=1.0
            )

            if st.button("Calculate Power", key="power1"):

                power = voltage * current

                st.success(
                    f"Power = {power:.2f} W"
                )

        elif method == "Current² × Resistance":

            current = st.number_input(
                "Current (A)",
                min_value=0.0,
                value=1.0
            )

            resistance = st.number_input(
                "Resistance (Ω)",
                min_value=0.0,
                value=10.0
            )

            if st.button("Calculate Power", key="power2"):

                power = current ** 2 * resistance

                st.success(
                    f"Power = {power:.2f} W"
                )

        else:

            voltage = st.number_input(
                "Voltage (V)",
                min_value=0.0,
                value=12.0
            )

            resistance = st.number_input(
                "Resistance (Ω)",
                min_value=0.01,
                value=100.0
            )

            if st.button("Calculate Power", key="power3"):

                power = voltage ** 2 / resistance

                st.success(
                    f"Power = {power:.2f} W"
                )

    # --------------------------------------------------------
    # VOLTAGE DIVIDER
    # --------------------------------------------------------

    elif calculator == "Voltage Divider":

        st.subheader("🔋 Voltage Divider Calculator")

        col1, col2, col3 = st.columns(3)

        with col1:

            vin = st.number_input(
                "Input Voltage (V)",
                min_value=0.0,
                value=12.0
            )

        with col2:

            r1 = st.number_input(
                "R1 (Ω)",
                min_value=0.01,
                value=1000.0
            )

        with col3:

            r2 = st.number_input(
                "R2 (Ω)",
                min_value=0.01,
                value=1000.0
            )

        if st.button("Calculate Output Voltage"):

            vout = vin * r2 / (r1 + r2)

            st.success(
                f"Output Voltage = {vout:.3f} V"
            )

            st.info(
                "Formula: Vout = Vin × R2 / (R1 + R2)"
            )


# ============================================================
# ECE CALCULATORS
# ============================================================

elif section == "📡 ECE Calculators":

    st.header("📡 ECE Calculators")

    calculator = st.selectbox(
        "Select calculator",
        [
            "Frequency / Wavelength",
            "dB Calculator",
            "RC Time Constant",
            "Resonant Frequency"
        ]
    )

    # --------------------------------------------------------
    # FREQUENCY / WAVELENGTH
    # --------------------------------------------------------

    if calculator == "Frequency / Wavelength":

        st.subheader("📡 Frequency ↔ Wavelength")

        mode = st.radio(
            "Choose calculation",
            [
                "Frequency → Wavelength",
                "Wavelength → Frequency"
            ]
        )

        if mode == "Frequency → Wavelength":

            frequency = st.number_input(
                "Frequency (Hz)",
                min_value=0.000001,
                value=1e9,
                format="%.6g"
            )

            if st.button("Calculate Wavelength"):

                wavelength = 3e8 / frequency

                st.success(
                    f"Wavelength = {wavelength:.6f} m"
                )

        else:

            wavelength = st.number_input(
                "Wavelength (m)",
                min_value=0.000001,
                value=0.3
            )

            if st.button("Calculate Frequency"):

                frequency = 3e8 / wavelength

                st.success(
                    f"Frequency = {frequency:.3e} Hz"
                )

        st.info(
            "Formula: c = fλ, where c ≈ 3 × 10⁸ m/s"
        )

    # --------------------------------------------------------
    # DECIBEL
    # --------------------------------------------------------

    elif calculator == "dB Calculator":

        st.subheader("📊 Decibel Calculator")

        mode = st.selectbox(
            "Choose calculation",
            [
                "Power Ratio → dB",
                "Voltage Ratio → dB"
            ]
        )

        ratio = st.number_input(
            "Ratio",
            min_value=0.000001,
            value=10.0
        )

        if st.button("Calculate dB"):

            if mode == "Power Ratio → dB":

                db = 10 * math.log10(ratio)

                st.success(
                    f"Gain/Loss = {db:.3f} dB"
                )

                st.info(
                    "Formula: dB = 10 log₁₀(P₂/P₁)"
                )

            else:

                db = 20 * math.log10(ratio)

                st.success(
                    f"Gain/Loss = {db:.3f} dB"
                )

                st.info(
                    "Formula: dB = 20 log₁₀(V₂/V₁)"
                )

    # --------------------------------------------------------
    # RC TIME CONSTANT
    # --------------------------------------------------------

    elif calculator == "RC Time Constant":

        st.subheader("⏱️ RC Time Constant")

        resistance = st.number_input(
            "Resistance (Ω)",
            min_value=0.0,
            value=1000.0
        )

        capacitance = st.number_input(
            "Capacitance (F)",
            min_value=0.000001,
            value=0.000001,
            format="%.8g"
        )

        if st.button("Calculate Time Constant"):

            tau = resistance * capacitance

            st.success(
                f"Time Constant τ = {tau:.6f} seconds"
            )

            st.info(
                "Formula: τ = RC"
            )

    # --------------------------------------------------------
    # RESONANT FREQUENCY
    # --------------------------------------------------------

    elif calculator == "Resonant Frequency":

        st.subheader("📻 LC Resonant Frequency")

        inductance = st.number_input(
            "Inductance (H)",
            min_value=0.000001,
            value=0.001,
            format="%.8g"
        )

        capacitance = st.number_input(
            "Capacitance (F)",
            min_value=0.000000000001,
            value=0.000001,
            format="%.8g"
        )

        if st.button("Calculate Resonant Frequency"):

            frequency = (
                1 /
                (
                    2 *
                    math.pi *
                    math.sqrt(
                        inductance * capacitance
                    )
                )
            )

            st.success(
                f"Resonant Frequency = {frequency:.3f} Hz"
            )

            st.info(
                "Formula: fr = 1 / (2π√LC)"
            )


# ============================================================
# LEARN ECE
# ============================================================

elif section == "📚 Learn ECE":

    st.header("📚 Learn ECE")

    subject = st.selectbox(
        "Choose a subject",
        [
            "Basic Electronics",
            "Analog Circuits",
            "Digital Electronics",
            "Communication",
            "Electromagnetics"
        ]
    )

    # --------------------------------------------------------
    # BASIC ELECTRONICS
    # --------------------------------------------------------

    if subject == "Basic Electronics":

        st.subheader("🔌 Basic Electronics")

        st.markdown("""
### Important Topics

- Voltage
- Current
- Resistance
- Ohm's Law
- Kirchhoff's Laws
- Power
- Capacitors
- Inductors
- Diodes
- Transistors
- LED
- Rectifiers
        """)

    # --------------------------------------------------------
    # ANALOG CIRCUITS
    # --------------------------------------------------------

    elif subject == "Analog Circuits":

        st.subheader("🔊 Analog Circuits")

        st.markdown("""
### Important Topics

- Diode Circuits
- BJT
- FET
- MOSFET
- CE Amplifier
- CB Amplifier
- CC Amplifier
- Small Signal Analysis
- Feedback Amplifiers
- Oscillators
- Operational Amplifiers
- Filters
        """)

    # --------------------------------------------------------
    # DIGITAL ELECTRONICS
    # --------------------------------------------------------

    elif subject == "Digital Electronics":

        st.subheader("💻 Digital Electronics")

        st.markdown("""
### Important Topics

- Number Systems
- Boolean Algebra
- Logic Gates
- Karnaugh Maps
- Combinational Circuits
- Multiplexers
- Demultiplexers
- Encoders
- Decoders
- Flip-Flops
- Counters
- Registers
        """)

    # --------------------------------------------------------
    # COMMUNICATION
    # --------------------------------------------------------

    elif subject == "Communication":

        st.subheader("📡 Communication Systems")

        st.markdown("""
### Important Topics

- Analog Communication
- AM
- FM
- PM
- Modulation
- Demodulation
- Noise
- Sampling
- Pulse Modulation
- Digital Communication
- Antennas
        """)

    # --------------------------------------------------------
    # ELECTROMAGNETICS
    # --------------------------------------------------------

    elif subject == "Electromagnetics":

        st.subheader("🧲 Electromagnetics")

        st.markdown("""
### Important Topics

- Electric Fields
- Magnetic Fields
- Maxwell's Equations
- Wave Propagation
- Transmission Lines
- Polarization
- Antennas
- Radiation
- Electromagnetic Waves
        """)


# ============================================================
# ECE AI ASSISTANT
# ============================================================

elif section == "🤖 ECE AI Assistant":
    st.header("🤖 ECE AI Assistant")
    st.write("Ask any ECE question and get an explanation from local AI.")

    question = st.text_area(
        "Ask an ECE question",
        placeholder="Example: Explain a half-wave dipole antenna in simple words.",
        height=150
    )

    if st.button("🚀 Ask ECE Assistant"):
        if question.strip():

            with st.spinner("🤖 Thinking..."):
                try:
                    response = requests.post(
                        "http://localhost:11434/api/generate",
                        json={
                            "model": "llama3.2:3b",
                            "prompt": f"""
You are an ECE AI Assistant.

Explain the following ECE question in simple,
student-friendly language.

Question:
{question}

Give:
1. Simple explanation
2. Important formula if applicable
3. Small example if applicable
""",
                            "stream": False
                        },
                        timeout=120
                    )

                    if response.status_code == 200:
                        answer = response.json()["response"]
                        st.success("✅ Answer")
                        st.markdown(answer)
                    else:
                        st.error(
                            f"Ollama returned an error: {response.status_code}"
                        )

                except requests.exceptions.ConnectionError:
                    st.error(
                        "❌ Cannot connect to Ollama. "
                        "Make sure Ollama is running."
                    )

                except Exception as e:
                    st.error(f"❌ Error: {e}")

        else:
            st.warning("Please enter an ECE question first.")

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "⚡ ECE Smart Lab Assistant | Built with Python & Streamlit"
)