using UnityEngine;
using UnityEngine.UI;

// Enhanced Anatomy Info UI
public class AnatomyInfo : MonoBehaviour
{
    public static AnatomyInfo instance;
    public Text infoText;
    public AudioSource audioSource;
    public AudioClip[] narrationClips;

    void Awake()
    {
        instance = this;
    }

    public static void ShowInfo(string partName, int clipIndex)
    {
        instance.infoText.text = "You selected: " + partName + "\nDescription: [Detailed Info Here]";
        if (instance.audioSource && instance.narrationClips.Length > clipIndex)
        {
            instance.audioSource.clip = instance.narrationClips[clipIndex];
            instance.audioSource.Play();
        }
    }
}

// Enhanced Object Selection
public class ObjectSelector : MonoBehaviour
{
    private Renderer objRenderer;
    private Color originalColor;
    public int narrationIndex;

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
            objRenderer.material.color = Color.yellow;  // Highlight
            AnatomyInfo.ShowInfo(gameObject.name, narrationIndex);  // Call UI
            transform.localScale *= 1.1f;  // Slightly enlarge selected object
        }
    }

    void OnMouseExit()
    {
        if (objRenderer)
        {
            objRenderer.material.color = originalColor;  // Reset color
            transform.localScale /= 1.1f;  // Reset scale
        }
    }
}

// Enhanced Camera Control
public class CameraControl : MonoBehaviour
{
    public float rotationSpeed = 5f;
    public float zoomSpeed = 2f;
    public float panSpeed = 0.5f;
    public float smoothDamp = 0.1f;
    private Quaternion targetRotation;
    private Vector3 lastMousePosition;

    void Start()
    {
        targetRotation = transform.rotation;
    }

    void Update()
    {
        if (Input.GetMouseButton(0))  // Left-click rotate
        {
            Vector3 delta = Input.mousePosition - lastMousePosition;
            targetRotation *= Quaternion.Euler(-delta.y * rotationSpeed, delta.x * rotationSpeed, 0);
        }
        
        transform.rotation = Quaternion.Lerp(transform.rotation, targetRotation, smoothDamp);
        
        float scroll = Input.GetAxis("Mouse ScrollWheel");
        transform.position += transform.forward * scroll * zoomSpeed;

        if (Input.GetMouseButton(2))  // Middle mouse pan
        {
            Vector3 pan = new Vector3(-Input.GetAxis("Mouse X"), -Input.GetAxis("Mouse Y"), 0) * panSpeed;
            transform.Translate(pan, Space.Self);
        }

        if (Input.GetKeyDown(KeyCode.R))  // Reset camera
        {
            transform.position = Vector3.zero;
            transform.rotation = Quaternion.identity;
        }

        lastMousePosition = Input.mousePosition;
    }
}

// Enhanced UI Toggle System
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
        {
            StartCoroutine(FadeSystem(system, state));
        }
    }

    IEnumerator FadeSystem(GameObject system, bool state)
    {
        CanvasGroup canvasGroup = system.GetComponent<CanvasGroup>();
        if (!canvasGroup)
        {
            canvasGroup = system.AddComponent<CanvasGroup>();
        }

        float targetAlpha = state ? 1 : 0;
        while (!Mathf.Approximately(canvasGroup.alpha, targetAlpha))
        {
            canvasGroup.alpha = Mathf.MoveTowards(canvasGroup.alpha, targetAlpha, Time.deltaTime * 2);
            yield return null;
        }
        system.SetActive(state);
    }
}
