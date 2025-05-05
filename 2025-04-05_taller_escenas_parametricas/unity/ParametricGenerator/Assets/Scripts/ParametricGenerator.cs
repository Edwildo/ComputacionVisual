using UnityEngine;

public class ParametricGenerator : MonoBehaviour
{
    [System.Serializable]
    public class ParametricObject
    {
        public Vector3 position;
        public Vector3 scale;
        public Color color;
        public string type; // "cube", "sphere", "cylinder"
    }

    public ParametricObject[] objects;

    void Start()
    {
        foreach (var obj in objects)
        {
            GameObject shape = null;

            // Elegir tipo de objeto
            switch (obj.type.ToLower())
            {
                case "cube":
                    shape = GameObject.CreatePrimitive(PrimitiveType.Cube);
                    break;
                case "sphere":
                    shape = GameObject.CreatePrimitive(PrimitiveType.Sphere);
                    break;
                case "cylinder":
                    shape = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
                    break;
                default:
                    Debug.LogWarning("Tipo desconocido: " + obj.type);
                    continue;
            }

            // Aplicar parámetros
            shape.transform.position = obj.position;
            shape.transform.localScale = obj.scale;

            var renderer = shape.GetComponent<Renderer>();
            renderer.material.color = obj.color;
        }
    }
}
