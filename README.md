## Profiles REST API

Django REST API providing basic functionality for managing user profiles.

- Create, Update and Delete  Custom User Profiles
- Token Based Authentication
- Create, Update and Delete Feed status
- APIView and ViewSets 

## Requirements 

* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Getting started

First install VirtualBox and Vagrant. 

Clone this repository

```bash
git clone https://github.com/Prithvi45/profiles-rest-api.git
```
## Create and provision the VMs

```bash
cd profiles-reat-api
vagrant up
```
**Note:** the above can take several minutes, especially the first time it runs (needs to download the Ubuntu Vagrant Box and install the required packages on each VM). This will take long only the first time, starting and stoping the VMs hereafter will be significantly faster. 

***Connect to ubuntu virtual machine via ssh

```bash
vagrant ssh
```
