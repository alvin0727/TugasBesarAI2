# 🧠 Fuzzy Logic for GERD Defuzzification Result

This project uses **Fuzzy Logic** to model and defuzzify the results for **Gastroesophageal Reflux Disease (GERD)**. Fuzzy Logic is a powerful tool for handling uncertainty and imprecise data, making it ideal for medical applications like GERD diagnosis and analysis.

![Algorithm Fuzzy Visualizer](https://github.com/alvin0727/TugasBesarAI2/blob/main/static/tabel_akhir.png)
---

# 📖 About the Project

## What is GERD?
Gastroesophageal Reflux Disease (GERD) is a chronic condition where stomach acid flows back into the esophagus, causing symptoms like heartburn, regurgitation, and discomfort. Fuzzy Logic is used to model the severity of GERD based on input parameters like:

- **Frequency of heartburn**
- **Intensity of regurgitation**
- **Duration of symptoms**

---

## How Fuzzy Logic Works
Fuzzy Logic allows us to handle the **uncertainty** and **vagueness** in medical data. The process involves:

1. **Fuzzification**: Convert crisp inputs (e.g., symptom severity) into fuzzy sets.
2. **Inference**: Apply fuzzy rules to determine the output (e.g., GERD severity).
3. **Defuzzification**: Convert the fuzzy output into a crisp value for interpretation.

---

## 📊 Visualization

The project uses **Matplotlib** to visualize:

- **Membership functions** for input and output variables.
- **The defuzzification process** (e.g., centroid calculation on the output fuzzy set).

---

## 🚀 Running the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alvin0727/TugasBesarAI2.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd your-repo
   ```
3. **Set up the environment and install dependencies**:
   ```bash
   py -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Run the Flask app**:
   ```bash
   flask --app main run
   ```
5. Open your browser and go to http://127.0.0.1:5000 to interact with the application.

---

## 🎉 Conclusion

This project demonstrates the power of **Fuzzy Logic** in modeling and analyzing complex medical conditions like **GERD**. By combining **Fuzzy Logic** with tools like **Matplotlib** and **Flask**, we’ve created an interactive and intuitive system for defuzzifying GERD severity results. This approach can be extended to other medical applications, providing a robust framework for handling uncertainty and imprecise data.

Thank you for exploring this project! If you have any questions, suggestions, or feedback, feel free to reach out. Your support and interest are greatly appreciated! 😊

---

## 🙏 Thank You!

We hope this project has been insightful and useful. Happy coding! 🚀