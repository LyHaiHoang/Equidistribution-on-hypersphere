import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_tetrahedron_with_center():
    # Các đỉnh của tứ diện đều
    v0 = np.array([ 1,  1,  1])
    v1 = np.array([-1, -1,  1])
    v2 = np.array([-1,  1, -1])
    v3 = np.array([ 1, -1, -1])
    
    vertices = [v0, v1, v2, v3]

    # Tính tọa độ tâm của tứ diện (trung bình 4 đỉnh)
    center = sum(vertices) / 4

    # Các mặt tam giác
    faces = [
        [v0, v1, v2],
        [v0, v1, v3],
        [v0, v2, v3],
        [v1, v2, v3]
    ]

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ các mặt
    poly = Poly3DCollection(faces, alpha=0.3, edgecolor='k')
    poly.set_facecolor('lightblue')
    ax.add_collection3d(poly)

    # Vẽ các đỉnh
    for i, v in enumerate(vertices):
        ax.scatter(*v, color='blue', s=100)
        ax.text(*v, f'V{i}', fontsize=12, color='black')

    # Vẽ các cạnh (đường nối các đỉnh)
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            xi, yi, zi = vertices[i]
            xj, yj, zj = vertices[j]
            ax.plot([xi, xj], [yi, yj], [zi, zj], color='black', linewidth=1)

    # Vẽ tâm tứ diện
    ax.scatter(*center, color='red', s=100)
    ax.text(*center, 'Center', fontsize=12, color='red')

    # Vẽ các đường nối từ tâm đến các đỉnh
    for v in vertices:
        ax.plot([center[0], v[0]], [center[1], v[1]], [center[2], v[2]],
                color='red', linestyle='dashed', linewidth=1)

    # Cài đặt trục và nhãn
    ax.set_box_aspect([1, 1, 1])
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Tứ diện với tâm và các đường nối từ tâm')

    plt.tight_layout()
    plt.show()

plot_tetrahedron_with_center()
