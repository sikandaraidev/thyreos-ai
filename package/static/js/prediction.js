const interpretationMap = {
  "negative": {
    interpretation: "No signs of thyroid dysfunction were detected based on your input data.",
    recommendation: "No immediate action is needed. Routine monitoring is still important, especially if symptoms arise or persist."
  },
  "hypothyroid": {
    interpretation: "Indicators suggest an underactive thyroid (hypothyroidism), where the thyroid gland may not produce enough hormones.",
    recommendation: "Please consult your physician. Blood tests like TSH, T4, and T3 should be confirmed. Early treatment often involves hormone replacement therapy."
  },
  "hyperthyroid": {
    interpretation: "Your input suggests signs of an overactive thyroid (hyperthyroidism), which may cause symptoms like anxiety, rapid heartbeat, or weight loss.",
    recommendation: "It's important to speak with a healthcare provider. Further testing can confirm this and guide treatment such as medication or radioactive iodine."
  },
  "other": {
    interpretation: "A thyroid-related anomaly was detected, but it doesn't clearly fit common categories like hypo- or hyperthyroidism.",
    recommendation: "This result warrants further clinical investigation. Please follow up with your doctor for more comprehensive evaluation."
  },
  "miscellaneous": {
    interpretation: "The model detected patterns not typical of known thyroid disorders—this could be due to atypical values or incomplete data.",
    recommendation: "Consider retesting or providing more complete clinical data. Always consult a medical professional for accurate diagnosis."
  }
};

document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('predictionForm');
  const resultDiv = document.getElementById('predictionResult');
  if (form) {
    form.addEventListener('submit', async function(e) {
      e.preventDefault();
      // Collect form data
      const data = {
        age: parseInt(document.getElementById('age').value, 10),
        sex: parseInt(document.getElementById('sex').value, 10),
        on_thyroxine: parseInt(document.getElementById('on_thyroxine').value, 10),
        referral_source: parseInt(document.getElementById('referral_source').value, 10),
        TSH: parseFloat(document.getElementById('TSH').value),
        T3: parseFloat(document.getElementById('T3').value),
        TT4: parseFloat(document.getElementById('TT4').value),
        T4U: parseFloat(document.getElementById('T4U').value),
        FTI: parseFloat(document.getElementById('FTI').value)
      };
      // Send to backend
      try {
        const response = await fetch('/predict', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });
        if (!response.ok) throw new Error('Prediction failed');
        const result = await response.json();
        // Show result
        document.getElementById('diagnosisBadge').textContent = result.label || '';
        document.getElementById('resultText').textContent = result.label || '-';
        document.getElementById('confidenceBar').style.width = (result.confidence * 100).toFixed(2) + '%';
        document.getElementById('confidenceText').textContent = (result.confidence * 100).toFixed(2) + '%';
        // Use interpretation map (case-insensitive)
        const labelKey = (result.label || '').toLowerCase();
        const interp = interpretationMap[labelKey] || {};
        document.getElementById('interpretationText').textContent = interp.interpretation || '';
        document.getElementById('recommendationsList').innerHTML = interp.recommendation
          ? `<li>${interp.recommendation}</li>` : '';
        resultDiv.style.display = 'block';
        resultDiv.scrollIntoView({behavior: 'smooth'});
      } catch (err) {
        alert('Prediction failed. Please try again.');
      }
    });
  }
}); 