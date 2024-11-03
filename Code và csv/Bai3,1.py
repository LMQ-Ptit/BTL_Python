import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Hàm vẽ biểu đồ K-means
def plot_clusters(data_points, centroid_points, cluster_labels, num_clusters):
    plt.figure(figsize=(8, 6))

    # Màu sắc ngẫu nhiên cho các cụm
    colors = plt.cm.get_cmap('viridis', num_clusters)

    for cluster_index in range(num_clusters):
        # Lấy các điểm thuộc cụm cluster_index
        cluster_points = data_points[cluster_labels == cluster_index]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], s=50, color=colors(cluster_index), label=f'Cụm {cluster_index}')
        # Vẽ tâm cụm
        plt.scatter(centroid_points[cluster_index, 0], centroid_points[cluster_index, 1], s=200, color=colors(cluster_index), marker='X', edgecolor='k')

    plt.title('K-means Phân cụm các cầu thủ bóng đá')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    plt.show()

# Hàm chuẩn bị dữ liệu
def prepare_data(file_path):
    # Đọc dữ liệu và xử lý giá trị thiếu
    data_frame = pd.read_csv(file_path)
    data_frame = data_frame.select_dtypes(exclude=['object'])
    data_frame.fillna(data_frame.mean(), inplace=True)
    
    # Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_frame)

    # Giảm chiều với PCA
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(standardized_data)

    return pd.DataFrame(reduced_data, columns=['PC1', 'PC2'])

# Hàm chạy K-means tùy chỉnh
def kmeans_custom(data_frame, num_clusters, max_iterations=100):
    # Khởi tạo tâm cụm ngẫu nhiên
    centroid_points = data_frame.sample(n=num_clusters).values
    cluster_labels = np.zeros(len(data_frame))

    for _ in range(max_iterations):
        # Gán nhãn cụm cho từng điểm
        for point_index in range(len(data_frame)):
            distances = np.linalg.norm(data_frame.values[point_index] - centroid_points, axis=1)
            cluster_labels[point_index] = np.argmin(distances)
        
        # Cập nhật tâm cụm mới
        new_centroid_points = np.array([data_frame.values[cluster_labels == cluster_index].mean(axis=0) for cluster_index in range(num_clusters)])
        
        # Kiểm tra sự hội tụ
        if np.all(centroid_points == new_centroid_points):
            break
        
        centroid_points = new_centroid_points

    # Vẽ biểu đồ kết quả cuối cùng
    plot_clusters(data_frame.values, centroid_points, cluster_labels, num_clusters)

# Chạy chương trình chính
if __name__ == "__main__":
    file_path = 'results.csv'
    prepared_data = prepare_data(file_path)
    num_clusters = 5  # Số cụm mong muốn
    kmeans_custom(prepared_data, num_clusters)
