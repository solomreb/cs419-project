Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python-software-properties
    sudo apt-get update -y
    # sudo apt-get upgrade -y

    sudo apt-get install -y postgresql postgresql-contrib postgresql-client libpq-dev
    sudo sed -i "s/#listen_address.*/listen_addresses '*'/" /etc/postgresql/9.3/main/postgresql.conf
    sudo cp /home/vagrant/cs419-project/vagrant_files/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf

    sudo service postgresql restart

    # createuser -U postgres -s vagrant
    sudo -u postgres psql -c "CREATE ROLE vagrant SUPERUSER LOGIN PASSWORD 'vagrant'"
    sudo su postgres -c "createdb -E UTF8 -T template0 --locale=en_US.utf8 -O vagrant cs419"

    sudo apt-get install -y python-pip python-psycopg2
    sudo pip install peewee
  SHELL

  config.vm.synced_folder ".", "/home/vagrant/cs419-project", id: "vagrant",
    owner: "vagrant",
    group: "admin",
    mount_options: ["dmode=775,fmode=664"]
end


