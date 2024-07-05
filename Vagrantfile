Vagrant.configure("2") do |config|
    # 1st VM : Splunk
    config.vm.define "splunk" do |c|
        c.vm.box = "ubuntu/jammy64"
        c.vm.hostname = "splunk"
        c.vm.network "forwarded_port", guest: 8000, host: 8000, protocol: "tcp"
        c.vm.network "forwarded_port", guest: 8089, host: 8089, protocol: "tcp"
        c.vm.network "private_network", ip: "192.168.56.100", virtualbox__intnet: true
        c.vm.provider "virtualbox" do |v|
            v.memory = 8192
            v.cpus = 4
        end
        c.vm.synced_folder ".", "/vagrant", disabled: true
    end

    # 2nd VM : Client
    config.vm.define "client" do |c|
        c.vm.box = "debian/bookworm64"
        c.vm.hostname = "client"
        c.vm.network "private_network", ip: "192.168.56.50", virtualbox__intnet: true
        c.vm.provider "virtualbox" do |v|
            v.memory = 1024
            v.cpus = 1
        end
        c.vm.synced_folder ".", "/vagrant", disabled: true
    end


    # 3rd VM : Ansible Control Node
    config.vm.define "provisionner" do |c|
        c.vm.box = "debian/bookworm64"
        c.vm.hostname = "provisionner"
        c.vm.network "private_network", ip: "192.168.56.10", virtualbox__intnet: true
        c.vm.provider "virtualbox" do |v|
            v.memory = 512
            v.cpus = 1
        end
        c.vm.synced_folder ".", "/vagrant", disabled: true
        c.vm.provision "file", source: ".vagrant/machines/splunk/virtualbox/private_key", destination: "/home/vagrant/.ssh/splunk_private_key"
        c.vm.provision "file", source: ".vagrant/machines/client/virtualbox/private_key", destination: "/home/vagrant/.ssh/client_private_key"
        c.vm.provision "file", source: "inventory.ini", destination: "/home/vagrant/inventory.ini"
        c.vm.provision "file", source: "splunk.yml", destination: "/home/vagrant/splunk.yml"
        c.vm.provision "file", source: "logs_forwarder.yaml", destination: "/home/vagrant/logs_forwarder.yaml"
        c.vm.provision "file", source: "alerts.zip", destination: "/home/vagrant/alerts.zip"
        c.vm.provision "shell", inline: <<-SHELL
            sudo echo "192.168.56.100 splunk" >> /etc/hosts
            sudo echo "192.168.56.50 client" >> /etc/hosts
            sudo apt-get update && sudo apt-get install unzip pipx -y
            unzip alerts.zip 
            sudo -u vagrant pipx install ansible-core
            export PATH=$PATH:/home/vagrant/.local/bin
            source .bashrc
            ansible-playbook -i inventory.ini -l splunk splunk.yml
            ansible-playbook -i inventory.ini -l client logs_forwarder.yaml
        SHELL
    end
end
