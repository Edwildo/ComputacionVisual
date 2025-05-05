using UnityEngine;
using UnityEngine.UI;

public class TransformController : MonoBehaviour
{
    public Transform targetObject;
    public Slider positionXSlider;
    public Slider rotationYSlider;

    void Start()
    {
        positionXSlider.onValueChanged.AddListener(UpdatePositionX);
        rotationYSlider.onValueChanged.AddListener(UpdateRotationY);
    }

    void UpdatePositionX(float value)
    {
        if (targetObject != null)
        {
            Vector3 currentPosition = targetObject.position;
            currentPosition.x = value;
            targetObject.position = currentPosition;
        }
    }

    void UpdateRotationY(float value)
    {
        if (targetObject != null)
        {
            Vector3 currentRotation = targetObject.rotation.eulerAngles;
            currentRotation.y = value;
            targetObject.rotation = Quaternion.Euler(currentRotation);
        }
    }
}
