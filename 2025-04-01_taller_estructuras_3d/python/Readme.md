🧪 Taller – Construyendo el Mundo 3D: Vértices, Aristas y Caras

📅 Fecha  
2025-04-15 – Fecha de entrega

🎯 Objetivo del Taller  
Explorar las estructuras internas de un modelo 3D en Python, identificando vértices, aristas y caras a partir de un archivo en formato `.glb`, visualizando su geometría y extrayendo su información estructural.

🧠 Conceptos Aprendidos  
- Estructura de mallas poligonales (mesh)  
- Uso del módulo `trimesh` para cargar y analizar modelos 3D  
- Diferencias entre escenas (`Scene`) y mallas (`Trimesh`)  
- Aplicación de transformaciones geométricas  
- Visualización interactiva en 3D con Python  

🔧 Herramientas y Entornos  
- Python 3.12  
- [trimesh](https://trimsh.org)  
- pyglet < 2.0  
- Visual Studio Code  
- Grabación con OBS para GIF

📁 Estructura del Proyecto

python/
├── modelos/
│ └── kawashaki_ninja_h2.glb
├── resultados/
│ └── kawasaki_estructura.gif
├── main_trimesh.py
├── README.md

arduino
Copiar
Editar

🧪 Implementación

🔹 Etapas realizadas  
1. Instalación de dependencias:
   ```bash
   pip install trimesh "pyglet<2"
Carga del modelo .glb usando trimesh.load().

Identificación del tipo Scene, y recorrido de sus geometrías aplicando transformaciones.

Unión de todas las submallas en una sola con concatenate.

Cálculo de número de vértices, aristas y caras.

Visualización interactiva del modelo renderizado.

🔹 Código relevante

python
Copiar
Editar
for name, geom in scene.geometry.items():
    transform = scene.graph.get(name)[0]
    transformed = geom.copy().apply_transform(transform)
    meshes.append(transformed)

mesh = trimesh.util.concatenate(meshes)
📊 Resultados Visuales

GIF mostrando la estructura renderizada del modelo en trimesh:


🧩 Prompts Usados
No se usaron prompts de IA en esta implementación.

💬 Reflexión Final
Este entorno me permitió acceder directamente a las propiedades estructurales del modelo, como el número de vértices, caras y aristas. Aprendí cómo trimesh interpreta una escena con múltiples mallas, y la importancia de aplicar correctamente las transformaciones de cada parte para una visualización coherente. La principal dificultad fue comprender cómo acceder a los datos reales desde una Scene, pero una vez resuelto, se logró una visualización correcta y detallada.

👥 Contribuciones Grupales (si aplica)

Carga y análisis del modelo .glb

Implementación del recorrido y transformación de geometrías

Visualización con trimesh.show()

Grabación del GIF y documentación

✅ Checklist de Entrega

 Visualización funcional del modelo

 Información estructural (vértices, aristas, caras)

 GIF incluido con evidencia clara

 Código comentado y funcional

 README completo y ordenado

 Commits descriptivos en inglés