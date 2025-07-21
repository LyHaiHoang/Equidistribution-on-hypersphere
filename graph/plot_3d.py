import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_data(filename):
    D = []
    N = []
    theta_moyen = []
    theta_goc = []
    diff = []

    with open(filename, 'r') as f:
        next(f)  # Bỏ qua header đầu tiên
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split()
            if len(parts) == 5:
                D.append(int(parts[0]))
                N.append(int(parts[1]))
                theta_moyen.append(float(parts[2]))
                theta_goc.append(float(parts[3]))
                diff.append(float(parts[4]))

    return np.array(D), np.array(N), np.array(theta_moyen), np.array(theta_goc), np.array(diff)

def plot_surface(D, N, Z, zlabel='Value', title='3D Surface Plot'):
    # Các giá trị duy nhất để tạo lưới
    D_unique = np.unique(D)
    N_unique = np.unique(N)

    # Tạo lưới 2D cho trục X và Y
    X, Y = np.meshgrid(D_unique, N_unique)

    # Khởi tạo ma trận Z với kích thước lưới
    Z_grid = np.full_like(X, np.nan, dtype=np.float64)

    # Gán giá trị Z từ dữ liệu cho đúng vị trí trên lưới
    for d, n, z_val in zip(D, N, Z):
        i = np.where(N_unique == n)[0][0]
        j = np.where(D_unique == d)[0][0]
        Z_grid[i, j] = z_val

    # Vẽ biểu đồ surface 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z_grid, cmap='viridis', edgecolor='k', linewidth=0.5)

    ax.set_xlabel('Dimension (D)')
    ax.set_ylabel('Number of Vectors (N)')
    ax.set_zlabel(zlabel)
    ax.set_title(title)

    fig.colorbar(surf, shrink=0.5, aspect=10, label=zlabel)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    filename = r'C:\Users\ADMIN\Downloads\Projet\Equidistribution-on-hypersphere\graph\result.dat'

    D, N, theta_moyen, theta_goc, diff = read_data(filename)

    # Vẽ hiệu số góc diff theo D và N
    plot_surface(D, N, diff, zlabel='Theta_theorical - Theta_moyen (°)', title='Difference between Dimension and Number of Vectors')
