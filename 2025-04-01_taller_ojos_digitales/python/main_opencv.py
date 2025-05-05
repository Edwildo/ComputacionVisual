import cv2
print("✔️ OpenCV está instalado. Versión:", cv2.__version__)
import numpy as np
import matplotlib.pyplot as plt

# Ruta de la imagen
image_path = r"2025-04-01_taller_ojos_digitales\python\r6r.jpeg"

# 1. Cargar imagen a color
image_color = cv2.imread(image_path)
if image_color is None:
    raise FileNotFoundError("⚠️ La imagen no se encontró en la ruta especificada.")

# 2. Convertir a escala de grises
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

# 3. Filtro de desenfoque (blur)
blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)

# 4. Filtro de enfoque (sharpen)
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
sharpened = cv2.filter2D(image_gray, -1, kernel_sharpen)

# 5. Detección de bordes
sobelx = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(image_gray, cv2.CV_64F)

# 6. Mostrar resultados con matplotlib
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.title("Original (color)")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(image_gray, cmap="gray")
plt.title("Escala de grises")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(blurred, cmap="gray")
plt.title("Blur (Gaussiano)")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(sharpened, cmap="gray")
plt.title("Sharpen")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(sobelx + sobely, cmap="gray")
plt.title("Sobel (X + Y)")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(laplacian, cmap="gray")
plt.title("Laplaciano")
plt.axis("off")

plt.tight_layout()
plt.show()
