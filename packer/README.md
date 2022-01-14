# Build Automated Machine Images based on Fit4Cybersecurity

Build a virtual machine for Fit4Cybersecurity based on Ubuntu 20.04 server
(for VirtualBox).


## Requirements

* [VirtualBox](https://www.virtualbox.org);
* [Packer](https://www.packer.io) from the Packer website;
* [jq](https://stedolan.github.io/jq/).


## Usage

You can customize the image thanks to various variables in the file
``ubuntu-20.04.json`` (see the _variables_ section).

Some variables you can configure:

- _site_name_ (default: _fit4cybersecurity_): name of the site/tool. Used to load custom configurations;
- _tool_name_ (default: _Fit4Cybersecurity_): name of the tool;
- _vm_description_ (default: _Fit4Cybersecurity_): description of the virtual machine;
- _service_host_ (default: _0.0.0._): host where the service is waiting for connections;
- _service_port_ (default: _5000_): port where the service is waiting for connections;
- _hostname_ (default: _fit4Cybersecurity_): hostname of the system.

Once the VM will be created you will still be able to change the configurations.

_site_name_ is the variable which will let you load the appropriate configurations.
It must be one of the modules in the the ``csskp``
module (_fit4cybersecurity_, _fit4ehealth_, etc.).

The _hostname_ variable will be used in the ``ALLOWED_HOSTS`` configuration variable of
the Django software. Pay attention that you internal DNS resolves it
(or your /etc/hosts).


Launch the generation with the VirtualBox builder:

    $ ./build_vbox.sh
