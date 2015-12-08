# CS419 Senior Project

## Overview

NCurses Database Viewer and Editor

## Prerequisites (OSX)

* [Python](https://www.python.org/downloads/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

### Virtual Machine PostgreSQL Credentials

* username = vagrant
* password = vagrant
* database = cs419

## Start Vagrant to build virtual machine sandbox

```bash
$ vagrant up
```

## Log into virtual machine

```bash
$ vagrant ssh
```

### Seeding the database (for demo purposes)
```bash
$ cd cs419-project
$ python demo_seed.py
```

### Start program
```bash
$ cd cs419-project
$ python main.py
```

## Authors

* [Allison Barnett](barnetal@oregonstate.edu)
* [Lynda Phan](phanly@onid.oregonstate.edu)
* [Becky Solomon](solomreb@oregonstate.edu)

