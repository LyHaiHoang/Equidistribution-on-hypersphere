import numpy as np
from scipy.spatial import ConvexHull

# Tọa độ đỉnh của 5 khối Platonic (đơn vị)
# 1. Tetrahedron
tetrahedron = np.array([
    [1, 1, 1],
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]
])
tetrahedron = tetrahedron / np.linalg.norm(tetrahedron[0])  # chuẩn hóa

# 2. Cube (đơn vị cạnh 2, tâm tại gốc)
cube = np.array([[x, y, z] for x in [-1,1] for y in [-1,1] for z in [-1,1]])
cube = cube / np.linalg.norm(cube[0])  # chuẩn hóa

# 3. Octahedron (tám đỉnh, trên các trục tọa độ)
octahedron = np.array([
    [1,0,0], [-1,0,0],
    [0,1,0], [0,-1,0],
    [0,0,1], [0,0,-1]
])

# 4. Dodecahedron và 5. Icosahedron có thể dùng vertices từ scipy.spatial.ConvexHull
# Scipy không có sẵn vertices Platonic, ta dùng thư viện khác hoặc tạo thủ công
# Ở đây dùng module external "platonic_solids" để đơn giản (cài pip install platonic-solids)
try:
    from platonic_solids import PlatonicSolid
except ImportError:
    print("Please install platonic-solids: pip install platonic-solids")
    exit()

dodecahedron = np.array(PlatonicSolid('dodecahedron').vertices)
icosahedron = np.array(PlatonicSolid('icosahedron').vertices)

def angle_between_vectors(u, v):
    """Calculate angle in degrees between two vectors u and v"""
    u = u / np.linalg.norm(u)
    v = v / np.linalg.norm(v)
    dot = np.clip(np.dot(u, v), -1.0, 1.0)  # clip for numerical stability
    return np.degrees(np.arccos(dot))

def all_vertex_angles(vertices):
    """Calculate all pairwise central angles between vertices"""
    n = len(vertices)
    angles = []
    for i in range(n):
        for j in range(i+1, n):
            angle = angle_between_vectors(vertices[i], vertices[j])
            angles.append(angle)
    return angles

solids = {
    'Tetrahedron': tetrahedron,
    'Cube': cube,
    'Octahedron': octahedron,
    'Dodecahedron': dodecahedron,
    'Icosahedron': icosahedron
}

for name, verts in solids.items():
    angles = all_vertex_angles(verts)
    print(f"{name}:")
    print(f"  Number of vertices: {len(verts)}")
    print(f"  Min angle (deg): {min(angles):.2f}")
    print(f"  Max angle (deg): {max(angles):.2f}")
    print(f"  Sample angles (first 5): {[round(a,2) for a in angles[:5]]}\n")
