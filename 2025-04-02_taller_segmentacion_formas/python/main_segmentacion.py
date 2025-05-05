import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ruta a la imagen en escala de grises
image_path = "r6r.jpeg"
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image_gray is None:
    raise FileNotFoundError("❌ Imagen no encontrada. Verifica la ruta.")

# 1. Umbralización fija
_, binary_fixed = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# 2. Umbralización adaptativa
binary_adaptive = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 11, 2
)

# 3. Detección de contornos
contours, _ = cv2.findContours(binary_adaptive, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. Dibujar contornos y análisis
image_result = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
total_area = 0
total_perimeter = 0

for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    total_area += area
    total_perimeter += perimeter

    # Dibujar contorno
    cv2.drawContours(image_result, [contour], -1, (0, 255, 0), 1)

    # Bounding box
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image_result, (x, y), (x+w, y+h), (255, 0, 0), 1)

    # Centro de masa
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        cv2.circle(image_result, (cx, cy), 2, (0, 0, 255), -1)

# 5. Métricas
num_formas = len(contours)
avg_area = total_area / num_formas if num_formas > 0 else 0
avg_perimeter = total_perimeter / num_formas if num_formas > 0 else 0

print("📊 Métricas:")
print(f"✔️ Formas detectadas: {num_formas}")
print(f"✔️ Área promedio: {avg_area:.2f}")
print(f"✔️ Perímetro promedio: {avg_perimeter:.2f}")

# 6. Visualización
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(image_gray, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Umbral Adaptativo")
plt.imshow(binary_adaptive, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Segmentación Final")
plt.imshow(cv2.cvtColor(image_result, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.savefig("resultado_segmentacion.png")  # Para README
plt.show()
