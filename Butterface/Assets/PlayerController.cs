using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour {
    public int catches;
    public Text catchText;
	// Use this for initialization
	void Start () {
        catches = 0;
        catchText.text = "Catches: "+catches;
	}
	
	// counts number of good catches
	public void goodCatch() {
        catches = catches + 1;
        catchText.text = "Catches: " + catches;
    }
}
