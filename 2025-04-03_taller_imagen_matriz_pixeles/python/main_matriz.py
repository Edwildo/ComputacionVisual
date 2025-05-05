import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar imagen
image = cv2.imread("r6r.jpeg")
if image is None:
    raise FileNotFoundError("❌ Imagen no encontrada. Asegúrate de que 'r6r.jpeg' esté en la carpeta 'python/'.")

# Obtener dimensiones de la imagen
height, width, _ = image.shape

# 2. Separar canales RGB y convertir a HSV
b, g, r = cv2.split(image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. Modificar región con slicing (solo si cabe en la imagen)
modified_image = image.copy()

# Coordenadas de las regiones
src_y1, src_y2 = 0, 100
src_x1, src_x2 = 0, 100
dst_y1, dst_y2 = 50, 150
dst_x1, dst_x2 = 100, 200
dst_x3, dst_x4 = 200, 300

# Verificar límites para evitar errores
if dst_y2 <= height and dst_x2 <= width:
    modified_image[dst_y1:dst_y2, dst_x1:dst_x2] = [0, 0, 255]  # rojo

if dst_y2 <= height and dst_x4 <= width and src_y2 <= height and src_x2 <= width:
    modified_image[dst_y1:dst_y2, dst_x3:dst_x4] = image[src_y1:src_y2, src_x1:src_x2]

# 4. Calcular histogramas de canales BGR
colors = ("b", "g", "r")
plt.figure()
for i, col in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
plt.title("Histograma de canales RGB")
plt.xlabel("Intensidad")
plt.ylabel("Frecuencia")
plt.savefig("histograma.png")

# 5. Ajuste de brillo y contraste
alpha = 1.5  # contraste
beta = 50    # brillo
brillo_contraste = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# 6. Guardar imagen modificada
cv2.imwrite("image_modificada.png", modified_image)

# 7. Mostrar resultados
cv2.imshow("Imagen Original", image)
cv2.imshow("Imagen Modificada", modified_image)
cv2.imshow("Brillo y Contraste", brillo_contraste)
cv2.waitKey(0)
cv2.destroyAllWindows()
