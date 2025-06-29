# Kubernetes Django Messaging App Deployment

This project demonstrates the deployment and management of a Django messaging application using Kubernetes. It covers essential Kubernetes concepts including clustering, deployments, scaling, ingress configuration, and advanced deployment strategies.

## 🎯 Project Overview

This repository contains all the necessary files and scripts to:
- Set up a local Kubernetes cluster using Minikube
- Deploy a Django messaging application
- Implement scaling strategies
- Configure ingress for external access
- Execute blue-green and rolling deployment strategies

## 📁 Project Structure

```
alx-backend-python/
└── messaging_app/
    ├── README.md
    ├── kurbeScript                 # Kubernetes cluster setup script
    ├── deployment.yaml            # Initial Django app deployment
    ├── blue_deployment.yaml       # Blue deployment configuration
    ├── green_deployment.yaml      # Green deployment configuration
    ├── kubeservice.yaml          # Service configuration for blue-green
    ├── ingress.yaml              # Ingress controller configuration
    ├── commands.txt              # Commands used for ingress setup
    ├── kubctl-0x01              # Scaling and monitoring script
    ├── kubctl-0x02              # Blue-green deployment script
    └── kubctl-0x03              # Rolling update script
```

## 🚀 Getting Started

### Prerequisites

- Linux operating system (Ubuntu/Debian recommended)
- Docker installed and running
- At least 2GB RAM available
- Virtualization support enabled
- Internet connection for downloading components

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/alx-backend-python.git
   cd alx-backend-python/messaging_app
   ```

2. **Set up Kubernetes cluster:**
   ```bash
   chmod +x kurbeScript
   ./kurbeScript
   ```

3. **Verify cluster is running:**
   ```bash
   kubectl cluster-info
   kubectl get nodes
   ```

## 📋 Task Breakdown

### Task 0: Install Kubernetes and Set Up Local Cluster

**Objective:** Set up and configure a local Kubernetes cluster using Minikube.

**Files:**
- `kurbeScript` - Automated setup script

**Features:**
- Cross-platform installation (Linux, macOS)
- Automatic installation of kubectl, Minikube, and Docker
- Prerequisites checking (memory, virtualization)
- Cluster verification and status reporting

**Usage:**
```bash
./kurbeScript
```

**What it does:**
- Installs kubectl, Minikube, and Docker (if not present)
- Starts Minikube cluster with 2GB memory and 2 CPUs
- Verifies cluster status using `kubectl cluster-info`
- Lists all available pods across namespaces

---

### Task 1: Deploy Django Messaging App

**Objective:** Deploy the containerized Django application on Kubernetes.

**Files:**
- `deployment.yaml` - Kubernetes deployment configuration

**Key Components:**
- Deployment with 2 replicas
- Resource requests and limits
- Health checks (liveness and readiness probes)
- ClusterIP service for internal communication

**Deployment:**
```bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl logs <pod-name>
```

**Configuration highlights:**
- Uses Django messaging app Docker image
- Implements proper resource management
- Includes health check endpoints
- Exposes service on port 8000

---

### Task 2: Scale the Django App

**Objective:** Learn application scaling in Kubernetes.

**Files:**
- `kubctl-0x01` - Scaling and monitoring script

**Features:**
- Scales deployment to 3 replicas
- Performs load testing using `wrk`
- Monitors resource usage with `kubectl top`
- Verifies pod distribution and health

**Usage:**
```bash
chmod +x kubctl-0x01
./kubctl-0x01
```

**What it does:**
- Scales the deployment using `kubectl scale`
- Runs load tests to validate performance
- Monitors CPU and memory usage
- Provides detailed pod status information

---

### Task 3: Set Up Kubernetes Ingress

**Objective:** Expose Django app externally using Ingress controller.

**Files:**
- `ingress.yaml` - Ingress resource configuration
- `commands.txt` - Commands used for setup

**Components:**
- Nginx Ingress Controller installation
- Path-based routing configuration
- SSL/TLS termination support
- Multiple service routing capabilities

**Setup:**
```bash
# Install Nginx Ingress Controller
minikube addons enable ingress

# Apply Ingress configuration
kubectl apply -f ingress.yaml

# Check Ingress status
kubectl get ingress
```

**Features:**
- Routes `/api/` paths to Django service
- Supports multiple domain configurations
- Load balancing across pods
- Health check integration

---

### Task 4: Blue-Green Deployment Strategy

**Objective:** Implement zero-downtime deployments using blue-green strategy.

**Files:**
- `blue_deployment.yaml` - Blue version deployment
- `green_deployment.yaml` - Green version deployment
- `kubeservice.yaml` - Service switching configuration
- `kubctl-0x02` - Blue-green deployment script

**Strategy:**
1. Deploy green version alongside blue
2. Test green version thoroughly
3. Switch traffic from blue to green
4. Monitor for issues and rollback if needed

**Usage:**
```bash
chmod +x kubctl-0x02
./kubctl-0x02
```

**Benefits:**
- Zero-downtime deployments
- Easy rollback capabilities
- Full testing before traffic switch
- Risk mitigation for production deployments

---

### Task 5: Rolling Updates

**Objective:** Update applications without downtime using rolling updates.

**Files:**
- `blue_deployment.yaml` (updated with v2.0)
- `kubctl-0x03` - Rolling update script

**Process:**
- Updates Docker image to version 2.0
- Monitors rollout progress
- Tests application during update
- Verifies completion and health

**Usage:**
```bash
chmod +x kubctl-0x03
./kubctl-0x03
```

**Features:**
- Continuous availability testing
- Progress monitoring
- Automatic rollback on failure
- Performance impact analysis

## 🛠️ Best Practices Implemented

### 1. **Declarative Configurations**
- All deployments defined in YAML files
- Version controlled configurations
- Reproducible deployments

### 2. **Resource Management**
- CPU and memory requests/limits defined
- Efficient resource utilization
- Prevention of resource starvation

### 3. **Health Checks**
- Liveness probes for container health
- Readiness probes for traffic routing
- Automatic recovery from failures

### 4. **Security**
- Principle of least privilege
- Secure image practices
- ConfigMaps and Secrets separation

### 5. **Monitoring & Observability**
- Resource usage monitoring
- Application log management
- Health status tracking

### 6. **Scaling & Performance**
- Horizontal scaling capabilities
- Load testing integration
- Performance monitoring

## 🔧 Common Commands

### Cluster Management
```bash
# Check cluster status
kubectl cluster-info
kubectl get nodes

# View all resources
kubectl get all --all-namespaces
```

### Application Management
```bash
# Deploy application
kubectl apply -f deployment.yaml

# Scale application
kubectl scale deployment django-messaging-app --replicas=3

# Check pods
kubectl get pods
kubectl logs <pod-name>
```

### Monitoring
```bash
# Resource usage
kubectl top nodes
kubectl top pods

# Describe resources
kubectl describe deployment django-messaging-app
kubectl describe service django-service
```

### Troubleshooting
```bash
# Debug pod issues
kubectl describe pod <pod-name>
kubectl logs <pod-name> --previous

# Check events
kubectl get events --sort-by=.metadata.creationTimestamp
```

## 🐛 Troubleshooting

### Common Issues

1. **Minikube won't start:**
   - Check virtualization support: `grep -E 'vmx|svm' /proc/cpuinfo`
   - Ensure Docker is running: `docker ps`
   - Try: `minikube delete && minikube start`

2. **Pods stuck in Pending:**
   - Check resource availability: `kubectl describe pod <pod-name>`
   - Verify node capacity: `kubectl top nodes`

3. **Service not accessible:**
   - Check service endpoints: `kubectl get endpoints`
   - Verify ingress status: `kubectl get ingress`
   - Test internal connectivity: `kubectl port-forward`

4. **Image pull errors:**
   - Verify image exists and is accessible
   - Check imagePullPolicy settings
   - Ensure proper registry authentication

## 📊 Load Testing

The project includes load testing capabilities using `wrk`:

```bash
# Install wrk (if not available)
sudo apt-get install wrk

# Run load test
wrk -t12 -c400 -d30s http://your-app-url/
```

## 🔒 Security Considerations

- Regular security updates for base images
- Proper RBAC configuration
- Network policies for pod communication
- Secrets management for sensitive data
- Container security scanning

## 📈 Monitoring and Observability

- Resource usage tracking with `kubectl top`
- Application logs via `kubectl logs`
- Health check monitoring
- Performance metrics collection
- Alert configuration for critical issues

## 🚀 Advanced Features

### Auto-scaling
```bash
# Enable Horizontal Pod Autoscaler
kubectl autoscale deployment django-messaging-app --cpu-percent=50 --min=1 --max=10
```

### Rolling Updates
```bash
# Update image
kubectl set image deployment/django-messaging-app django-app=new-image:tag

# Monitor rollout
kubectl rollout status deployment/django-messaging-app

# Rollback if needed
kubectl rollout undo deployment/django-messaging-app
```

## 📚 Additional Resources

- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the ALX Backend Python curriculum and is intended for educational purposes.

---

**Note:** This project demonstrates Kubernetes fundamentals and deployment strategies. In production environments, additional considerations for security, monitoring, and infrastructure management would be required.
