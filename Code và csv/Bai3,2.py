import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

# Hàm tải dữ liệu từ file CSV
def load_csv_data(file_path):
    return pd.read_csv(file_path)

# Hàm vẽ biểu đồ radar cho hai cầu thủ
def create_radar_chart(data_frame, player1_name, player2_name, attribute_list):
    # Lọc dữ liệu cho từng cầu thủ
    player1_data = data_frame[data_frame['Name'] == player1_name]
    player2_data = data_frame[data_frame['Name'] == player2_name]

    # Kiểm tra nếu không tìm thấy cầu thủ
    if player1_data.empty or player2_data.empty:
        print("Không tìm thấy cầu thủ hoặc sai tên.")
        return

    # Lấy giá trị các thuộc tính
    player1_values = player1_data[attribute_list].values.flatten()
    player2_values = player2_data[attribute_list].values.flatten()

    # Xây dựng góc của biểu đồ radar
    num_attributes = len(attribute_list)
    angles = np.linspace(0, 2 * np.pi, num_attributes, endpoint=False).tolist()

    # Hoàn thành vòng radar
    player1_values = np.concatenate((player1_values, [player1_values[0]]))
    player2_values = np.concatenate((player2_values, [player2_values[0]]))
    angles += angles[:1]

    # Vẽ biểu đồ
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, player1_values, color='blue', alpha=0.25)
    ax.fill(angles, player2_values, color='red', alpha=0.25)
    ax.plot(angles, player1_values, color='blue', linewidth=2, label=player1_name)
    ax.plot(angles, player2_values, color='red', linewidth=2, label=player2_name)

    # Cấu hình các nhãn thuộc tính
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attribute_list)
    plt.title(f"So sánh chỉ số giữa {player1_name} và {player2_name}")
    plt.legend(loc='upper right')
    plt.show()

# Chạy chương trình chính
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vẽ biểu đồ radar so sánh cầu thủ")
    parser.add_argument("--p1", type=str, required=True, help="Tên cầu thủ thứ nhất")
    parser.add_argument("--p2", type=str, required=True, help="Tên cầu thủ thứ hai")
    parser.add_argument("--Attribute", type=str, required=True, help="Danh sách các chỉ số cần so sánh, cách nhau bởi dấu phẩy")
    args = parser.parse_args()

    # Chuyển đổi chuỗi các thuộc tính thành danh sách
    attribute_list = [attribute.strip() for attribute in args.Attribute.split(",")]

    # Đọc dữ liệu và vẽ biểu đồ
    player_data = load_csv_data("results.csv")
    create_radar_chart(player_data, args.p1, args.p2, attribute_list)

    # Cú pháp chạy chương trình
    # C:/Users/luong/AppData/Local/Programs/Python/Python312/python.exe Bai3,2.py --p1 "Aaron Cresswell" --p2 "Aaron Ramsdale" --Attribute "Goals, Assists1, Minutes"
