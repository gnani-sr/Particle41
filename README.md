# SimpleTimeService

Microservice that returns timestamp and client IP in JSON format.

## Local Development

```bash
docker build -t simpletimeservice .
docker run -p 8080:8080 simpletimeservice
curl http://localhost:8080
```

## AWS Deployment

### Prerequisites
- Docker Desktop
- Terraform
- AWS CLI configured

### Deploy

```bash
# Build and push image
docker build -t simpletimeservice .
docker tag simpletimeservice your-username/simpletimeservice:latest
docker push your-username/simpletimeservice:latest

# Deploy infrastructure
cd terraform
terraform init
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your image URL
terraform apply

# Get service URL
terraform output load_balancer_url
```

### Test

```bash
curl http://simpletimeservice-alb-241207875.us-east-1.elb.amazonaws.com/
```

### Cleanup

```bash
terraform destroy
```

## Response Format

```json
{
  "timestamp": "2024-01-01T12:00:00.000Z",
  "ip": "127.0.0.1"
}
```