import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ==========================================
# STEP 1: 資料準備與清洗 (Data Preparation)
# ==========================================
print("=== Step 1: Starting Data Preparation ===")

# 檢查原始檔案是否存在
if not os.path.exists('YRBS_2007.csv'):
    raise FileNotFoundError("錯誤：找不到 'YRBS_2007.csv' 檔案，請確認它與此程式碼放在同一個資料夾！")

# 1. 讀取原始資料
df = pd.read_csv('YRBS_2007.csv')
print(f"成功載入原始數據，共計 {len(df)} 筆資料。")

# 2. 篩選研究變數：Sleep (自變數 X) 與 PhysicalFightingAtSchool (因變數 Y)
columns_of_interest = ['Sleep', 'PhysicalFightingAtSchool']
processed_df = df[columns_of_interest].copy()

# 3. 移除缺失值 (NaN)
processed_df = processed_df.dropna()

# 4. 資料重編碼 (Recoding)：對照 YRBS 官方定義將數值映射至文字標籤
sleep_mapping = {
    1.0: "4 hours or less",
    2.0: "5 hours",
    3.0: "6 hours",
    4.0: "7 hours",
    5.0: "8 hours",
    6.0: "9 hours",
    7.0: "10 hours or more"
}
processed_df['Sleep_Group'] = processed_df['Sleep'].map(sleep_mapping)

# 再次確認移除無法成功映射的異常資料
processed_df = processed_df.dropna(subset=['Sleep_Group'])
print(f"資料清洗完成！有效觀測值共計 {len(processed_df)} 筆。")

# 5. 導出教授要求的 processed_data.csv 檔案
processed_df.to_csv('processed_data.csv', index=False)
print("🎉 成功導出 'processed_data.csv' 檔案！")


# ==========================================
# STEP 2: 描述性統計 (Descriptive Statistics)
# ==========================================
print("\n=== Step 2: Generating Descriptive Statistics ===")

# 定義睡眠群組在圖表與統計上的標準順序（由少到多）
sleep_order = [
    "4 hours or less", "5 hours", "6 hours", 
    "7 hours", "8 hours", "9 hours", "10 hours or more"
]

# 計算各組的樣本數、平均值與標準差
summary_stats = processed_df.groupby('Sleep_Group')['PhysicalFightingAtSchool'].agg(['count', 'mean', 'std']).reindex(sleep_order)
print(summary_stats)


# ==========================================
# STEP 3: 數據視覺化 (Data Visualization)
# ==========================================
print("\n=== Step 3: Generating Visualizations ===")

# 設定 Seaborn 圖表風格
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# 繪製盒狀圖 (Boxplot)
sns.boxplot(
    x='Sleep_Group', 
    y='PhysicalFightingAtSchool', 
    data=processed_df, 
    order=sleep_order,
    palette="coolwarm"
)

# 加上圖表標題與軸標籤
plt.title('School Physical Fighting Frequency Across Different Sleep Durations', fontsize=14, fontweight='bold')
plt.xlabel('Sleep Duration per Night', fontsize=12)
plt.ylabel('Physical Fighting at School (Frequency Score)', fontsize=12)
plt.xticks(rotation=15)

# 儲存高品質圖檔（上傳 GitHub 與製作一頁式簡報用）
plt.tight_layout()
plt.savefig('sleep_vs_violence_boxplot.png', dpi=300)
print("🎉 統計圖表已成功繪製並儲存為 'sleep_vs_violence_boxplot.png'！")
plt.show()


# ==========================================
# STEP 4: 變異數分析 (One-Way ANOVA)
# ==========================================
print("\n=== Step 4: Running One-Way ANOVA ===")

# 建立普通最小二乘法 (OLS) 模型
model = ols('PhysicalFightingAtSchool ~ C(Sleep_Group)', data=processed_df).fit()

# 計算 ANOVA 表格
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# 提取並判斷 P 值是否顯著
p_value = anova_table['PR(>F)'][0]
f_statistic = anova_table['F'][0]

print("\n--------------------------------------------------")
print(f"F-Statistic: {f_statistic:.4f}")
print(f"P-Value: {p_value:.5e}")

if p_value < 0.05:
    print("結果判斷: 具備統計學上的顯著差異 (p < 0.05)！")
    print("我們拒絕虛無假設 (Reject H0)。這代表不同的睡眠時間確實會顯著影響青少年在校園打架的頻率。")
else:
    print("結果判斷: 無顯著差異 (p >= 0.05)。")
    print("無法拒絕虛無假設。")
print("--------------------------------------------------")


# ==========================================
# STEP 5: 事後檢定 (Post-Hoc Tukey HSD)
# ==========================================
if p_value < 0.05:
    print("\n=== Step 5: Running Post-Hoc Tukey HSD Test ===")
    
    # 執行 Tukey HSD 檢定
    tukey_results = pairwise_tukeyhsd(
        endog=processed_df['PhysicalFightingAtSchool'],
        groups=processed_df['Sleep_Group'],
        alpha=0.05
    )
    
    # 打印前 2000 個字元的結果避免洗版，重點關注 'reject' 欄位是否為 True
    print(str(tukey_results)[:2000])
    print("\n🎉 全自動統計工作流執行完畢！所有輸出與圖表已就緒。")

    # 設定圖表風格
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 繪製平均值與 95% 信賴區間圖
sns.pointplot(
    x='Sleep_Group', 
    y='PhysicalFightingAtSchool', 
    data=processed_df, 
    order=sleep_order,
    color="#cb4335",      # 使用醒目的紅色
    errorbar=('ci', 95),  # 顯示 95% 信賴區間
    capsize=0.1,          # 區間頂端加短橫線
    markers="o",          # 數據點標記
    linestyles="-"        # 點與點之間用線連起來
)

# 加上圖表標題與軸標籤
plt.title('Mean School Physical Fighting Frequency by Sleep Duration (with 95% CI)', fontsize=14, fontweight='bold')
plt.xlabel('Sleep Duration per Night', fontsize=12)
plt.ylabel('Average Physical Fighting Score', fontsize=12)
plt.xticks(rotation=20)

# 儲存高品質圖檔（這張圖非常適合放在一頁式簡報的精華區！）
plt.tight_layout()
plt.savefig('sleep_vs_violence_mean_trend.png', dpi=300)
plt.show()

# 修改後的折線圖程式碼片段
plt.figure(figsize=(10, 6))
sns.pointplot(
    x='Sleep_Group', 
    y='PhysicalFightingAtSchool', 
    data=processed_df, 
    order=sleep_order,
    color="#cb4335",
    errorbar=('ci', 95),
    capsize=0.1
)
plt.ylim(1.0, 2.0) # 👈 加上這行，固定 Y 軸範圍，圖表就不會看起來波動過於誇張了！
plt.title('Mean School Physical Fighting Frequency by Sleep Duration', fontsize=14, fontweight='bold')
plt.show()
