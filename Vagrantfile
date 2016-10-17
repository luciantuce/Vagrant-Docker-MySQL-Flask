Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 80, host:1234
  config.vm.network "public_network"
  config.vm.define "mysql-docker"
  config.vm.provision :shell, inline: "apt-get install python -y"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end
