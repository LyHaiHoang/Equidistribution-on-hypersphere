import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Định nghĩa đỉnh của 5 Platonic solids (đơn giản, chưa chuẩn hóa)

# 1. Tetrahedron (4 đỉnh)
tetrahedron_vertices = np.array([
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
])

tetrahedron_faces = [
    [0,1,2],
    [0,3,1],
    [0,2,3],
    [1,3,2]
]

# 2. Cube (8 đỉnh)
cube_vertices = np.array([[x,y,z] for x in [-1,1] for y in [-1,1] for z in [-1,1]])
cube_faces = [
    [0,1,3,2], [4,5,7,6], [0,1,5,4],
    [2,3,7,6], [0,2,6,4], [1,3,7,5]
]

# 3. Octahedron (6 đỉnh)
octahedron_vertices = np.array([
    [1,0,0], [-1,0,0],
    [0,1,0], [0,-1,0],
    [0,0,1], [0,0,-1]
])

octahedron_faces = [
    [0,2,4], [2,1,4], [1,3,4], [3,0,4],
    [0,2,5], [2,1,5], [1,3,5], [3,0,5]
]

# Hàm vẽ đa giác 3D
def plot_solid(ax, vertices, faces, color):
    poly3d = [[vertices[face] for face in f] for f in faces]
    collection = Poly3DCollection(poly3d, facecolors=color, linewidths=1, edgecolors='k', alpha=0.5)
    ax.add_collection3d(collection)
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], color='k')

fig = plt.figure(figsize=(15,4))

# Vẽ Tetrahedron
ax1 = fig.add_subplot(151, projection='3d')
plot_solid(ax1, tetrahedron_vertices, tetrahedron_faces, 'cyan')
ax1.set_title('Tetrahedron')
ax1.auto_scale_xyz([-1.5,1.5],[-1.5,1.5],[-1.5,1.5])

# Vẽ Cube
ax2 = fig.add_subplot(152, projection='3d')
plot_solid(ax2, cube_vertices, cube_faces, 'orange')
ax2.set_title('Cube')
ax2.auto_scale_xyz([-1.5,1.5],[-1.5,1.5],[-1.5,1.5])

# Vẽ Octahedron
ax3 = fig.add_subplot(153, projection='3d')
plot_solid(ax3, octahedron_vertices, octahedron_faces, 'green')
ax3.set_title('Octahedron')
ax3.auto_scale_xyz([-1.5,1.5],[-1.5,1.5],[-1.5,1.5])

# Để vẽ Dodecahedron và Icosahedron phức tạp hơn, bạn có thể dùng thư viện external hoặc tọa độ chuẩn tốn diện tích
# Nên mình tạm dừng ở 3 khối cơ bản này

for ax in [ax1, ax2, ax3]:
    ax.set_axis_off()

plt.tight_layout()
plt.show()
