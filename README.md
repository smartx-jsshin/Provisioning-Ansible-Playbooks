# Provisioning-Ansible-Playbooks
Ansible Playbooks for SmartX Tower and Post

<H2> Ansible Tutorial: How to use Playbooks </H2>
<H3> Check SSH Connectivity to remote Hosts </H3>
ansible -m ping -i <inventory_file> <hostname>
<H3> Execute Ansible Playbook </H3>
ansible-playbook -i <inventory_file> -u <LinuxAccount> <Playbook_file>
