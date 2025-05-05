🧪 Taller – Construyendo el Mundo 3D: Vértices, Aristas y Caras

📅 Fecha  
2025-04-15 – Fecha de entrega

🎯 Objetivo del Taller  
Visualizar la estructura interna de un modelo 3D resaltando vértices, aristas y caras, usando un archivo `.glb` cargado en una escena interactiva con React Three Fiber.

🧠 Conceptos Aprendidos  
- Mallas poligonales: vértices, aristas y caras  
- Visualización 3D en tiempo real con React Three Fiber  
- Carga de modelos GLB con `useGLTF`  
- Control de cámara interactiva (`OrbitControls`)  
- Superposición de geometría con `Edges` y `Points`

🔧 Herramientas y Entornos  
- React + Vite  
- @react-three/fiber  
- @react-three/drei  
- Three.js  
- Visual Studio Code  
- GIF grabado con OBS

📁 Estructura del Proyecto

threejs/
├── public/
│ ├── modelos/
│ │ └── kawashaki_ninja_h2.glb
│ └── resultados/
│ └── kawasaki_visualizacion.gif
├── src/
│ ├── components/
│ │ └── ModelViewer.jsx
│ ├── App.jsx
│ ├── main.jsx
│ └── index.css
├── index.html
└── README.md

markdown
Copiar
Editar

🧪 Implementación

🔹 Etapas realizadas  
1. Inicialización del proyecto con Vite + React.  
2. Instalación de @react-three/fiber y drei.  
3. Carga del modelo 3D `kawashaki_ninja_h2.glb`.  
4. Recorrido de todas las mallas (`child.isMesh`) para aplicar geometría.  
5. Visualización con:
   - **Aristas** en negro (`Edges`)  
   - **Vértices** en rojo (`Points`)  
   - **Material gris claro** sobre fondo blanco  

🔹 Código relevante

```jsx
<Points geometry={child.geometry}>
  <pointsMaterial color="red" size={0.15} sizeAttenuation={false} />
</Points>

<Edges geometry={child.geometry} color="black" scale={1.01} />