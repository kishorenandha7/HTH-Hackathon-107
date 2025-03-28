using UnityEngine;
using UnityEngine.UI;

public class BodySystemToggle : MonoBehaviour
{
    public GameObject skeletalSystem;
    public GameObject muscularSystem;
    public Toggle skeletalToggle;
    public Toggle muscularToggle;

    void Start()
    {
        skeletalToggle.onValueChanged.AddListener(delegate { ToggleSystem(skeletalSystem, skeletalToggle.isOn); });
        muscularToggle.onValueChanged.AddListener(delegate { ToggleSystem(muscularSystem, muscularToggle.isOn); });
    }

    void ToggleSystem(GameObject system, bool state)
    {
        if (system)
            system.SetActive(state);
    }
}
