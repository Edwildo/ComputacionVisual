# 🧪 Taller - Análisis de Figuras Geométricas: Centroide, Área y Perímetro

## 🎯 Objetivo
Detectar formas simples (como círculos) en imágenes binarizadas y calcular propiedades geométricas como área, perímetro y centroide usando Python y OpenCV.

---

## 📂 Estructura del proyecto

2025-04-04_taller_analisis_figuras_geometricas/
├── python/
│ ├── main_figuras.py
│ └── circulo.png
├── resultados/
│ └── resultado_circulo.png
└── README.md

yaml
Copiar
Editar

---

## 🛠️ Proceso implementado

1. **Carga de imagen binarizada**:
   - Se utiliza una imagen de entrada en blanco y negro (`circulo.png`).

2. **Conversión a escala de grises y umbralización**:
   - Se aplica `cv2.threshold()` para generar una imagen binaria.

3. **Detección de contornos**:
   - Se usa `cv2.findContours()` para identificar figuras geométricas.

4. **Cálculo de métricas**:
   - **Área** mediante `cv2.contourArea()`
   - **Perímetro** con `cv2.arcLength()`
   - **Centroide** a partir de `cv2.moments()`

5. **Dibujo de resultados**:
   - Se dibujan los contornos y se etiquetan con sus métricas (área, perímetro y centroide).

---

## 🖼️ Resultados

La imagen generada muestra:

- Contorno detectado en rojo.
- Centroide marcado con un círculo.
- Texto con las métricas calculadas.

📌 **Ejemplo visual:**  
`resultados/resultado_circulo.png`

---

## 💬 Comentarios personales

Este ejercicio permitió comprender cómo se pueden extraer características geométricas básicas a partir de contornos detectados en imágenes binarizadas. Fue especialmente útil aplicar `cv2.moments()` para calcular el centroide de forma precisa.

---

## ✅ Estado

- [x] Detección de contornos
- [x] Cálculo de área y perímetro
- [x] Visualización del centroide
- [x] Anotación sobre la imagen