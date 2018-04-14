## Local Testbed

### Install Required Packages
We provide Vagrant File for supporting development and testing in local host.
Before creating testing environment, you should ensure that required packages
are installed. The required packages are listed below.
- Ansible (Latest Version)
- Vagrant
- VirtualBox
- Python 2.7

### Prepare SSH Key
Vagrant copies SSH public key of host into guest VM, and adds the key to
authorized_keys file. So ensure that you have SSH key at "~/.ssh/id_rsa.pub"
If you don't have a key, then execute below command.
```bash
$ ssh-keygen
```

### Modify Vagrant File
You can adjusts detailed configuration of testing environment by modifying
variables in Vagrant File. Modify those variables according to your requirement.

```bash
$ vim Vagrantfile

# In Vagrantfile, modify below variables
CLUSTER_NUMBERS=1
CONTROL_NUMBERS=1
CLIENT_NUMBERS=1

CONTROL_CPU="2"
CONTROL_RAM="2048"
CLIENT_CPU="2"
CLIENT_RAM="2048"
MGMT_IP_PREFIX="192.168.100.1"
CTRL_IP_PREFIX="192.168.101.1"
DATA_IP_PREFIX="192.168.102.1"
```

### Create testing environment with Vagrant
Finally, you prepare to create the testing environment. Follow below instruction.
```bash
# For checking format of Vagrant file and VM list
$ vagrant status
# For creating all VMs in the list
$ vagrant up
# For creating specific VMs
$ vagrant up <VM Names>
```

Creating the environment may take more than 10~20 minutes depend on your
Vagrant File. Take a break with a cup of coffee :)

After finishing the creation, you can access the VM without asking password.
```bash
$ ssh vagrant@<VM IP address>
```

### Writing Ansible inventory file for testing environment
```yaml
$ vim ./test_inventory.yml
# In test_inventory.yml, write network information for each box.
# If we create one control VM and one compute VM, then
all:
  children:
    control:
      hosts:
        opestack-control1-1:
          ansible_host: 192.168.100.111
          ansible_user: vagrant
          mgmt_ip: 192.168.100.111
          mgmt_mask: 255.255.255.0
          ctrl_ip: 192.168.101.111
          ctrl_mask: 255.255.255.0
          data_ip: 192.168.102.111
          data_mask: 255.255.255.0

    compute:
      hosts:
        openstack-compute1-1:
          ansible_host: 192.168.100.112
          ansible_user: vagrant
          mgmt_ip: 192.168.100.112
          mgmt_mask: 255.255.255.0
          ctrl_ip: 192.168.101.112
          ctrl_mask: 255.255.255.0
          data_ip: 192.168.102.112
          data_mask: 255.255.255.0
```

### Ansible Testing
```bash
$ ansible-playbook -i ./test_inventory -l control install_control.yml
$ ansible-playbook -i ./test_inventory -l compute install_compute.yml
```
