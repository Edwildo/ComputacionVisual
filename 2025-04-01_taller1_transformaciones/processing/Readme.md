🧪 Taller 1 – Transformaciones Básicas en Computación Visual

📅 Fecha  
2025-04-15 – Fecha de entrega

🎯 Objetivo del Taller  
Aplicar transformaciones geométricas (traslación, rotación y escala) a un cubo 3D animado en Processing, usando funciones dependientes del tiempo como `sin()` y `frameCount`.

🧠 Conceptos Aprendidos  

- Transformaciones 3D en Processing  
- Movimiento senoidal (onda)  
- Rotaciones con `rotateX()` y `rotateY()`  
- Escala con `scale()`  
- Uso de `frameCount` para animación  

🔧 Herramientas y Entornos  

- Processing 4  
- Modo `P3D`  
- Exportación de frames con `saveFrame()` (opcional)  

📁 Estructura del Proyecto

2025-04-15_taller1_transformaciones/  
├── processing/  
│   ├── sketch_transformaciones/  
│   │   └── sketch_transformaciones.pde  
│   ├── resultados/  
│   │   └── cubo_transformaciones_processing.gif  
│   └── README.md  

📎 Sigue la estructura de entregas descrita en la guía GitLab  

🧪 Implementación

🔹 Etapas realizadas  

1. Inicialización de ventana en 3D (`size(..., P3D)`)  
2. Traslación ondulante del cubo con `sin()` y `cos()`  
3. Rotación animada con `rotateX()` y `rotateY()`  
4. Escalado cíclico con `scale()`  
5. Exportación opcional de frames con `saveFrame()`  

🔹 Código relevante

```java
translate(width/2, height/2);
translate(100 * sin(frameCount * 0.05), 100 * cos(frameCount * 0.05));
rotateX(angle);
rotateY(angle * 0.5);
scale(1 + 0.5 * sin(frameCount * 0.05));
box(100);
