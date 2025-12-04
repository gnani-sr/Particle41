# Infrastructure

AWS ECS deployment with VPC, load balancer, and private subnets.

## Usage

```bash
terraform init
cp terraform.tfvars.example terraform.tfvars
terraform apply
terraform output load_balancer_url
```

## Cleanup

```bash
terraform destroy
```