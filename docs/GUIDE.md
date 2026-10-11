# 📖 Project Guide — ECE Smart Lab Assistant

Everything about this project, explained from the ground up.

**Repository:** `ece-smart-lab-assistant`
**What it is in one line:** a single web app that does the everyday
calculations and revision an Electronics & Communication Engineering student
needs, in one place.

> **Note:** this is the project that was already on your GitHub before we worked
> together. The app is yours; the documentation here is written to help you
> understand what you built.

---

## 1. What problem does it solve?

As an ECE student you reach for the same handful of things constantly:

- Ohm's law, resistor values for an LED, series and parallel resistance
- Voltage dividers, power dissipation
- Frequency ↔ wavelength, decibels, RC time constants, LC resonance

Normally these live in scattered places: a textbook, a notebook, a phone
calculator, a half-remembered formula. You lose time switching between them,
and you can get a formula subtly wrong.

This app puts all of it behind one page: type the numbers, get the answer
immediately. And because it also carries short concept notes, it doubles as
revision before a lab or an exam.

---

## 2. The big picture

```
        ┌────────────────────────────────────────────┐
        │              app.py (one file)             │
        │   Sidebar navigation:                      │
        │   1. Circuit Calculators                   │
        │   2. ECE Calculators                       │
        │   3. Learn ECE                             │
        │   4. AI Assistant                          │
        │                                            │
        │   Each section: inputs ──► formula ──► answer
        └────────────────────────────────────────────┘
                            │
                            ▼
                    your web browser
```

There is no database and no server to run. It is one Python file that turns
into a web page when Streamlit runs it.

---

## 3. What is inside it

### 🔌 Circuit Calculators
| Tool | What it does |
|---|---|
| Ohm's Law | Given any two of voltage, current and resistance, find the third |
| LED Resistor | Works out the resistor you need to protect an LED |
| Series Resistance | Adds resistances in series |
| Parallel Resistance | Combines resistances in parallel |
| Electrical Power | Power from voltage, current or resistance |
| Voltage Divider | Output voltage of a two-resistor divider |

### 📡 ECE Calculators
| Tool | What it does |
|---|---|
| Frequency ↔ Wavelength | Converts between the two, using the speed of light |
| Decibel | Converts between ratios and decibels |
| RC Time Constant | τ = R × C — how fast a capacitor charges |
| LC Resonant Frequency | The frequency a coil-and-capacitor pair resonates at |

### 📚 Learn ECE
Short concept notes on Basic Electronics, Analog Circuits, Digital
Electronics, Communication Systems and Electromagnetics — for revision.

### 🤖 AI Assistant
An in-app assistant you can ask electronics questions.

---

## 4. Every technology used, and what it is

| Technology | What it actually is | Where it appears |
|---|---|---|
| **Python** | The language the whole app is written in. | `app.py` |
| **Streamlit** | A library that turns a plain Python script into an interactive web page. You write Python; it draws the buttons, inputs and output. **No HTML, CSS or JavaScript needed** — this is why it is the fastest way for a beginner to build a real app. | `app.py` |
| **`math`** | Python's built-in maths module. Provides `pi`, `sqrt`, trigonometry — everything the formulas need. | `app.py` |
| **`requests`** | A library for making web requests. Used by the AI assistant to talk to an external service. | `app.py` |
| **Formulas** | The actual engineering: Ohm's law, τ = RC, f = 1/(2π√(LC)), and so on. | `app.py` |
| **Widgets** | The Streamlit building blocks — text boxes, number inputs, buttons, dropdowns, tabs. | `app.py` |

---

## 5. File-by-file

The whole project is remarkably small:

### `app.py`
Everything. It is organised into four sections, and each calculator follows the
same three-step shape:

1. **Collect inputs** — number boxes for the values
2. **Apply the formula** — ordinary Python arithmetic
3. **Show the result** — print it to the page

Once you have seen one calculator, you have seen them all. That is deliberate:
the structure repeats so it stays easy to add more.

### `requirements.txt`
Just one line — `streamlit`. The app needs nothing else. Note that `math` is
built into Python.

### `README.md`
The front page: features, how to run it, and the roadmap.

---

## 6. How to run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

Your browser opens at `http://localhost:8501`. To stop it, press `Ctrl + C` in
the terminal.

---

## 7. Concepts worth understanding (in this order)

1. **A variable** — `voltage = 5` stores a number under a name
2. **Arithmetic** — `current = voltage / resistance`
3. **A function** — the code that calculates one answer, wrapped up and named
4. **Streamlit's pattern** — you write plain Python, and each `st.something()`
   call draws one thing on the page
5. **The order matters** — Streamlit runs your script from top to bottom, every
   time you interact with the page. That single fact explains most Streamlit
   behaviour.

Item 5 is the one that surprises people. There is no "event handler" you attach
to a button — the whole script simply runs again.

---

## 8. Common problems and what they mean

| Symptom | What is happening | Fix |
|---|---|---|
| `streamlit: command not found` | Streamlit is not installed | `pip install -r requirements.txt` |
| The page is blank | The script hit an error before drawing anything | Look at the terminal — the error is printed there |
| A calculation gives a strange number | Unit mismatch (volts vs millivolts, ohms vs kilohms) | Convert to base units first |
| The AI assistant does not reply | It needs a working internet connection and a service URL | Check your connection; the rest of the app still works |

---

## 9. What you would say about this project in an interview

> "It's a Streamlit toolkit for ECE students — about a dozen calculators plus
> concept notes, in one app. It's a single file, and every calculator follows
> the same input → formula → output shape, which made it easy to keep adding
> tools. It's the project where I learned how Streamlit's re-run model works."

It is the least technically deep project in the portfolio, and that is fine —
**it is the one that is genuinely yours**, and the one you can most easily
explain today. That has value.

---

## 10. Where this project goes next

See the roadmap in the README. The most valuable additions would be:

- A **resistor colour-code tool** — genuinely useful, and a nice bit of logic
- **Screenshots** in the README, so people can see it without running it
- **Deploying it** to Streamlit Community Cloud so it has a live link — a public
  URL is worth more than a repository on its own
