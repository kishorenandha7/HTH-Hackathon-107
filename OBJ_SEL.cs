using UnityEngine;

public class ObjectSelector : MonoBehaviour
{
    private Renderer objRenderer;
    private Color originalColor;

    void Start()
    {
        objRenderer = GetComponent<Renderer>();
        if (objRenderer)
            originalColor = objRenderer.material.color;
    }

    void OnMouseDown()
    {
        if (objRenderer)
        {
            objRenderer.material.color = Color.yellow;  // Highlight selected part
            AnatomyInfo.ShowInfo(gameObject.name);  // Call UI function to display info
        }
    }

    void OnMouseExit()
    {
        if (objRenderer)
            objRenderer.material.color = originalColor;  // Reset color
    }
}
