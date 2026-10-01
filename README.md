# ⚡ ECE Smart Lab Assistant

An interactive electronics toolkit built for Electronics and Communication Engineering (ECE) students. It combines everyday circuit calculators, ECE-specific tools, quick-reference notes, and an AI assistant — all in one beginner-friendly Streamlit app.

## 🎯 The Problem It Solves

ECE students reach for the same handful of calculations and concepts constantly — Ohm's law, resistor selection, RC time constants, decibel conversions — and these are normally scattered across textbooks, notebooks, and half-remembered formulas. This app puts the routine work in one place: run the calculation, read a short concept note, and get back to the lab.

## 🚀 Features

### 🔌 Circuit Calculators
- ⚡ Ohm's Law Calculator (V, I, R)
- 💡 LED Resistor Calculator
- 🔗 Series Resistance Calculator
- 🔗 Parallel Resistance Calculator
- ⚡ Electrical Power Calculator
- 🔋 Voltage Divider Calculator

### 📡 ECE Calculators
- 📡 Frequency ↔ Wavelength Converter
- 📊 Decibel (dB) Calculator
- ⏱️ RC Time Constant Calculator
- 📻 LC Resonant Frequency Calculator

### 📚 Learn ECE
Quick concept notes for:
- Basic Electronics
- Analog Circuits
- Digital Electronics
- Communication Systems
- Electromagnetics

### 🤖 AI Assistant
An in-app assistant to answer electronics questions.

## 🏗️ How It Works

The app is a single Streamlit script (`app.py`) organised into four sections that you move between in the sidebar:

1. **Circuit Calculators** — everyday component and circuit maths
2. **ECE Calculators** — frequency, decibel, and time-constant tools
3. **Learn ECE** — short concept notes for revision
4. **AI Assistant** — ask electronics questions in plain language

Each calculator takes your inputs, applies the standard formula, and shows the result immediately — no page reloads, no setup.

## 🛠️ Technologies Used

- Python
- Streamlit

## 📦 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/gshivaprasad0009-gana/ece-smart-lab-assistant.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

## 🗺️ Future Improvements

- [ ] Add more calculators (filters, impedance, antenna basics)
- [ ] Unit conversion helper (resistor color codes, dBm ↔ mW)
- [ ] ESP32 / IoT experiment helpers
- [ ] Add screenshots and a short demo GIF to this README
- [ ] Deploy as a live web app so it can be used without installing anything

## 🤝 Contributing

Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## ✍️ Author

**Ganamolla Shiva Prasad** — B.Tech ECE student, learning and building in Python, AI/ML, and embedded systems.
