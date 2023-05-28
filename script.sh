#!/bin/bash

# Enabling YUM Repositories
subscription-manager repos --enable rhocp-4.13-for-rhel-9-x86_64-rpms
subscription-manager repos --enable rhocp-4.13-for-rhel-9-x86_64-source-rpms

# Updating and installing required modules
yum clean all
yum update -y
yum install git
yum install pip
yum install tesseract
yum install openshift-clients

# Updating and installing required packages
pip install --upgrade pip
pip install streamlit
pip install PIL
pip install pytesseract
pip install uuid
pip install textblob

# Creating required image and container
podman stop image_text2
podman rm image_text2
podman rmi image_text2
podman build -t image_text2 .
podman images | grep image_text2
podman run -d -p 8501:8501 --name image_text2 localhost/image_text2:latest
podman ps | grep image_text2
podman login docker.io 
podman tag localhost/image_text2:latest docker.io/rba991/image_text2:latest
podman push docker.io/rba991/image_text2:latest

# Creating and deploying web app on Open Shift
oc login --token="Your Token" --server="Your API End Point"
oc projects
oc status
oc get pods
oc new-app docker.io/rba991/image_text2:latest
oc status
oc get pods
oc expose service image-text2
oc get route
