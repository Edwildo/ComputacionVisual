# 🧪 Taller - Importando el Mundo: Visualización y Conversión de Formatos 3D

Este taller tiene como objetivo comparar y convertir modelos 3D en distintos formatos — `.OBJ`, `.STL` y `.GLTF` — utilizando Python para análisis y conversión, y React Three Fiber para la visualización interactiva en la web.

---

## 📂 Estructura del proyecto

2025-04-03_taller_conversion_formatos_3d/
├── python/
│ └── conversion_visualizacion.ipynb
├── threejs/
│ ├── public/
│ │ ├── handtruck.obj
│ │ ├── teamugstl.stl
│ │ ├── scene.gltf
│ │ ├── scene.bin
│ ├── src/
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── components/ModelViewer.jsx
│ └── README.md

markdown
Copiar
Editar

---

## 🧠 Flujo del Taller

### 1. 📊 Análisis en Python
Se cargaron y analizaron los modelos 3D con `trimesh`. Se compararon los siguientes aspectos:

- Número de vértices y caras
- Presencia de normales
- Vértices duplicados

### 2. 🔁 Conversión de formatos
Los modelos se convirtieron y cargaron en múltiples formatos para su visualización. Se utilizó `trimesh` y `open3d` para facilitar las exportaciones.

### 3. 🌐 Visualización web
Con `React Three Fiber` y `@react-three/drei` se implementó un visor interactivo que:

- Permite alternar entre `.obj`, `.stl` y `.gltf`
- Usa `OrbitControls` para navegación 3D
- Renderiza modelos con luz ambiental y direccional

---

## 🖼️ Evidencia visual

### Visualización de modelos

| Formato | Vista interactiva |
|--------|-------------------|
| `.OBJ` | ![obj-demo](./assets/gif_obj.gif) |
| `.STL` | ![stl-demo](./assets/gif_stl.gif) |
| `.GLTF` | ![gltf-demo](./assets/gif_gltf.gif) |

> *(Incluir tus propios GIFs grabados con ScreenToGif, OBS o similar, colocados en `/threejs/src/assets/` o enlazados desde Imgur.)*

---

## 🧠 Comentarios personales

- Fue útil entender las diferencias internas entre los formatos 3D. Por ejemplo, `.STL` no contiene información de materiales, mientras que `.GLTF` sí.
- Trabajar con React Three Fiber facilitó mucho la integración visual, aunque los errores por rutas incorrectas (como cargar `index.html` en vez de modelos) fueron un reto importante al principio.
- Trimesh resultó muy flexible para inspeccionar y convertir modelos, aunque algunos `.gltf` con referencias externas necesitaron archivos `.bin` asociados correctamente.

---

## 🔗 Recursos utilizados

- [trimesh](https://trimsh.org/)
- [three.js](https://threejs.org/)
- [react-three-fiber](https://docs.pmnd.rs/react-three-fiber/)
- [GLTF to GLB converter](https://gltf.pmnd.rs/)

---

## ✅ Checklist de criterios cumplidos

- ✅ Conversión exitosa entre formatos `.obj`, `.stl`, `.gltf`
- ✅ Visualización funcional en React Three Fiber
- ✅ Comparación de geometría con Python (vértices, caras, normales)
- ✅ Código organizado y comentado
- ✅ Evidencias visuales (GIFs)
- ✅ Commits descriptivos en inglés