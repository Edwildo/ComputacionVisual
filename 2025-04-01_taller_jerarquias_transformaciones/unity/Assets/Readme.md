# 🧪 Taller - Jerarquías y Transformaciones: El Árbol del Movimiento

## 🎯 Objetivo
Explorar cómo las transformaciones aplicadas a un objeto padre afectan a sus hijos en una jerarquía de escena, mediante estructuras de nodos padre-hijo en 3D. Se implementaron sliders para controlar dinámicamente la posición y rotación del nodo raíz en tiempo real.

---

## 🔧 Entornos desarrollados

### 1️⃣ Three.js con React Three Fiber
#### 🛠 Implementación
- Se creó un proyecto con Vite + React Three Fiber.
- Se usó un `<group>` como nodo padre y tres `<mesh>` como cubos/esferas anidadas (padre → hijo → nieto).
- Se aplicaron transformaciones (rotación y traslación) al grupo padre.
- Se integró la librería **Leva** para controlar los sliders de rotaciónY y posiciónX.
- Se renderizó el resultado en pantalla completa y con fondo blanco.

#### 📸 Evidencia visual
![threejs](./threejs/demo.gif)

#### 🔗 Código clave
```jsx
const { rotationY, positionX } = useControls({
  rotationY: { value: 0, min: -Math.PI, max: Math.PI },
  positionX: { value: 0, min: -5, max: 5 }
});
✅ Comportamiento
La rotación del padre arrastra visualmente al hijo y al nieto.

El control de sliders se refleja inmediatamente en los elementos anidados.

2️⃣ Unity
🛠 Implementación
Se creó una jerarquía de objetos: RootObject → Hijo_Cubo → Nieto_Esfera.

Se usó UI con dos sliders (Slider_PositionX, Slider_RotationY) para controlar las transformaciones del nodo raíz.

Se escribió un script en C# llamado TransformController que actualiza en tiempo real la posición X y la rotación Y del nodo padre.

📸 Evidencia visual

🔗 Fragmento de código
csharp
Copiar
Editar
public void UpdateRotationY(float value)
{
    if (targetObject != null)
    {
        Vector3 currentRotation = targetObject.eulerAngles;
        currentRotation.y = value;
        targetObject.eulerAngles = currentRotation;
    }
}
✅ Comportamiento
Los hijos responden correctamente a las transformaciones del padre.

Cambios se reflejan en tiempo real desde los sliders.

✅ Aprendizajes y dificultades
Se comprendió claramente la propagación de transformaciones desde un padre a sus hijos en una escena 3D.

En Three.js, la composición jerárquica con <group> fue intuitiva.

En Unity, se aprendió a conectar sliders con scripts mediante onValueChanged.

Dificultad inicial para encontrar el canvas y asignar el script correctamente en Unity, resuelta revisando cuidadosamente el Inspector.

📁 Estructura del repositorio
cpp
Copiar
Editar
yyyy-mm-dd_taller_jerarquias_transformaciones/
├── threejs/
│   ├── public/
│   └── src/
│       ├── App.jsx
│       └── components/
│           └── HierarchyScene.jsx
├── unity/
│   ├── Assets/
│   │   └── Scripts/
│   │       └── TransformController.cs
├── README.md
✅ Criterios cumplidos
 Estructura jerárquica funcional implementada correctamente.

 Transformaciones aplicadas y visibles en objetos hijos.

 Control dinámico de transformaciones mediante UI o sliders.

 Repositorio ordenado con subcarpetas por entorno.

 Código comentado y funcional.

 Commits descriptivos en inglés.

 README completo con explicación, prompts y evidencias visuales (GIF).

yaml
Copiar
Editar
