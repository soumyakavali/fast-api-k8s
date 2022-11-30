This is micro-service which will provide REST API"s for all finding operations. This is developed by using python fastapi framework.

# How to run locall

1. Open command prompt in project directory and create python virtual environment.
    ```
    python -m venv venv --system-site-packages
    
    ```
2. Activate python virtual environment.
    ```
    source ./venv/bin/activate
    ```
3. Install all python dependencies.
    ```
    pip install -r requirments.txt
    ```
4. Set below environment variables.
    ```
    export DB_NAME=test_db
    export DB_COLLECTION=test_db_collection
    export MONGO_DB_URL=mongodb://localmongodb:27701
    ```
6. Finally got to app folder and run the finding service with below command.
    ```
    cd app/
    uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8080
    ```
# Create Docker image and push to remote registry

1. Build local image with tag.
    ```
    docker build -t finding:latest .
    ```
2. Tag it for remote registry.
    ```
    Add comamnds for tagging
    ```
# Deploy to kubernet cluster.
1. Update your kubectl config to point to your destination cluster.
2. Deploy secret.
    ```
    kubectl apply -f ./Deployment/secret.yaml
    ```
4. Deploy ConfigMap.
    ```
    kubectl apply -f ./Deployment/configmap.yaml
    ```
6. Deploy finding deployment.
    ```
    kubectl apply -f ./Deployment/deployment.yaml
    ```
8. Deploy finding ingress.
    ```
    kubectl apply -f ./Deployment/ingress.yaml
    ```
