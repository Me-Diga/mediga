# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "mediga_dev" do |mediga_dev|

    mediga_dev.vm.box = "ubuntu/xenial64"

    mediga_dev.vm.network "forwarded_port", guest: 8000, host: 8000
    mediga_dev.vm.network "private_network", ip: "127.0.0.1"

    mediga_dev.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "2048"
    end

    mediga_dev.vm.provision "shell", inline: "apt-get install -y python"

    mediga_dev.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/dev/provision.yml"
    end

  end

end
