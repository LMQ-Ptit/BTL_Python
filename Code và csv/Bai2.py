import pandas as pd
import numpy as np
from collections import Counter
import os
import time
import seaborn as sns
import matplotlib.pyplot as plt

# Tìm top 3 và bottom 3 cầu thủ cho mỗi chỉ số
def find_top_bottom_players(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    result_top = pd.DataFrame()
    for col in numeric_cols:
        top_3 = df.nlargest(3, col)['Name'].values
        bottom_3 = df.nsmallest(3, col)['Name'].values
        result_top[col] = np.concatenate((top_3, bottom_3))
    print("Top 3 và Bottom 3 cầu thủ cho từng chỉ số:")
    print(result_top)

# Tính toán thống kê trung vị, trung bình, độ lệch chuẩn
def calculate_team_statistics(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    # Thống kê cho toàn giải
    overall_stats = {
        'Team': ['All'],
        **{f'{col}_median': [df[col].median()] for col in numeric_cols},
        **{f'{col}_mean': [df[col].mean()] for col in numeric_cols},
        **{f'{col}_std': [df[col].std()] for col in numeric_cols},
    }
    overall_df = pd.DataFrame(overall_stats)

    # Thống kê cho từng đội
    team_stats = df.groupby('Team')[numeric_cols].agg(['median', 'mean', 'std']).round(2)
    team_stats.columns = [f'{col}_{stat}' for col, stat in team_stats.columns]
    team_stats.reset_index(inplace=True)

    # Kết hợp và lưu kết quả
    final_df = pd.concat([overall_df, team_stats], ignore_index=True)
    # final_df.to_csv('results2.csv', index=False)
    print(final_df)

# Vẽ biểu đồ histogram cho toàn giải và từng đội
def generate_histograms(df):
    def save_histograms(data, folder, title_prefix=""):
        os.makedirs(folder, exist_ok=True)
        for col in data.select_dtypes(include=['number']).columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(data[col], bins=20, kde=True)
            plt.title(f'{title_prefix} {col}')
            plt.xlabel(col)
            plt.ylabel('Số lượng cầu thủ')
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.savefig(os.path.join(folder, f"{col}.png"))
            plt.close()

    save_histograms(df, 'histograms_all', 'Toàn giải -')
    for team in df['Team'].unique():
        save_histograms(df[df['Team'] == team], f"histograms_teams/{team}", f"Đội {team} -")
    print("Đã lưu tất cả biểu đồ histogram.")

# Tìm đội có trung bình cao nhất ở mỗi chỉ số
def identify_best_team(df):
    numeric_cols = df.select_dtypes(include=['number']).columns
    team_means = df.groupby('Team')[numeric_cols].mean()
    best_teams = pd.DataFrame([(col, team_means[col].idxmax(), team_means[col].max()) for col in numeric_cols], columns=['Chỉ số', 'Đội', 'Giá trị'])
    print("Đội có điểm cao nhất cho từng chỉ số:")
    print(best_teams)

    # Đếm số lần xuất hiện của mỗi đội và tìm đội xuất hiện nhiều nhất
    top_team = Counter(best_teams['Đội']).most_common(1)
    print(f"Đội có điểm cao nhất tổng hợp: {top_team[0][0]} với {top_team[0][1]} chỉ số cao nhất.")

# Thực thi các hàm
if __name__ == "__main__":
    df = pd.read_csv("results.csv")
    find_top_bottom_players(df)
    calculate_team_statistics(df)
    # generate_histograms(df)
    identify_best_team(df)
