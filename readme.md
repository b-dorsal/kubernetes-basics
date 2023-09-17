https://www.youtube.com/watch?v=X48VuDVv0do

# Kubernetes Basics Tutorial

My introduction to managing kubernetes.
Trying to grow my knowledge of k8s outside of my usual GKE infrastructure configuration and troubleshooting role.

## Prerequisites
- minikube
- kubectl
- hyperkit

## Usage

Start Minikube using kyperkid VM driver
```bash
minikube start --driver=hyperkit
```

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

Assign External IP to LB Service
```bash
minikube service mongo-express-service
```

Check on your cluster
```bash
kubectl get all
kubectl get pod

```

## Docker Hub Images Links
- https://hub.docker.com/_/mongo
- https://hub.docker.com/_/mongo-express














