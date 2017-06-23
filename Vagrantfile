Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Hello"

  config.vm.define "node1" do |node1|
    node1.vm.box = "centos/7"
    node1.vm.hostname = "node1.local"
    node1.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = "1"
    end
    node1.vm.network "private_network", ip: "172.28.128.3"
    node1.vm.synced_folder "node1/", "/vagrant", type: "virtualbox"
    node1.vm.synced_folder "provisioning/", "/vagrant/provisioning", type: "virtualbox"

    node1.vm.provision 'ansible_local' do |ansible|
      ansible.install_mode = 'default'
      ansible.verbose = true
      ansible.install = true
      ansible.playbook = 'provisioning/site.yml'
    end
  end

    config.vm.define "node4" do |node4|
      node4.vm.box = "centos/7"
      node4.vm.hostname = "node4.local"
      node4.vm.provider "virtualbox" do |vb|
        vb.memory = "4096"
        vb.cpus = "1"
      end
      node4.vm.network "private_network", ip: "172.28.128.6"
      node4.vm.synced_folder "node4/", "/vagrant", type: "virtualbox"
      node4.vm.synced_folder "provisioning/", "/vagrant/provisioning", type: "virtualbox"

      node4.vm.provision 'ansible_local' do |ansible|
        ansible.install_mode = 'default'
        ansible.verbose = true
        ansible.install = true
        ansible.playbook = 'provisioning/site.yml'
      end
    end

  config.vm.define "node2" do |node2|
    node2.vm.box = "centos/7"
    node2.vm.hostname = "node2.local"
    node2.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = "1"
    end
    node2.vm.network "private_network", ip: "172.28.128.4"
    node2.vm.synced_folder "node2/", "/vagrant", type: "virtualbox"
    node2.vm.synced_folder "provisioning/", "/vagrant/provisioning", type: "virtualbox"

    node2.vm.provision 'ansible_local' do |ansible|
      ansible.install_mode = 'default'
      ansible.verbose = true
      ansible.install = true
      ansible.playbook = 'provisioning/site.yml'
    end
 end

  config.vm.define "node3" do |node3|
    node3.vm.box = "centos/7"
    node3.vm.hostname = "node3.local"
    node3.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = "1"
    end
    node3.vm.network "private_network", ip: "172.28.128.5"
    node3.vm.synced_folder "node3/", "/vagrant", type: "virtualbox"
    node3.vm.synced_folder "provisioning/", "/vagrant/provisioning", type: "virtualbox"

    node3.vm.provision 'ansible_local' do |ansible|
      ansible.install_mode = 'default'
      ansible.verbose = true
      ansible.install = true
      ansible.playbook = 'provisioning/site.yml'
    end
  end


end

