import numpy as np
import matplotlib.pyplot as plt

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

def plot_2d_lines(D, N, Z, Ds_to_plot=[3,4,5], zlabel='Value', title='2D Line Plot'):
    plt.figure(figsize=(10,6))
    for d_val in Ds_to_plot:
        # Lọc dữ liệu với D = d_val
        mask = (D == d_val)
        N_filtered = N[mask]
        Z_filtered = Z[mask]

        # Sắp xếp theo N để vẽ đường liền mạch
        sorted_indices = np.argsort(N_filtered)
        N_sorted = N_filtered[sorted_indices]
        Z_sorted = Z_filtered[sorted_indices]

        plt.plot(N_sorted, Z_sorted, marker='.', label=f'D = {d_val}')

    plt.xlabel('Number of Vectors (N)')
    plt.ylabel(zlabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    filename = r'C:\Users\ADMIN\Downloads\Projet\Equidistribution-on-hypersphere\graph\result.dat'

    D, N, theta_moyen, theta_goc, diff = read_data(filename)

    plot_2d_lines(D, N, diff, Ds_to_plot=[3,4,5], 
                  zlabel='Theta_theorical - Theta_moyen (°)', 
                  title='Difference between Dimension and Number of Vectors')
