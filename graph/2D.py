import matplotlib.pyplot as plt
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

# Đọc từ hai file
file1 = 'C:\\Users\\ADMIN\\Downloads\\Projet\\hypersurface\\graph\\E_tot.txt'
file2 = 'C:\\Users\\ADMIN\\Downloads\\Projet\\hypersurface\\graph\\theta_moyen.txt'

dim1, nv1, theta1 = read_data(file1)
dim2, nv2, theta2 = read_data(file2)

# Danh sách các dimension cần vẽ
dims_to_plot = [3, 4, 5]
colors = ['r', 'g', 'b']

plt.figure(figsize=(10, 6))

for d, color in zip(dims_to_plot, colors):
    # Dữ liệu từ file 1
    mask1 = dim1 == d
    nv1_filtered = nv1[mask1]
    theta1_filtered = theta1[mask1]
    sorted_indices1 = np.argsort(nv1_filtered)
    nv1_sorted = nv1_filtered[sorted_indices1]
    theta1_sorted = theta1_filtered[sorted_indices1]

    # Dữ liệu từ file 2
    mask2 = dim2 == d
    nv2_filtered = nv2[mask2]
    theta2_filtered = theta2[mask2]
    sorted_indices2 = np.argsort(nv2_filtered)
    nv2_sorted = nv2_filtered[sorted_indices2]
    theta2_sorted = theta2_filtered[sorted_indices2]

    # Vẽ 2 đường cho mỗi dimension
    plt.plot(nv1_sorted, theta1_sorted, marker='.', color=color, linestyle='-', label=f'D={d} (E_tot)')
    plt.plot(nv2_sorted, theta2_sorted, marker='*', color=color, linestyle='-', label=f'D={d} (theta_moyen)')

plt.xlabel('Nombre de vecteurs')
plt.ylabel('Theta moyen (°)')
plt.title('Comparaison des valeurs de Theta moyen pour D=3, 4, 5')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
