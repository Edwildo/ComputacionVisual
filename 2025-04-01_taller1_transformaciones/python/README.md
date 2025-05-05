🧪 Taller 1 – Transformaciones Básicas en Computación Visual

📅 Fecha  
2025-04-15 – Fecha de entrega

🎯 Objetivo del Taller  
Aplicar transformaciones geométricas (traslación, rotación y escala) sobre una figura 2D mediante el uso de matrices homogéneas en Python. Se busca visualizar estas transformaciones en forma de animación y generar un GIF representativo.

🧠 Conceptos Aprendidos  

- Transformaciones geométricas (escala, rotación, traslación)  
- Matrices homogéneas en 2D  
- Visualización de formas con Matplotlib  
- Generación de animaciones por frames  
- Exportación de GIFs con ImageIO  

🔧 Herramientas y Entornos  

- Python 3  
- VSCode con extensión Jupyter  
- `numpy`, `matplotlib`, `imageio`  

📁 Estructura del Proyecto

2025-04-15_taller1_transformaciones/  
├── python/  
│   ├── transformaciones.ipynb  
│   ├── resultados/  
│   │   └── transformaciones_cuadrado.gif  
│   └── README.md  

📎 Sigue la estructura de entregas descrita en la guía GitLab  

🧪 Implementación

🔹 Etapas realizadas  

1. Definición de una figura geométrica base (cuadrado en 2D).  
2. Construcción de matrices homogéneas para traslación, rotación y escala.  
3. Animación cuadro a cuadro de las transformaciones en función del tiempo (`frame`).  
4. Visualización de cada frame con `matplotlib`.  
5. Exportación del resultado como un archivo GIF usando `imageio`.  

🔹 Código relevante

```python
theta = t * np.pi / 30
tx, ty = np.sin(t * 0.1), np.cos(t * 0.1)
s = 1 + 0.5 * np.sin(t * 0.1)

T = get_translation_matrix(tx, ty)
R = get_rotation_matrix(theta)
S = get_scale_matrix(s, s)
combined = T @ R @ S
transformed = apply_transform(square, combined)
