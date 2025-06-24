import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_icosahedron():
    phi = (1 + np.sqrt(5)) / 2  # tỉ lệ vàng

    # 12 đỉnh của Icosahedron (chuẩn hóa trên mặt cầu bán kính 1)
    vertices = np.array([
        [-1,  phi,  0],
        [ 1,  phi,  0],
        [-1, -phi,  0],
        [ 1, -phi,  0],
        [ 0, -1,  phi],
        [ 0,  1,  phi],
        [ 0, -1, -phi],
        [ 0,  1, -phi],
        [ phi,  0, -1],
        [ phi,  0,  1],
        [-phi,  0, -1],
        [-phi,  0,  1],
    ])

    # Chuẩn hóa các điểm về mặt cầu bán kính 1
    vertices /= np.linalg.norm(vertices, axis=1)[:, np.newaxis]

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ điểm
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], color='blue', s=80)

    # Vẽ các đường nối (cạnh Icosahedron)
    # Danh sách cạnh (từ Wikipedia Icosahedron)
    edges = [
        (0,1), (0,5), (0,7), (0,10), (0,11),
        (1,5), (1,7), (1,8), (1,9),
        (2,3), (2,4), (2,6), (2,10), (2,11),
        (3,4), (3,6), (3,8), (3,9),
        (4,5), (4,9), (4,11),
        (5,9), (5,11),
        (6,7), (6,8), (6,10),
        (7,8), (7,10),
        (8,9),
        (10,11)
    ]

    for edge in edges:
        i, j = edge
        ax.plot([vertices[i,0], vertices[j,0]],
                [vertices[i,1], vertices[j,1]],
                [vertices[i,2], vertices[j,2]], color='black')

    ax.set_box_aspect([1,1,1])
    ax.set_title("Icosahedron với 12 điểm đỉnh trên mặt cầu")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.grid(False)
    plt.show()

plot_icosahedron()
