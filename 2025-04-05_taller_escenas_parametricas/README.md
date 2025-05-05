# 🧪 Taller - Escenas Paramétricas (Unity)

## 🎮 Entorno: Unity (LTS)
Este proyecto implementa una generación de objetos 3D (cubos, esferas, cilindros) en tiempo de ejecución a partir de datos estructurados. Utiliza programación con C# y estructuras personalizadas para parametrizar forma, posición, escala y color.

---

## 🧱 Estructura del Proyecto

Assets/
├── Scenes/
│ └── MainScene.unity
├── Scripts/
│ └── ParametricGenerator.cs

yaml
Copiar
Editar

---

## ⚙️ Lógica del Script

El archivo `ParametricGenerator.cs` contiene:

- Una clase serializable `ParametricObject` con propiedades:
  - `Vector3 position`
  - `Vector3 scale`
  - `Color color`
  - `string type` ("cube", "sphere", "cylinder")

- En el método `Start()`:
  - Se recorren los objetos definidos en el Inspector.
  - Se crea cada GameObject usando `GameObject.CreatePrimitive(...)`.
  - Se aplican sus parámetros dinámicamente.

---

## ▶️ Instrucciones para ejecutar

1. Abre `MainScene.unity`.
2. Crea un GameObject vacío llamado `Generator`.
3. Asigna el script `ParametricGenerator.cs`.
4. Desde el Inspector, agrega elementos al array `objects`:
   - Define posición, escala, color y tipo.

---

## 🎯 Ejemplo de uso

| Tipo    | Posición       | Escala         | Color     |
|---------|----------------|----------------|-----------|
| Cube    | (0, 0, 0)       | (1, 1, 1)       | Azul      |
| Sphere  | (2, 0, 0)       | (0.5, 0.5, 0.5) | Rojo      |
| Cylinder| (4, 0, 0)       | (1, 2, 1)       | Verde     |

---

## 💡 Comentarios y mejoras

- El sistema permite generar múltiples formas de manera dinámica sin prefabs.
- Es posible extender este enfoque leyendo datos desde archivos `.json` o integrando un botón UI que regenere la escena.
- Se podrían agrupar objetos bajo un contenedor para limpiar la jerarquía.

---

## ✅ Criterios cubiertos

- ✔️ Generación programática en tiempo de ejecución.
- ✔️ Uso de condicionales y estructuras para definir geometría.
- ✔️ Parametrización completa desde datos en Inspector.
- ✔️ Escena estructurada, clara y funcional.
- ✔️ Código comentado, limpio y reutilizable.