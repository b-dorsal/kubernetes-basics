https://www.youtube.com/watch?v=X48VuDVv0do

# Kubernetes Basics Tutorial

My introduction to managing kubernetes.
Trying to grow my knowledge of k8s outside of my usual GKE infrastructure configuration and troubleshooting role.

## Prerequisites
- minikube
- kubectl
- hyperkit
- docker CLI

## Usage

### Start Cluster

Start Minikube using kyperkid VM driver
```bash
minikube start --driver=hyperkit
```

### Setup Mongo

Create secrets for MongoDB username and password
```bash
echo -n 'username' | base64
echo -n 'password' | base64
```

Apply secrets
```bash
kubectl apply -f mongo-secret.yaml
```

Apply Mongo DB Deployment and Service
```bash
kubectl apply -f mongo.yaml
```

Apply Mongo Express Config Map
```bash
kubectl apply -f mongo-configmap.yaml
```

Apply Mongo Express Deployment and Service
```bash
kubectl apply -f mongo-express.yaml
```

Assign External IP to Mongo Express LB Service
```bash
minikube service mongo-express-service
```


### Setup Flask App

I'm using Docker Hub...

Build the docker file
```bash
docker build -t <USERNAME>/flask-kubernetes .
```

Login to Docker Hub
```bash
docker login
```

Push the image to Docker Hub
```bash
docker push <USERNAME>/flask-kubernetes
```

Run the image locally to test
```bash
docker run -p 5000:5000 <USERNAME>/flask-kubernetes:latest
```

Apply Flask App Deployment and Service
```bash
kubectl apply -f flask-app.yaml
```

Assign External IP to Flask App LB Service
```bash
minikube service flask-app-service
```

### Basic Commands for Checking on the Cluster
Check on your cluster
```bash
kubectl get all
kubectl get deployment
kubectl get service
kubectl get pod -o wide
kubectl describe service <SERVICE_NAME>
```


## Docker Hub Images Links
- [MongoDB Official Image](https://hub.docker.com/_/mongo)
- [Mongo Express Official Image](https://hub.docker.com/_/mongo-express)














