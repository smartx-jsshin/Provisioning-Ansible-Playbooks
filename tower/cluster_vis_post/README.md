# Cluster Visibility Post

# How to Use
## Modifying inventory.yaml
- Ansible will automatically access target boxes based on "inventory.yaml". So you have to modify "inventory.yaml" according to your infrastructure.
- But you should be follow some restrictions listed below


- You should keep the structure of inventory.yaml. If not, this playbook will not be working.
- In this version, this playbook doesn't use "mgmt_ip" and "data_ip". So those fields can be empty.


- The number of dashboard hosts should be 1.
- The number of datalake control hosts should be 1.
- In this version, this playbook install nothing in datalake client hosts. So datalake client host can be empty. (In future We will implement a playbook for OpenTSDB-based datalake, then the clients should be multiple.)

## Modifying configurations.yaml
- Ansible loads variables in "configurations.yaml" that is required for installing Grafana and InfluxDB
- Before executing Ansible, you have to adjust variables (At least, ID & Password variables)

## Executing Ansible
```bash
~ $ ansible-playbook -i ./inventory.yaml provision_post.yaml
```

# Local Testing

## Modifying Vagrantfile according to your favor
```bash
~ $ cd local_testbed
~ $ vim Vagrantfile
```

Modifying below variables in Vagrantfile
```bash
CONTROL_NUMBERS=1
CLIENT_NUMBERS=0

CONTROL_CPU="2"
CONTROL_RAM="2048"
CLIENT_CPU="1"
CLIENT_RAM="1024"

MGMT_IP_PREFIX="192.168.100.11"
CTRL_IP_PREFIX="192.168.101.11"
DATA_IP_PREFIX="192.168.102.11"
```

## Creating Vagrant-based Virtual Testbed
```bash
~ $ vagrant up
```

## Executing Ansible
After creating the testbed, refer "How to Use" section
