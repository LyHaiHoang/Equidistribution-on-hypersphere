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

def create_grid(dimensions, n_vectors, thetas):
    dim_unique = np.unique(dimensions)
    nv_unique = np.unique(n_vectors)
    X, Y = np.meshgrid(dim_unique, nv_unique)
    Z = np.full_like(X, np.nan, dtype=np.float64)

    for d, nv, theta in zip(dimensions, n_vectors, thetas):
        i = np.where(nv_unique == nv)[0][0]
        j = np.where(dim_unique == d)[0][0]
        Z[i, j] = theta

    return X, Y, Z

# Đường dẫn file
filename_real = 'C:\\Users\\ADMIN\\Downloads\\Projet\\equidistribution-on-hypersphere\\graph\\E_tot.txt'
filename_code = 'C:\\Users\\ADMIN\\Downloads\\Projet\\equidistribution-on-hypersphere\\graph\\theta_moyen.txt'

# Đọc dữ liệu
dims1, nvs1, thetas1 = read_data(filename_real)
dims2, nvs2, thetas2 = read_data(filename_code)

# Tạo grid
X1, Y1, Z1 = create_grid(dims1, nvs1, thetas1)
X2, Y2, Z2 = create_grid(dims2, nvs2, thetas2)

# Vẽ
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface 1: dữ liệu thực
surf1 = ax.plot_surface(X1, Y1, Z1, cmap='viridis', alpha=0.7, edgecolor='k', label='Theory')
fig.colorbar(surf1, shrink=0.5, aspect=10, label='Theory theta')
# Surface 2: dữ liệu từ code
surf2 = ax.plot_surface(X2, Y2, Z2, cmap='plasma', alpha=0.7, edgecolor='k', label='Experiment')
fig.colorbar(surf2, shrink=0.5, aspect=10, label='Experiment theta')

# Nếu muốn dùng scatter thay cho surface:
# ax.scatter(dims1, nvs1, thetas1, color='blue', label='Thực nghiệm')
# ax.scatter(dims2, nvs2, thetas2, color='red', label='Mô phỏng')

ax.set_xlabel('Dimension')
ax.set_ylabel('Vectors number')
ax.set_zlabel('Theta (°)')
ax.set_title('Comparison of Theta values from Theory and Experiment')

# Tạo legend bằng custom lines nếu dùng surface
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='blue', lw=4, label='Experiment'),
    Line2D([0], [0], color='orange', lw=4, label='Theory')
]
ax.legend(handles=legend_elements, loc='upper left')

plt.tight_layout()
plt.show()
