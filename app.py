import streamlit as st

import math

import requests

from hindsight_client import Hindsight



HINDSIGHT_URL = "http://localhost:8888"
HINDSIGHT_BANK = "ece-smart-lab"


def _run_hindsight_in_thread(operation, *args, **kwargs):
    """Run Hindsight sync calls in a worker thread to avoid Streamlit loop conflicts."""
    import concurrent.futures

    def _worker():
        client = Hindsight(HINDSIGHT_URL)
        try:
            return operation(client, *args, **kwargs)
        finally:
            client.close()

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        return executor.submit(_worker).result(timeout=120)


def _hindsight_recall(query):
    return _run_hindsight_in_thread(
        lambda client, bank_id, q: client.recall(
            bank_id=bank_id, query=q, max_tokens=1500
        ),
        HINDSIGHT_BANK,
        query,
    )


def _hindsight_retain(content):
    return _run_hindsight_in_thread(
        lambda client, bank_id, text: client.retain(
            bank_id=bank_id, content=text
        ),
        HINDSIGHT_BANK,
        content,
    )

# ============================================================

# PAGE CONFIGURATION

# ============================================================



st.set_page_config(

    page_title="ECE Smart Lab Assistant",

    page_icon="⚡",

    layout="wide",

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

        "🤖 ECE AI Assistant",

    ],

)



# ============================================================

# SMART LAB HOME

# ============================================================



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

        st.info(

            "Ohm's Law • LED Resistor • Resistance • Power • Voltage Divider"

        )



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

    st.subheader("🚀 Quick Start")



    quick_col1, quick_col2, quick_col3 = st.columns(3)



    with quick_col1:

        st.info(

            "🔌 **Calculate**\n\n"

            "Use circuit and ECE calculators for quick engineering calculations."

        )



    with quick_col2:

        st.info(

            "📚 **Learn**\n\n"

            "Explore important ECE topics and build your fundamentals."

        )



    with quick_col3:

        st.info(

            "🤖 **Ask AI**\n\n"

            "Ask the local ECE AI Assistant for simple explanations and examples."

        )



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

            "Voltage Divider",

        ],

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

                value=12.0,

                key="ohm_voltage",

            )



        with col2:

            resistance = st.number_input(

                "Resistance (Ω)",

                min_value=0.01,

                value=100.0,

                key="ohm_resistance",

            )



        if st.button("Calculate Current", key="ohm"):

            current = voltage / resistance

            st.success(f"Current = {current:.4f} A")

            st.info(f"Formula: I = V / R = {voltage} / {resistance}")



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

                value=5.0,

                key="led_supply",

            )



        with col2:

            led_voltage = st.number_input(

                "LED Forward Voltage (V)",

                min_value=0.0,

                value=2.0,

                key="led_voltage",

            )



        with col3:

            led_current = st.number_input(

                "LED Current (mA)",

                min_value=0.1,

                value=20.0,

                key="led_current",

            )



        if st.button("Calculate Resistor", key="led"):

            if supply_voltage <= led_voltage:

                st.error(

                    "Supply voltage must be greater than LED forward voltage."

                )

            else:

                current_a = led_current / 1000

                resistor = (supply_voltage - led_voltage) / current_a

                st.success(f"Required Resistor = {resistor:.1f} Ω")

                st.info("Formula: R = (Vs - Vf) / I")



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

            step=1,

            key="series_count",

        )



        resistors = []



        for i in range(int(count)):

            value = st.number_input(

                f"R{i + 1} (Ω)",

                min_value=0.0,

                value=100.0,

                key=f"series_{i}",

            )

            resistors.append(value)



        if st.button("Calculate Series Resistance", key="series_button"):

            total = sum(resistors)

            st.success(f"Total Resistance = {total:.2f} Ω")

            st.info("Formula: Rtotal = R1 + R2 + R3 + ...")



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

            step=1,

            key="parallel_count",

        )



        resistors = []



        for i in range(int(count)):

            value = st.number_input(

                f"R{i + 1} (Ω)",

                min_value=0.01,

                value=100.0,

                key=f"parallel_{i}",

            )

            resistors.append(value)



        if st.button("Calculate Parallel Resistance", key="parallel_button"):

            inverse_total = sum(1 / r for r in resistors)

            total = 1 / inverse_total

            st.success(f"Total Resistance = {total:.2f} Ω")

            st.info("Formula: 1/Rtotal = 1/R1 + 1/R2 + ...")



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

                "Voltage² ÷ Resistance",

            ],

        )



        if method == "Voltage × Current":

            voltage = st.number_input(

                "Voltage (V)",

                min_value=0.0,

                value=12.0,

                key="power_voltage_1",

            )



            current = st.number_input(

                "Current (A)",

                min_value=0.0,

                value=1.0,

                key="power_current_1",

            )



            if st.button("Calculate Power", key="power1"):

                power = voltage * current

                st.success(f"Power = {power:.2f} W")

                st.info("Formula: P = V × I")



        elif method == "Current² × Resistance":

            current = st.number_input(

                "Current (A)",

                min_value=0.0,

                value=1.0,

                key="power_current_2",

            )



            resistance = st.number_input(

                "Resistance (Ω)",

                min_value=0.01,

                value=10.0,

                key="power_resistance_2",

            )



            if st.button("Calculate Power", key="power2"):

                power = current**2 * resistance

                st.success(f"Power = {power:.2f} W")

                st.info("Formula: P = I²R")



        else:

            voltage = st.number_input(

                "Voltage (V)",

                min_value=0.0,

                value=12.0,

                key="power_voltage_3",

            )



            resistance = st.number_input(

                "Resistance (Ω)",

                min_value=0.01,

                value=100.0,

                key="power_resistance_3",

            )



            if st.button("Calculate Power", key="power3"):

                power = voltage**2 / resistance

                st.success(f"Power = {power:.2f} W")

                st.info("Formula: P = V² / R")



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

                value=12.0,

                key="divider_vin",

            )



        with col2:

            r1 = st.number_input(

                "R1 (Ω)",

                min_value=0.01,

                value=1000.0,

                key="divider_r1",

            )



        with col3:

            r2 = st.number_input(

                "R2 (Ω)",

                min_value=0.01,

                value=1000.0,

                key="divider_r2",

            )



        if st.button("Calculate Output Voltage", key="divider"):

            vout = vin * r2 / (r1 + r2)

            st.success(f"Output Voltage = {vout:.4f} V")

            st.info("Formula: Vout = Vin × R2 / (R1 + R2)")



# ============================================================

# ECE CALCULATORS

# ============================================================



elif section == "📡 ECE Calculators":

    st.header("📡 ECE Calculators")



    calculator = st.selectbox(

        "Select ECE calculator",

        [

            "Wavelength",

            "Decibel Gain",

            "RC Time Constant",

            "Resonant Frequency",

        ],

    )



    # --------------------------------------------------------

    # WAVELENGTH

    # --------------------------------------------------------



    if calculator == "Wavelength":

        st.subheader("📡 Wavelength Calculator")



        frequency = st.number_input(

            "Frequency (Hz)",

            min_value=0.000001,

            value=1_000_000.0,

            format="%.6f",

        )



        if st.button("Calculate Wavelength", key="wavelength"):

            speed_of_light = 299_792_458

            wavelength = speed_of_light / frequency

            st.success(f"Wavelength = {wavelength:.6f} m")

            st.info("Formula: λ = c / f")



    # --------------------------------------------------------

    # DECIBEL

    # --------------------------------------------------------



    elif calculator == "Decibel Gain":

        st.subheader("📶 Decibel Gain Calculator")



        mode = st.selectbox(

            "Choose calculation",

            ["Power Gain", "Voltage Gain"],

        )



        if mode == "Power Gain":

            pout = st.number_input(

                "Output Power",

                min_value=0.000001,

                value=10.0,

                key="db_pout",

            )

            pin = st.number_input(

                "Input Power",

                min_value=0.000001,

                value=1.0,

                key="db_pin",

            )



            if st.button("Calculate dB", key="db_power"):

                db = 10 * math.log10(pout / pin)

                st.success(f"Gain = {db:.2f} dB")

                st.info("Formula: G(dB) = 10 log10(Pout / Pin)")



        else:

            vout = st.number_input(

                "Output Voltage",

                min_value=0.000001,

                value=10.0,

                key="db_vout",

            )

            vin = st.number_input(

                "Input Voltage",

                min_value=0.000001,

                value=1.0,

                key="db_vin",

            )



            if st.button("Calculate dB", key="db_voltage"):

                db = 20 * math.log10(vout / vin)

                st.success(f"Gain = {db:.2f} dB")

                st.info("Formula: G(dB) = 20 log10(Vout / Vin)")



    # --------------------------------------------------------

    # RC TIME CONSTANT

    # --------------------------------------------------------



    elif calculator == "RC Time Constant":

        st.subheader("⏱️ RC Time Constant Calculator")



        resistance = st.number_input(

            "Resistance (Ω)",

            min_value=0.01,

            value=1000.0,

            key="rc_r",

        )



        capacitance = st.number_input(

            "Capacitance (F)",

            min_value=0.000000001,

            value=0.000001,

            format="%.9f",

            key="rc_c",

        )



        if st.button("Calculate Time Constant", key="rc"):

            tau = resistance * capacitance

            st.success(f"Time Constant τ = {tau:.6f} s")

            st.info("Formula: τ = R × C")



    # --------------------------------------------------------

    # RESONANCE

    # --------------------------------------------------------



    elif calculator == "Resonant Frequency":

        st.subheader("📻 Resonant Frequency Calculator")



        inductance = st.number_input(

            "Inductance (H)",

            min_value=0.000001,

            value=0.001,

            format="%.6f",

            key="res_l",

        )



        capacitance = st.number_input(

            "Capacitance (F)",

            min_value=0.000000001,

            value=0.000001,

            format="%.9f",

            key="res_c",

        )



        if st.button("Calculate Resonant Frequency", key="resonance"):

            frequency = 1 / (2 * math.pi * math.sqrt(inductance * capacitance))

            st.success(f"Resonant Frequency = {frequency:.2f} Hz")

            st.info("Formula: f₀ = 1 / (2π√(LC))")



# ============================================================

# LEARN ECE

# ============================================================



elif section == "📚 Learn ECE":

    st.header("📚 Learn ECE")



    topic = st.selectbox(

        "Choose a topic",

        [

            "Basic Electronics",

            "Analog Electronics",

            "Digital Electronics",

            "Communication Systems",

            "Electromagnetic Waves",

        ],

    )



    topics = {

        "Basic Electronics": {

            "definition": "Basic electronics covers voltage, current, resistance, power, components, and simple circuits.",

            "points": [

                "Voltage is electrical potential difference.",

                "Current is the flow of electric charge.",

                "Resistance opposes current flow.",

                "Ohm's Law: V = IR.",

            ],

        },

        "Analog Electronics": {

            "definition": "Analog electronics deals with continuously varying signals and circuits such as amplifiers and filters.",

            "points": [

                "BJT and MOSFET are common semiconductor devices.",

                "Amplifiers increase signal amplitude.",

                "Filters select or reject frequency ranges.",

            ],

        },

        "Digital Electronics": {

            "definition": "Digital electronics represents information using discrete logic levels, commonly 0 and 1.",

            "points": [

                "Basic gates include AND, OR, and NOT.",

                "Combinational circuits depend on present inputs.",

                "Sequential circuits also depend on previous states.",

            ],

        },

        "Communication Systems": {

            "definition": "Communication systems transfer information from a source to a destination through a transmission medium.",

            "points": [

                "A transmitter prepares a signal for transmission.",

                "A channel carries the signal.",

                "A receiver recovers the information.",

                "Common modulation types include AM, FM, and PM.",

            ],

        },

        "Electromagnetic Waves": {

            "definition": "Electromagnetic waves consist of time-varying electric and magnetic fields that propagate through space.",

            "points": [

                "Electric and magnetic fields are mutually perpendicular.",

                "The wavelength-frequency relationship is c = fλ in free space.",

                "Antennas can transmit and receive electromagnetic energy.",

            ],

        },

    }



    selected = topics[topic]



    st.subheader(topic)

    st.write(selected["definition"])



    st.markdown("### Key Points")

    for point in selected["points"]:

        st.write(f"• {point}")



# ============================================================

# ============================================================
# ECE AI ASSISTANT
# ============================================================

elif section == "🤖 ECE AI Assistant":
    st.header("🤖 ECE AI Assistant")

    st.write(
        "Ask an ECE-related question. This assistant uses local Ollama AI and Hindsight memory."
    )

    prompt = st.text_area(
        "Your question",
        height=120,
        placeholder="Example: Explain Kirchhoff's Voltage Law",
    )

    if st.button("Ask ECE AI", key="ai"):
        if not prompt.strip():
            st.warning("Please enter a question first.")
        else:
            memory_text = ""

            try:
                memories = _hindsight_recall(prompt)
                memory_text = "\n".join(
                    item.text for item in memories.results
                    if getattr(item, "text", "").strip()
                )
            except Exception as e:
                st.warning(f"Hindsight recall unavailable: {e}")

            with st.spinner("Thinking..."):
                try:
                    response = requests.post(
                        "http://localhost:11434/api/generate",
                        json={
                            "model": "llama3.2:3b",
                            "prompt": (
                                "You are the ECE Smart Lab Assistant. "
                                "Answer ECE study questions clearly and simply. "
                                "Use formulas and examples when useful. "
                                "This project is a Streamlit-based ECE toolkit using local Ollama and Hindsight memory. "
                                "Use recalled memory only when it is relevant to this ECE Smart Lab project or the current student question. "
                                "Ignore unrelated or conflicting memories.\n\n"
                                f"Relevant Hindsight memory:\n{memory_text}\n\n"
                                f"Student question: {prompt}"
                            ),
                            "stream": False,
                        },
                        timeout=120,
                    )

                    if response.status_code == 200:
                        data = response.json()
                        answer = data.get("response", "").strip()

                        if answer:
                            st.success("AI Response")
                            st.write(answer)

                            # Save the new interaction to Hindsight without
                            # interfering with the answer-generation request.
                            try:
                                _hindsight_retain(
                                    f"Student asked: {prompt}\nAssistant answered: {answer}"
                                )
                            except Exception as e:
                                st.info(f"Answer completed; memory save unavailable: {e}")
                        else:
                            st.warning("The AI returned an empty response.")
                    else:
                        st.error(
                            f"Ollama returned HTTP status {response.status_code}."
                        )

                except requests.exceptions.ConnectionError:
                    st.error(
                        "Could not connect to Ollama. "
                        "Make sure Ollama is running on your computer."
                    )
                except requests.exceptions.Timeout:
                    st.error(
                        "The AI request timed out. "
                        "Please try again after checking Ollama."
                    )
                except Exception as error:
                    st.error(f"Unexpected error: {error}")


# FOOTER

# ============================================================



st.divider()

st.caption("⚡ ECE Smart Lab Assistant • Smart Lab V2")



