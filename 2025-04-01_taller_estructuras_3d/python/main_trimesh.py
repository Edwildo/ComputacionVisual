import trimesh

# Cargar la escena
scene = trimesh.load("modelos/kawashaki_ninja_h2.glb")

# Si es una escena con múltiples geometrías
if isinstance(scene, trimesh.Scene):
    # Aplicar las transformaciones y unir las geometrías en una sola
    meshes = []
    for name, geom in scene.geometry.items():
        transform = scene.graph.get(name)[0]  # obtener transformación
        transformed = geom.copy().apply_transform(transform)
        meshes.append(transformed)

    # Unir todas las mallas transformadas
    mesh = trimesh.util.concatenate(meshes)
else:
    mesh = scene

# Mostrar la información estructural
print("📊 Información del modelo:")
print(f"✔️ Vértices: {len(mesh.vertices)}")
print(f"✔️ Aristas:  {len(mesh.edges)}")
print(f"✔️ Caras:    {len(mesh.faces)}")

# Mostrar la visualización
mesh.show()
