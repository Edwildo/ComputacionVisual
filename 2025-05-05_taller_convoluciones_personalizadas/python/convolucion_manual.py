import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# Función de convolución 2D
# ---------------------------
def apply_convolution(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    pad_h, pad_w = kh // 2, kw // 2
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    result = np.zeros_like(image, dtype=np.float32)

    for i in range(h):
        for j in range(w):
            region = padded[i:i+kh, j:j+kw]
            result[i, j] = np.sum(region * kernel)

    return np.clip(result, 0, 255).astype(np.uint8)

# ---------------------------
# Kernels personalizados
# ---------------------------
sharpen = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
blur = np.ones((3, 3), dtype=np.float32) / 9
edge = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# ---------------------------
# Leer imagen original
# ---------------------------
img = cv2.imread('imagenes/image.png', cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("❌ No se pudo cargar la imagen. Asegúrate de que la ruta 'imagenes/image.png' sea correcta.")

# ---------------------------
# Aplicar convolución manual
# ---------------------------
out_sharp = apply_convolution(img, sharpen)
out_blur = apply_convolution(img, blur)
out_edge = apply_convolution(img, edge)

# ---------------------------
# Comparación con OpenCV
# ---------------------------
cv_sharp = cv2.filter2D(img, -1, sharpen)
cv_blur = cv2.filter2D(img, -1, blur)
cv_edge = cv2.filter2D(img, -1, edge)

# ---------------------------
# Mostrar comparaciones
# ---------------------------
titles = [
    "Original", "Manual Sharpen", "OpenCV Sharpen",
    "Manual Blur", "OpenCV Blur",
    "Manual Edge", "OpenCV Edge"
]
images = [img, out_sharp, cv_sharp, out_blur, cv_blur, out_edge, cv_edge]

plt.figure(figsize=(14, 8))
for i in range(7):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.savefig("comparacion_filtros.png")  # Para incluir en el README
plt.show()
