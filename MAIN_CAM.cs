using UnityEngine;

public class CameraControl : MonoBehaviour
{
    public float rotationSpeed = 5f;
    public float zoomSpeed = 2f;
    public float panSpeed = 0.5f;
    
    private Vector3 lastMousePosition;

    void Update()
    {
        // Rotate Model
        if (Input.GetMouseButton(0))  // Left click
        {
            Vector3 delta = Input.mousePosition - lastMousePosition;
            transform.Rotate(Vector3.up, -delta.x * rotationSpeed, Space.World);
            transform.Rotate(Vector3.right, delta.y * rotationSpeed, Space.World);
        }

        // Zoom In/Out
        float scroll = Input.GetAxis("Mouse ScrollWheel");
        transform.position += transform.forward * scroll * zoomSpeed;

        // Pan View
        if (Input.GetMouseButton(2))  // Middle mouse button
        {
            Vector3 pan = new Vector3(-Input.GetAxis("Mouse X"), -Input.GetAxis("Mouse Y"), 0) * panSpeed;
            transform.Translate(pan, Space.Self);
        }

        lastMousePosition = Input.mousePosition;
    }
}
