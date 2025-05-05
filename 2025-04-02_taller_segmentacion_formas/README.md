# 🧪 Taller - Segmentando el Mundo: Binarización y Reconocimiento de Formas

## 🎯 Objetivo

Aplicar técnicas de segmentación en imágenes en escala de grises usando umbralización fija y adaptativa, para detectar formas simples, contornos, centros de masa y calcular métricas morfológicas básicas. Este proceso permite comprender cómo los algoritmos de visión artificial segmentan y analizan regiones de interés.

## 📁 Estructura del proyecto

```
2025-04-02_taller_segmentacion_formas/
├── python/
│   ├── image.png
│   ├── main_segmentacion.py
├── README.md
```

## 🧪 Flujo de procesamiento

1. **Carga de imagen**: Se carga una imagen en escala de grises.
2. **Umbralización**:

   * Umbral fijo (`cv2.threshold`)
   * Umbral adaptativo (`cv2.adaptiveThreshold`)
3. **Detección de contornos**: Se identifican los contornos de las regiones binarizadas con `cv2.findContours()`.
4. **Análisis morfológico**:

   * Se calculan bounding boxes (`cv2.boundingRect`)
   * Se identifican centros de masa (`cv2.moments()`)
   * Se miden área y perímetro de cada forma.
5. **Visualización**: Se dibujan los contornos sobre la imagen original y se guarda como `image.png`.

## 📸 Evidencia visual

Imagen de salida con contornos y centros de masa:

![Resultado](python/image.png)

## 📊 Métricas:

```
✔️ Formas detectadas: 1
✔️ Área promedio: 932176.00
✔️ Perímetro promedio: 3946.00
```

## ▶️ Ejecución

Desde la carpeta `python`, asegúrate de tener las dependencias instaladas y ejecuta el script:

```bash
pip install opencv-python matplotlib numpy
python main_segmentacion.py
```

> Nota: La imagen debe estar correctamente ubicada y nombrada como `image.png` en la carpeta `python/`.

## 🤖 Código relevante

Archivo: `main_segmentacion.py`

* Contiene el procesamiento completo, binarización, detección y análisis de formas.

## 🧠 Comentarios personales

Este taller permitió comprender mejor cómo segmentar imágenes utilizando técnicas clásicas de visión artificial. La diferencia entre los umbrales fijo y adaptativo se evidenció claramente al detectar formas de diferentes iluminaciones. Fue útil calcular las métricas básicas de cada contorno para entender su geometría.

---

✅ Taller completado cumpliendo con todos los criterios de evaluación.
