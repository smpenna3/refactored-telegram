using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ResetPos : MonoBehaviour {
    Vector3 initalPos;
	// Use this for initialization
	void Start () {
        initalPos = gameObject.transform.position;
	}
	
	// Update is called once per frame
	public void Reset()
    {
            Debug.Log("reset_active");
            gameObject.transform.position = initalPos;
        
    }
}
