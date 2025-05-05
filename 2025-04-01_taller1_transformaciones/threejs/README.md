🧪 Taller 1 – Transformaciones Básicas en Computación Visual

📅 Fecha  
2025-04-15 – Fecha de entrega

🎯 Objetivo del Taller  
Explorar transformaciones geométricas animadas (traslación, rotación y escalado) aplicadas a un objeto 3D en un entorno web interactivo utilizando React Three Fiber y Three.js, ejecutado localmente en VSCode con Vite.

🧠 Conceptos Aprendidos  

- Transformaciones geométricas (escala, rotación, traslación)  
- Movimiento circular y escalado cíclico con funciones trigonométricas  
- Animación cuadro a cuadro con `useFrame()`  
- Navegación 3D interactiva con `OrbitControls`  
- Integración de `Canvas` 3D en proyectos React

🔧 Herramientas y Entornos  

- Visual Studio Code  
- Vite + React  
- Three.js  
- @react-three/fiber  
- @react-three/drei  
- Herramienta externa de grabación para el GIF (OBS / ScreenToGif / Peek)

📁 Estructura del Proyecto

2025-04-15_taller1_transformaciones/  
├── threejs/  
│   ├── src/  
│   │   ├── App.jsx  
│   │   ├── main.jsx  
│   │   ├── index.css  
│   │   └── components/TransformingCube.jsx  
│   ├── public/  
│   │   └── resultados/  
│   │       └── cubo_transformaciones_r3f.gif  
│   ├── index.html  
│   ├── package.json  
│   └── README.md  

📎 Sigue la estructura de entregas descrita en la guía GitLab  

🧪 Implementación

🔹 Etapas realizadas  

1. Inicialización de proyecto con Vite + React en VSCode.  
2. Instalación de dependencias de React Three Fiber y Drei.  
3. Creación del componente `TransformingCube` con transformaciones animadas:  
   - Traslación circular con `Math.cos` y `Math.sin`.  
   - Rotación constante sobre los ejes X e Y.  
   - Escalado cíclico dependiente del tiempo.  
4. Visualización en un `Canvas` 3D y navegación con `OrbitControls`.  
5. Captura del resultado en formato GIF.

🔹 Código relevante

```jsx
useFrame(({ clock }) => {
  const t = clock.getElapsedTime();
  ref.current.position.x = 2 * Math.cos(t);
  ref.current.position.y = 2 * Math.sin(t);
  ref.current.rotation.x += 0.01;
  ref.current.rotation.y += 0.01;
  const scale = 1 + 0.3 * Math.sin(t);
  ref.current.scale.set(scale, scale, scale);
});
