import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def read_data(filename):
    dimensions = []
    n_vectors = []
    thetas = []

    with open(filename, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split()
            if len(parts) == 3:
                dim = int(parts[0])
                nv = int(parts[1])
                theta = float(parts[2])
                dimensions.append(dim)
                n_vectors.append(nv)
                thetas.append(theta)
    
    return np.array(dimensions), np.array(n_vectors), np.array(thetas)

def plot_surface(dimensions, n_vectors, thetas):
    # Lấy các giá trị duy nhất để tạo lưới
    dim_unique = np.unique(dimensions)
    nv_unique = np.unique(n_vectors)

    # Tạo lưới 2D
    X, Y = np.meshgrid(dim_unique, nv_unique)

    # Khởi tạo Z theo cùng kích thước lưới
    Z = np.full_like(X, np.nan, dtype=np.float64)

    # Điền Z theo dữ liệu gốc
    for d, nv, theta in zip(dimensions, n_vectors, thetas):
        i = np.where(nv_unique == nv)[0][0]
        j = np.where(dim_unique == d)[0][0]
        Z[i, j] = theta

    # Vẽ surface
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ surface với shading
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', linewidth=0.5)

    ax.set_xlabel('Dimension')
    ax.set_ylabel('Number of Vectors')
    ax.set_zlabel('Theta (°)')
    ax.set_title('Surface Plot: Minimum angles depending on Dimension and Number of Vectors')

    fig.colorbar(surf, shrink=0.5, aspect=10, label='Theta')
    plt.tight_layout()
    plt.show()

# Đường dẫn file
filename = 'C:\\Users\\ADMIN\\Downloads\\Projet\\equidistribution-on-hypersphere\\graph\\E_tot.txt'
filename_code = 'C:\\Users\\ADMIN\\Downloads\\Projet\\equidistribution-on-hypersphere\\graph\\theta_moyen.txt'

# Đọc và vẽ
dims, nvs, thetas = read_data(filename)
D,N,theta_code = read_data(filename_code)
ecart = theta_code - thetas
plot_surface(dims, nvs, thetas)
plot_surface(D, N, theta_code)
plot_surface(D, N, ecart, zlabel='Écart (°)', title='Difference (Écart = theta_code - theta)')