# OpenStack Playbook

## Target Playgrounds
- Minimal OpenStack Configuration
  - One OpenStack control box & Multiple OpenStack Compute boxes
  - OpenStack Services: Keystone, Glance, Cinder, Nova, Neutron, Horizon
  - Networking: Self-Service Networking (VXLAN-based) with Open vSwitch

## Assumption

## How to use
### Dynamically Load Inventory
1. Execute load_inventory.yml

### Install OpenStack Control
2. Execute install_control.yml

### Install OpenStack Compute
3. Execute install_compute.yml

## Local Testing
Refer README.md in subdirectory "local_testbed"

## In Progress
- Support K-Posts in K-ONE Playground
- Support OF@KOREN Playground
- Support OF@TEIN Playground
