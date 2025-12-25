# House Price Prediction using Machine Learning

A machine learning project that predicts house prices based on housing and socio-economic features.  
The project demonstrates a complete ML workflow including data analysis, preprocessing, model training, and evaluation.

---

## Project Objective

To build a **regression-based machine learning model** that can estimate house prices using structured housing data and analyze the influence of different features on price prediction.

---

## Project Structure

## Project Structure

```text
housepriceprediction/
├── app.py                  # Flask web application
├── main.ipynb              # EDA, preprocessing, training & evaluation
├── main.py                 # Model training script
├── model/
│   └── model.pkl           # Trained ML model
├── data/
│   └── housingdata.csv     # Dataset
├── templates/
│   └── index.html          # Web UI
├── requirements.txt
├── README.md
└── LICENSE

```

---

## Model Used

- **Linear Regression** (baseline supervised regression model)

The model learns linear relationships between features and housing prices.

---

## Technologies & Tools
### Programming & Libraries
- Python 3.14
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Flask

### Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

##  Environment Setup

### Clone the Repository

```bash
git clone https://github.com/PranabSantra45/housepriceprediction.git
cd housepriceprediction

```

---

### venv setup

```bash
python -m venv boston

```

### venv activate

```bash
boston\Scripts\activate

```

---

## installation:
  ```bash
  pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

## run_project:
  start_jupyter:
    command: jupyter notebook
  open_notebook:
    file: main.ipynb

---

## run the web-app:
```bash
python app.py

---

