# 🧪 Taller - Ojos Digitales: Introducción a la Visión Artificial

## 🎯 Objetivo
Explorar cómo los computadores procesan imágenes aplicando transformaciones básicas de visión por computador con OpenCV, como la conversión a escala de grises, filtros y detección de bordes.

## 🐍 Entorno Python

### Herramientas utilizadas
- `opencv-python`
- `numpy`
- `matplotlib`

### 📂 Estructura del proyecto
```
2025-04-01_taller_ojos_digitales/
├── python/
│   ├── main_opencv.py
│   ├── r6r.jpeg
│   └── image.png
└── README.md
```

### 🚀 Ejecución del código
1. Instalar dependencias (si no están en el entorno virtual):
```bash
pip install opencv-python numpy matplotlib
```

2. Ejecutar el script desde la terminal:
```bash
python python/main_opencv.py
```

### 🧠 Flujo de procesamiento implementado
1. Carga una imagen a color (`r6r.jpeg`).
2. Convierte la imagen a escala de grises.
3. Aplica un filtro de desenfoque (`GaussianBlur`).
4. Aplica un filtro de enfoque (`Sharpen` con convolución).
5. Detecta bordes usando Sobel X, Sobel Y y Laplaciano.
6. Muestra los resultados en una visualización tipo collage y los guarda en `image.png`.

### 🖼️ Resultado visual
![Resultado de procesamiento](python/image.png)

### ✅ Resultado esperado en consola
```
✔️ OpenCV está instalado. Versión: 4.x.x
✔️ Imagen cargada correctamente.
✔️ Imagen procesada y guardada como image.png.
```

### 💬 Comentarios personales
- La detección de bordes fue clara y muestra cómo diferentes filtros destacan estructuras distintas.
- Fue importante cuidar el path del archivo para evitar errores con `\` en Windows.
- La visualización con `matplotlib` es más flexible para guardar el resultado como imagen.

---

### ✅ Criterios cumplidos
- [x] Conversión a escala de grises
- [x] Filtros de desenfoque y enfoque
- [x] Detección de bordes con Sobel y Laplaciano
- [x] Visualización de resultados
- [x] Código funcional y limpio
- [x] README con resultados y explicación clara