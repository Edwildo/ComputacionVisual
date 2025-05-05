🧪 Taller – Jerarquías y Transformaciones: El Árbol del Movimiento

📅 Fecha  
2025-04-15 – Fecha de entrega

🎯 Objetivo del Taller  
Simular una estructura jerárquica padre → hijo → nieto y observar cómo las transformaciones aplicadas al objeto padre afectan visualmente a sus hijos. Se controlan las transformaciones en tiempo real mediante una interfaz interactiva.

🧠 Conceptos Aprendidos  
- Jerarquía padre-hijo-nieto en gráficos 3D  
- Agrupación de nodos con `<group>`  
- Propagación de transformaciones en jerarquía  
- Control visual en tiempo real con `leva`  
- Uso de `OrbitControls` y `Canvas` en React Three Fiber  

🔧 Herramientas y Entornos  
- React + Vite  
- React Three Fiber  
- @react-three/drei  
- Leva (sliders interactivos)  
- Visual Studio Code  
- GIF grabado con OBS Studio  

📁 Estructura del Proyecto

threejs/
├── public/
├── src/
│ ├── components/
│ │ └── SceneHierarchy.jsx
│ ├── App.jsx
│ ├── main.jsx
│ └── index.css
├── index.html
└── resultados/
└── jerarquia_padre_hijo.gif

markdown
Copiar
Editar

🧪 Implementación

🔹 Etapas realizadas  
1. Creación de proyecto Vite con plantilla React.  
2. Instalación de dependencias necesarias (`three`, `@react-three/fiber`, `leva`).  
3. Implementación de jerarquía con `<group>` conteniendo un `<mesh>` cubo (padre) y un `<mesh>` esfera (nieto).  
4. Uso de `useFrame` para aplicar transformaciones del padre (rotación y posición).  
5. Sliders en tiempo real con `leva`.  
6. Estilo global (`index.css`) para lograr visualización a pantalla completa.  

🔹 Código relevante

```jsx
const groupRef = useRef()

const { rotationY, positionX } = useControls({
  rotationY: { value: 0, min: -Math.PI, max: Math.PI },
  positionX: { value: 0, min: -5, max: 5 }
})

useFrame(() => {
  if (groupRef.current) {
    groupRef.current.rotation.y = rotationY
    groupRef.current.position.x = positionX
  }
})
📊 Resultados Visuales

🎥 GIF mostrando jerarquía y transformación con sliders:


🧩 Prompts Usados
No se usaron prompts de IA para esta implementación.

💬 Reflexión Final
Este taller me permitió comprender cómo una transformación aplicada a un objeto afecta directamente a todos sus hijos en una jerarquía. Fue útil ver cómo una simple rotación o traslación se propaga automáticamente, y cómo los sliders permiten controlarlo intuitivamente. Al principio, fue un reto lograr que los objetos ocuparan toda la pantalla, pero con ajustes en los estilos globales (index.css) se resolvió con éxito.

👥 Contribuciones Grupales (si aplica)

Implementación completa de jerarquía 3D en React

Configuración del entorno con Vite + Fiber + Leva

Generación de visualización final y documentación

✅ Checklist de Entrega

 Jerarquía funcional implementada

 Transformaciones aplicadas y observables

 Sliders en tiempo real con leva

 GIF incluido y funcional

 Código limpio y ordenado

 README completo y claro

 Commits en inglés descriptivo