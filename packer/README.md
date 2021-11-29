# Build Automated Machine Images based on Fit4Cybersecurity

Build a virtual machine for Fit4Cybersecurity based on Ubuntu 20.04 server
(for VirtualBox).


## Requirements

* [VirtualBox](https://www.virtualbox.org)
* [Packer](https://www.packer.io) from the Packer website
* [jq](https://stedolan.github.io/jq/)


## Usage

You can customize the image thanks to various variables in the file
``ubuntu-20.04.json`` (in the _variables_ section).

Launch the generation with the VirtualBox builder:

    $ ./build_vbox.sh
