import pandas as pd
import numpy as np

# 1. 讀取原始資料集
try:
    df = pd.read_csv('YRBS_2007.csv')
    print(f"成功讀取原始資料！原始資料筆數：{len(df)}")
except FileNotFoundError:
    print("錯誤：找不到 'YRBS_2007.csv' 檔案，請確認該檔案與此 Python 檔案在同一個資料夾內。")

# 2. 挑選本研究關注的欄位
# Sleep: 睡眠時數 (自變數 X)
# PhysicalFightingAtSchool: 校園打架頻率 (因變數 Y)
columns_to_keep = ['Sleep', 'PhysicalFightingAtSchool']
processed_df = df[columns_to_keep].copy()

# 3. 資料清洗：移除任一欄位有缺失值 (NaN) 的資料列
processed_df = processed_df.dropna()
print(f"移除缺失值後，剩餘有效資料筆數：{len(processed_df)}")

# 4. 資料重編碼 (Recoding)：建立易讀的睡眠時數群組標籤
# 根據 YRBS 官方 Codebook 的數值定義進行對應
sleep_mapping = {
    1.0: "4 hours or less",
    2.0: "5 hours",
    3.0: "6 hours",
    4.0: "7 hours",
    5.0: "8 hours",
    6.0: "9 hours",
    7.0: "10 hours or more"
}

# 新增一欄 'Sleep_Group' 作為 ANOVA 的分類依據
processed_df['Sleep_Group'] = processed_df['Sleep'].map(sleep_mapping)

# 再次移除無法成功對應（例如數值異常或超出定義範圍）的缺失值
processed_df = processed_df.dropna(subset=['Sleep_Group'])

# 5. 檢查清洗與處理後的資料結構
print("\n--- 經處理後的資料前五筆預覽 ---")
print(processed_df.head())

print("\n--- 各睡眠群體的資料計數 ---")
print(processed_df['Sleep_Group'].value_counts())

# 6. 核心任務：匯出成 processed_data.csv
processed_df.to_csv('processed_data.csv', index=False)
print("\n🎉 成功！'processed_data.csv' 已成功生成並儲存至你的資料夾中。")