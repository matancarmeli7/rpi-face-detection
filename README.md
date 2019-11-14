rpi-face-detection
=================
 this project contains resources for building and deploying python-base face detection application on raspberry pi inside a kubernetes cluster.

----------------------------------------------------------
## jenkinsfile
make sure to put your own parameters in the file:
 * registry
 * registryCredential
 
## inventory
put your kubernetes cluster address

## kuberenetesResources/full-deployment.yml
pass to the template your registry address and build number

## use the api
1. use a post call with postman\curl and pass img = path/to/image
2. use client.py to pass the img.
