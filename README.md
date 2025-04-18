# 🏃‍♀️ Apple Running Training Data Analysis

This project analyzes **weekly training trends** in preparation for a half marathon using a CSV export from a personal running tracker. It visualizes key metrics such as **weekly mileage**, **average pace**, and **cadence trends** over time.

## 📁 Dataset
- `JordinHalfMarathonTr_DATA_LABELS_2024-12-30_0040.csv`
- Exported from personal running data tracking app
- Key columns:
  - `Date`: Date of the run
  - `Distance`: Distance covered (in miles)
  - `Pace`: Average pace in `mm:ss` format
  - `Cadence`: Steps per minute

---

## 🧰 Technologies Used

- **Python** 3.x
- **Pandas** for data manipulation
- **Matplotlib** for visualizations
- **NumPy** for numerical operations

---

## 📊 Analyses Performed

### 📅 Weekly Mileage
Grouped run data by week to compute total distance covered per week and visualize progress.

<img width="708" alt="image" src="https://github.com/user-attachments/assets/3532a231-53e9-4102-81ec-816e2f4b2925" />


---

### ⏱️ Weekly Average Pace
Converted pace from `mm:ss` to total seconds to compute weekly average pace and plotted the pace trend over time.

<img width="732" alt="image" src="https://github.com/user-attachments/assets/b4a0fcfb-9057-413c-9aef-9c4e89cb07c0" />

---

### 👣 Weekly Average Cadence
Analyzed cadence data to show trends in steps per minute, an indicator of running form and performance.

<img width="717" alt="image" src="https://github.com/user-attachments/assets/efb3ca08-7d9e-4cf8-91fb-41703de4e1c4" />

---

## 📈 Key Functions

- `pace_to_seconds()`: Converts pace strings like `"10:30"` to total seconds (e.g., `630`)
- `seconds_to_pace()`: Converts total seconds back into `"mm:ss"` format for labeling

---

## 📌 Sample Visual Output

- Line charts with annotations for:
  - Total mileage each week
  - Weekly average pace (in mm:ss)
  - Weekly average cadence

---

## ✅ Future Enhancements

- Add more metrics such as **heart rate**, **elevation**, or **run type (easy/tempo/long)** if available
- Integrate with **Strava API** or **Nike Run Club** for automatic data pulls
- Build an interactive dashboard using **Plotly** or **Streamlit**

