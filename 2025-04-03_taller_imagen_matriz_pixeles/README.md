🧪 Taller - De Píxeles a Coordenadas: Explorando la Imagen como Matriz
🔍 Objetivo del taller
El objetivo de este taller fue comprender cómo una imagen digital puede ser interpretada como una matriz y cómo modificar sus píxeles directamente. Para ello, se realizaron manipulaciones sobre los canales de color, se modificaron regiones específicas, se calcularon histogramas y se aplicaron ajustes de brillo y contraste.

📁 Estructura del proyecto
yaml
Copiar
Editar
2025-04-03_taller_imagen_matriz_pixeles/
├── python/
│   ├── main_matriz.py
│   ├── r6r.jpeg
│   ├── image_modificada.png
│   ├── histograma.png
├── README.md
⚙️ Flujo de procesamiento implementado
Carga de imagen en color: Se utilizó cv2.imread() para cargar la imagen r6r.jpeg.

Separación de canales: Se dividió la imagen en sus componentes B, G y R usando cv2.split() y se convirtió también a HSV.

Modificación por regiones:

Se coloreó una región rectangular con rojo puro ([0, 0, 255] en BGR).

Se reemplazó otra región con una copia de un fragmento de la imagen original (solo si el tamaño lo permitía).

Histograma: Se calculó el histograma por canal (B, G, R) y se guardó como histograma.png.

Ajuste de brillo y contraste: Se aumentó el brillo y contraste usando cv2.convertScaleAbs().

Visualización: Se mostraron en ventana las 3 versiones: original, modificada, y con brillo/contraste.

🖼️ Resultados visuales
Imagen Original	Imagen Modificada	Ajuste Brillo/Contraste
(Se muestra por ventana OpenCV)

📝 Las ventanas también fueron visualizadas correctamente usando cv2.imshow().

📊 Histograma de Canales RGB

El histograma muestra la distribución de intensidades para cada canal de color.

Se observa mayor presencia de valores altos en el canal rojo, coherente con la imagen de una motocicleta naranja/roja.

💡 Comentarios y aprendizaje
El ejercicio permitió visualizar cómo una imagen es realmente una estructura de datos (matriz) y puede ser manipulada como tal.

Se trabajó con slicing, reemplazo de regiones, y operaciones básicas de mejora visual.

Aprendí a validar tamaños antes de copiar regiones de una imagen sobre otra para evitar errores de broadcasting.

✅ Requisitos cumplidos
 Manipulación de regiones con slicing.

 Separación de canales y conversión a HSV.

 Cálculo y visualización de histogramas.

 Ajuste manual de brillo y contraste.

 Código limpio y funcional.

 README completo con imágenes generadas.