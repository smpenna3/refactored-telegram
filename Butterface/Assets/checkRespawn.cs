using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class checkRespawn : MonoBehaviour {
    public Vector3 initialVelocity;
    Vector3 initialPos;

    public Rigidbody rb;
    // Use this for initialization
    void Start () {
        rb = GetComponent<Rigidbody>();
        rb.velocity = initialVelocity;
        initialPos = gameObject.transform.position;
    }
	
    public void respawn()
    {
        gameObject.transform.position = initialPos;
        rb.velocity = new Vector3(initialVelocity.x + Random.value, initialVelocity.y + Random.value, 
            initialVelocity.z - (Random.value));
    }
	// Update is called once per frame
	void Update () {
        if (gameObject.transform.position.y <  0.2)
        {
            respawn();
        }
	}
}
