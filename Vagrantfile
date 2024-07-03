Vagrant.configure("2") do |config|
    config.vm.define "Splunk" do |c|
        c.vm.box = "ubuntu/jammy64"
        c.vm.hostname = "Splunk"
        c.vm.network "forwarded_port", guest: 8000, host: 8000, protocol: "tcp"
        c.vm.network "private_network", ip: "192.168.56.100", virtualbox__intnet: true
        c.vm.provider "virtualbox" do |v|
            v.memory = 8192
            v.cpus = 4
            #v.gui = true
        end
        c.vm.synced_folder ".", "/vagrant", disabled: true
        c.vm.provision "ansible" do |ansible|
            ansible.playbook = "splunk.yml"
            ansible.inventory_path = "inventory.ini"
        end
    end
# end

    config.vm.define "Client" do |c|
        c.vm.box = "debian/bookworm64"
        c.vm.hostname = "Client"
        c.vm.network "private_network", ip: "192.168.56.50", virtualbox__intnet: true
        c.vm.provider "virtualbox" do |v|
            v.memory = 1024
            v.cpus = 1
            #v.gui = true
        end
        c.vm.synced_folder ".", "/vagrant", disabled: true
        c.vm.provision "ansible" do |ansible|
            ansible.playbook = "logs_forwarder.yaml"
            ansible.inventory_path = "inventory.ini"
        end
    end
end
#     config.vm.define "Client2" do |c|
#         c.vm.box = "debian/bookworm64"
#         c.vm.hostname = "Client2"
#         c.vm.network "private_network", ip: "192.168.56.51", virtualbox__intnet: true
#         c.vm.provider "virtualbox" do |v|
#             v.memory = 1024
#             v.cpus = 1
#             #v.gui = true
#         end
#         c.vm.synced_folder ".", "/vagrant", disabled: true
#         c.vm.provision "ansible" do |ansible|
#             ansible.playbook = "client2_logs_forwarder.yaml"
#             ansible.inventory_path = "inventory.ini"
#         end
#     end
# end
