using UnityEngine;
using UnityEngine.UI;

public class AnatomyInfo : MonoBehaviour
{
    public static AnatomyInfo instance;
    public Text infoText;

    void Awake()
    {
        instance = this;
    }

    public static void ShowInfo(string partName)
    {
        instance.infoText.text = "You selected: " + partName;
    }
}
