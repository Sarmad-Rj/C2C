
# 💱 C2C Converter

A mini web application that converts **cryptocurrency prices to local currencies** and supports **currency-to-currency** conversion — built with **Python**, **Streamlit**, and **web scraping**.

> 🚀 My very first complete mini project with both frontend and backend — and it's live!

---

## 🌐 Live Demo

🔗 **[Click here to try it live](https://currency-converter-by-sarmad.streamlit.app/)**

---

## 📌 Features

- 🔁 **Coin to Currency Converter**  
  Get the latest crypto prices (e.g., BTC, ETH, XRP) in your local currency.

- 💱 **Currency to Currency Converter**  
  Convert from one fiat currency (e.g., USD → PKR, EUR → INR).

- 🎮 **Mini Game Page**  
  A fun number guessing game built with Streamlit.

- 📦 **Dynamic UI with Sidebar Navigation**  
  Pages are separated for easy access via the Streamlit sidebar.

- 🌐 **Internet Connection Check**  
  Prevents data fetching if no internet is available.


---

## 🛠️ Tech Stack

- **Frontend**: Streamlit UI components  
- **Backend**: Python, Web Scraping (`requests`, `BeautifulSoup`)  
- **Image Processing**: PIL  
- **Live Deployment**: [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📁 Project Structure

```

C2C/
│
├── main.py                         # Home page (Coin to Currency)
│
├── pages/
│   ├── 1\_Coin\_to\_Currnecy.py     # Coin to Currency Converter
│   ├── 2\_Currnecy\_to\_Currnecy.py # Currency to Currency Converter
│   └── 3\_game.py                   # Game page
│
├── utils/
│   └── shared\_data.py              # Shared lists like currency codes
│
└── requirements.txt                 # Required Python packages

````

---

## 🚧 How It Works

### 📊 Coin to Currency
- Scrapes latest crypto data from **[CoinMarketCap](https://coinmarketcap.com/)**
- Gets real-time conversion rates using **[Google Finance](https://www.google.com/finance)**

### 💱 Currency to Currency
- Allows conversion between fiat currencies (e.g., EUR → PKR)

### 🧠 Game
- A simple interactive number guessing game using `st.number_input()` and `st.toast()`

---

## 📦 Requirements to use

* `Python`
  
but the key libraries are:

* `streamlit`
* `requests`
* `beautifulsoup4`
* `pillow`

---

## 💬 A Note from Me

This is my **first fully functional mini project**, combining:

* Clean UI using Streamlit
* Real-time data from the web
* Python logic for conversions
* Page-based structure for scalability

Deployed and working — and I’m super proud of it! 🎉

---

## 📜 License

This project is open-sourced for learning and practice.
Feel free to fork and build upon it!

