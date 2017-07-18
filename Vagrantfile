BOX="centos/7"

HDP_AMBARI_REPO="http://public-repo-1.hortonworks.com/ambari/centos7/2.x/updates/2.5.1.0/ambari.repo"

nodes = [
    {:name => "node1", :cpu => 1, :mem => 4096, :ip => "172.28.128.3"},
    {:name => "node2", :cpu => 1, :mem => 2048, :ip => "172.28.128.4"},
    {:name => "node3", :cpu => 1, :mem => 2048, :ip => "172.28.128.5"},
    {:name => "node4", :cpu => 1, :mem => 2048, :ip => "172.28.128.6"}
]

VAGRANTFILE_API_VERSION = "2"

PLAYBOOK_PATH='provisioning/'
PLAYBOOK_NAME='hdp_centos7_playbook.yml'

HOST_TLD = "bigdata"
AMBARI_HOST_NAME = "node1.%s" % HOST_TLD

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = BOX

  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end
  
  nodes.each do |opts|
    config.vm.define opts[:name] do |config|
        config.vm.hostname = "%s.%s" % [opts[:name].to_s, HOST_TLD]
        config.vm.network :private_network, ip: opts[:ip]
        config.vm.provider :virtualbox do |vb|
            vb.customize ["modifyvm", :id, "--cpus", opts[:cpu] ] if opts[:cpu]
            vb.customize ["modifyvm", :id, "--memory", opts[:mem] || 2048 ]
        end

        config.vm.synced_folder "./", "/vagrant", type: "virtualbox"

        config.vm.provision :hosts do |provisioner|
            provisioner.autoconfigure = false
            provisioner.add_localhost_hostnames = false
            nodes.each do |n|
                provisioner.add_host n[:ip], [ "%s.%s" % [ n[:name].to_s, HOST_TLD ], n[:name].to_s ]
            end
        end

        config.vm.network "forwarded_port", guest: 8080, host: 8080, auto_correct: true if "%s.%s" % [ opts[:name].to_s, HOST_TLD ] == AMBARI_HOST_NAME

        config.vm.provision 'ansible_local' do |ansible|
           ansible.groups = {
               "ambari_host" => ['node1']
           }
           ansible.extra_vars = {
               "hdp_ambari_repo" => HDP_AMBARI_REPO,
               "ownhostname" => "%s.%s" % [opts[:name].to_s, HOST_TLD],
               "ambarihostname" => AMBARI_HOST_NAME 
           }
           ansible.install_mode = 'default'
           ansible.verbose = true
           ansible.install = true
           ansible.playbook = "%s/%s" % [PLAYBOOK_PATH, PLAYBOOK_NAME]
        end
    end
  end
end