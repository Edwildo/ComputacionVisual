import cv2
import numpy as np

# Cargar imagen binarizada
image = cv2.imread("circulo.png")
if image is None:
    raise FileNotFoundError("❌ Imagen no encontrada. Asegúrate de que 'circulo.png' esté en la carpeta 'python/'.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Detectar contornos
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image_result = image.copy()

# Analizar cada contorno
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    # Dibujar contorno y texto
    cv2.drawContours(image_result, [contour], -1, (0, 255, 0), 2)
    cv2.circle(image_result, (cx, cy), 5, (0, 0, 255), -1)
    cv2.putText(image_result, f"A:{int(area)} P:{int(perimeter)}", (cx - 50, cy - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
    cv2.putText(image_result, f"({cx},{cy})", (cx - 30, cy + 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1)

# Guardar imagen final
cv2.imwrite("resultados/figuras_geometricas_analisis.png", image_result)
