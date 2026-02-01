# 🌍 Countries CLI Tool (Python)

A lightweight **Python command-line application** that fetches country information such as **population** and **currency details** using the **RestCountries API**.

This project was built to practice working with APIs, parsing JSON, and handling nested dictionaries in Python.

---

## ✨ Features

- 📊 Count the total number of countries
- 🌎 Get detailed information about a specific country:
  - Country name
  - Population
  - Currency name and symbol
- 🖥 Simple command-line interface (CLI)
- 🔗 Uses live data from a public REST API

---

## 🛠 Technologies Used

- Python 3
- requests
- RestCountries API
- Standard libraries: `json`, `sys`

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/countries-cli.git
cd countries-cli
pip install requests
```

---

## 🚀 Usage

### Count all countries
```bash
python countries.py count
```

### Get information about a country
```bash
python countries.py info brazil
python countries.py info "united states"
```

---

## 🖨 Example Output

```text
Country: Brazil
Population: 213421037
Currency: Brazilian real (R$)
```

---

## 🧠 What This Project Demonstrates

- Making HTTP requests in Python
- Parsing JSON responses
- Navigating nested dictionaries and lists
- Building a simple but functional CLI application
- Writing reusable helper functions

---

## 📈 Possible Improvements

- Add a `list` command to show all countries
- Handle multiple currencies more elegantly
- Add caching to reduce API calls
- Improve error handling
- Package as an installable CLI tool

---

## 📜 License

This project is open-source and available under the MIT License.

---

Author: **Arthur Hoffmann**
