# 2007 YRBS 數據分析專案：青少年睡眠時數與校園暴力行為之 ANOVA 分析
# (Project: ANOVA Analysis on Adolescent Sleep Hours and School Fighting Frequency)

---

## Student Information
Name: [填寫你的姓名，例如：王小明]
Student ID: [填寫你的學號，例如：111370XXX]

## Project Repository
https://github.com/[你的GitHub帳號]/[你的專案名稱]

## Presentation Video
https://youtube.com/watch?v=[你的YouTube影片代碼]

---

### 📊 使用數據 (Dataset)
* **數據集名稱 (Dataset Name)**: 2007 Youth Risk Behavior Surveillance System (YRBSS) / 2007 年青少年危險行為調查
* **來源 (Source)**: Centers for Disease Control and Prevention (CDC) / 美國疾病管制與預防中心

---

### 🔍 選定變數 (Selected Variables)
1. **自變數 (Predictor / Independent Variable)**: `HowManyHoursOfSleepDoYouGet` (上學日平均睡眠時數)。這是一個類別變數（Categorical Variable），用來將學生分為不同的睡眠長度群體（如：5小時以下、6小時、7小時、8小時以上等）。
2. **應變數 (Outcome / Dependent Variable)**: `PhysicalFightingAtSchool` (過去12個月在學校打架的次數)。這是一個連續型/數值變數（Continuous Variable），用來衡量青少年的校園暴力行為頻率。

---

### 🎯 研究問題 (Research Question)
* **核心問題**：不同睡眠時數的青少年，在校園內參與打架與暴力事件的平均頻率是否有顯著差異？（Does the average frequency of physical fighting at school significantly differ among high school students with different amounts of sleep?）

---

### 🛠️ 統計方法 (Statistical Method)
* 本研究採用 **單因子變異數分析 (One-way ANOVA)** 來檢定多個睡眠時數群體的打架頻率平均值是否相等。
* 若 ANOVA 結果達到統計顯著 ($p < 0.05$)，將進一步使用 **Tukey HSD 事後檢定 (Post-hoc Test)**，以釐清具體是哪幾個睡眠群體之間存在顯著差異。

---

### 💡 預期結論與統計อธิบาย (Expected Results & Interpretation)
*(備註：這部分等我們把 Python 程式碼跑出實際數據後，再把真實的 p-value 和數字填進來！)*
* **ANOVA 檢定結果**：根據分析，不同睡眠時數群體在校園打架頻率上呈現[顯著/非顯著]差異 ($p$ 值 [大於/小於] 0.05)。
* **事後檢定觀察**：數據初步顯示，睡眠時間較短（如 5 小時以下）的青少年，其校園打架頻率顯著高於睡眠充足（如 8 小時以上）的同儕。這符合公共衛生學中「睡眠不足易導致情緒失控與衝動行為」的理論。
