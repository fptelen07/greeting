# AWS EKS Python Greeting Application

This project contains a simple Python Flask application that returns a greeting message. It is containerized with Docker and designed to be deployed on Amazon EKS (Elastic Kubernetes Service).

## Application Structure

- `app.py` - Flask application that serves a simple greeting endpoint
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container definition
- `k8s/` - Kubernetes deployment manifests
- `buildspec.yml` - AWS CodeBuild specification
- `setup_eks.sh` - Helper script to set up EKS and deploy the application

## Prerequisites

- AWS CLI configured with appropriate permissions
- Docker installed
- kubectl installed
- eksctl installed (optional, for cluster creation)

## Local Development

1. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run the application locally:
   ```
   python app.py
   ```

3. Access the application at http://localhost:8080/hello

## Deployment to AWS EKS

### Option 1: Manual Deployment

1. Build and tag the Docker image:
   ```
   docker build -t greeting-app .
   ```

2. Create an ECR repository and push the image:
   ```
   aws ecr create-repository --repository-name greeting-app
   aws ecr get-login-password | docker login --username AWS --password-stdin <your-aws-account-id>.dkr.ecr.<region>.amazonaws.com
   docker tag greeting-app:latest <your-aws-account-id>.dkr.ecr.<region>.amazonaws.com/greeting-app:latest
   docker push <your-aws-account-id>.dkr.ecr.<region>.amazonaws.com/greeting-app:latest
   ```

3. Deploy to EKS:
   ```
   # Update image in deployment.yaml with your ECR image URL
   kubectl apply -f k8s/deployment.yaml
   ```

### Option 2: Automated Deployment

Use the provided setup script:
```
chmod +x setup_eks.sh
./setup_eks.sh
```

### Option 3: CI/CD Pipeline

This project includes a `buildspec.yml` file for AWS CodeBuild. Set up a CodeBuild project pointing to your repository and configure the following environment variables:

- `AWS_DEFAULT_REGION`: Your AWS region
- `AWS_ACCOUNT_ID`: Your AWS account ID
- `EKS_CLUSTER_NAME`: The name of your EKS cluster

## Accessing the Application

After deployment, you can access the application via the LoadBalancer URL:

```
kubectl get svc greeting-service
```

The application will be available at `http://<EXTERNAL-IP>/hello`

## Security

The CI/CD pipeline includes a security scan using Trivy to check for vulnerabilities in the container image.

## Cleanup

To remove all resources:

```
kubectl delete -f k8s/deployment.yaml
aws ecr delete-repository --repository-name greeting-app --force
# If you want to delete the EKS cluster:
# aws eks delete-cluster --name greeting-cluster
```
