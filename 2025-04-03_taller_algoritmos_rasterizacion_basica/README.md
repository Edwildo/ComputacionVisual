🧪 Taller - Rasterización desde Cero: Dibujando con Algoritmos Clásicos
🎯 Objetivo
Implementar los algoritmos fundamentales de rasterización (línea de Bresenham, círculo por punto medio y relleno de triángulo por scanline), comprendiendo el proceso de construcción de primitivas gráficas píxel a píxel sin usar librerías gráficas de alto nivel.

🧠 Algoritmos implementados
1. 🟥 Línea - Algoritmo de Bresenham
Dibuja líneas con enteros, sin usar floats.

Eficiente y muy utilizado en hardware gráfico.

Resultado: linea.png

2. 🔵 Círculo - Algoritmo de Punto Medio
Calcula puntos simétricos sobre octantes.

Basado en decisiones incrementales.

Resultado: circulo.png

3. 🔺 Triángulo - Relleno con Scanline
Ordena los vértices y realiza interpolación horizontal por franjas (y).

Rellena el triángulo píxel a píxel.

Resultado: triangulo.png

🖼️ Resultados visuales
Figura	Imagen
Línea (Bresenham)	
Círculo (Punto Medio)	
Triángulo (Scanline Fill)	

🧾 Código relevante
Ubicado en python/rasterizacion_algoritmos.ipynb.

Incluye:

Funciones bresenham, midpoint_circle, fill_triangle.

Visualización con matplotlib.

Guardado con Pillow.

💬 Reflexión final
Precisión: Bresenham y punto medio son exactos y eficientes para enteros.

Velocidad: Todos los métodos funcionan sin operaciones costosas (como trigonometría o floats).

Aplicación real: Son la base de renderizado en sistemas embebidos, videojuegos retro y dispositivos gráficos de bajo nivel.

✅ Checklist de entrega
 Algoritmo de línea funcional.

 Algoritmo de círculo funcional.

 Relleno de triángulo implementado.

 Resultados exportados como .png.

 README con explicaciones y visualización.

 Código comentado y limpio.