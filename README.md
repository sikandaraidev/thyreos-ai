```markdown
# 🧠 ThyreosAI — Clinical Thyroid Risk Predictor

**ThyreosAI** is a machine learning–powered clinical decision support tool that predicts thyroid conditions based on patient data. Built for reliability and ease of integration in healthcare environments, it provides accurate risk classification to assist clinicians and researchers.

---

## 🚀 Features

- ✅ Cleaned & preprocessed dataset from UCI ML Repository (via Kaggle)
- 🧪 Trained multi-class classifier on selected clinical features
- ⚙️ RESTful API using FastAPI for real-time predictions
- 🔐 Secure session-based access (ready for extension with auth)
- 📊 Confidence scoring and interpretable output labels
- 🖥️ UI-friendly response structure for frontend integration

---

## 📦 Tech Stack

- **Backend**: Python, FastAPI, Pydantic
- **ML**: scikit-learn, NumPy, pandas
- **Frontend**: Cursor (AI-generated UI)
- **Deployment**: Designed for Heroku, Vercel, or local use
- **Dataset**: UCI Thyroid Disease Dataset (Kaggle version)

---

## 🧬 Prediction Classes

| Class ID | Label     | Meaning                            |
|----------|-----------|------------------------------------|
| 0        | Negative  | No thyroid disorder detected       |
| 1        | Hypo      | Hypothyroidism detected            |
| 2        | Hyper     | Hyperthyroidism detected           |
| 3        | Other     | Other thyroid-related abnormalities|
| 4        | Misc      | Miscellaneous/uncertain conditions |



---

## 📈 Example API Usage

**Endpoint:** `POST /predict/`  
**Payload:**

```json
{
  "age": 45,
  "sex": 1,
  "on_thyroxine": 1,
  "TSH": 2.4,
  "T3": 1.5,
  "TT4": 110.0,
  "T4U": 1.0,
  "FTI": 105.0,
  "referral_source": 2
}
````

**Response:**

```json
{
  "prediction": 1,
  "label": "hypo",
  "confidence": 0.92
}
```

---

## 📚 Dataset

This project uses a preprocessed version of the [Thyroid Disease Dataset](https://archive.ics.uci.edu/ml/datasets/thyroid+disease) from the UCI Machine Learning Repository. The dataset was cleaned (missing values removed), categorical features encoded, and diagnosis labels grouped into meaningful classes based on clinical literature.

---

## 📌 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/thyreos-ai
cd thyreos-ai

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```

---

## 📖 License

This project is licensed under the CC BY-NC License.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Please open an issue to discuss before submitting a pull request.

---

## 👨‍⚕️ About

ThyreosAI was developed as part of an academic–clinical initiative to explore how machine learning can support early thyroid risk prediction using publicly available health data. The tool is intended to assist clinicians in fast, explainable triaging of thyroid-related conditions while being accessible for researchers and data scientists.

📊 Kaggle Dataset: [ThyreosAI: Cleaned Thyroid Risk Dataset](https://www.kaggle.com/datasets/sikandaraidev/thyroid-dataset)

🔗 LinkedIn: [Sikandar Khan](https://www.linkedin.com/in/sikandaraidev/)

We encourage clinicians, researchers, and developers to experiment, share feedback, and build upon this work to enhance clinical decision support systems.

