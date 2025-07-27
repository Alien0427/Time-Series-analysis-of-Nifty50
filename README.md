# NIFTY50 Time Series Analysis & Forecasting Dashboard

A comprehensive **Streamlit** application for interactive analysis and forecasting of *NIFTY-50* stock prices using both classical statistical models and modern deep-learning techniques.

---

## ✨ Key Features

• **Multiple forecasting models**  
&nbsp;&nbsp;▫️ *Long Short-Term Memory (LSTM)* neural network  
&nbsp;&nbsp;▫️ *ARIMA* (Auto-Regressive Integrated Moving Average)  
&nbsp;&nbsp;▫️ *SARIMA* (Seasonal ARIMA)  
&nbsp;&nbsp;▫️ *Facebook Prophet*

• **Technical indicators & charts**  
&nbsp;&nbsp;▫️ Rolling mean / standard deviation  
&nbsp;&nbsp;▫️ Bollinger Bands  
&nbsp;&nbsp;▫️ Seasonal decomposition  
&nbsp;&nbsp;▫️ Cumulative returns

• **Side-by-side model comparison** for 30-day forecasts with automatic CSV download.

• Modern, responsive **Streamlit** UI with custom styling.

---

## 🗂️ Project Structure

```
├── app.py                # Archived experimental Streamlit app (commented)
├── streamlit_code.py     # Main Streamlit dashboard (recommended entry-point)
├── Arima.py              # ARIMA helper functions
├── Sarims.py             # SARIMA helper functions
├── Lstm_model.py         # LSTM model utilities
├── prophet_model.py      # Prophet model utilities
├── rolling_statistics.py # Rolling mean / std plots
├── bollinger_band.py     # Bollinger Band plots
├── comulative_return.py  # Cumulative return plots
├── Seasonal.py           # Seasonal decomposition helper
├── Select_symbol.py      # Utility to filter symbol data
├── requirement.txt       # Python dependencies
└── README.md             # Project documentation (you are here)
```

---

## 🚀 Quick Start

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd -Time_seires_analysis-
   ```

2. **Create & activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirement.txt
   ```

4. **Add dataset**

   Place your historical NIFTY-50 CSV file (e.g. `NIFTY50_all.csv`) in a location of your choice and update the hard-coded path inside `streamlit_code.py` / `app.py` if necessary.

5. **Run the dashboard**

   ```bash
   streamlit run streamlit_code.py
   ```

6. Open the provided local URL in your browser to explore analyses & forecasts.

---

## ⚙️ Configuration

If your CSV filename or path differs, edit the `load_data()` function in `streamlit_code.py` (and `app.py` if you intend to use it). Ensure the dataframe contains at least the following columns:

- `Date` (YYYY-MM-DD)
- `Symbol` (stock ticker)
- `Close` (closing price)
- `Volume` (quantity traded) – optional but recommended

---

## 📝 Contributing

Pull requests are welcome! Feel free to open issues for bugs, questions, or feature requests.

---

## 📄 License

This project is released under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

Devananditha V

---

## 🤝 Acknowledgements

- [Streamlit](https://streamlit.io)
- [Facebook Prophet](https://github.com/facebook/prophet)
- [Statsmodels](https://www.statsmodels.org)
- [TensorFlow / Keras](https://www.tensorflow.org)
- [Scikit-learn](https://scikit-learn.org)

