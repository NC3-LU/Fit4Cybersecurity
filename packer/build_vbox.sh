#!/usr/bin/env bash

GOT_PACKER=$(which packer > /dev/null 2>&1; echo $?)
if [[ "$GOT_PACKER" == "0" ]]; then
  echo "Packer detected, version: $(packer -v)"
  PACKER_RUN=$(which packer)
else
  echo "No packer binary detected, please make sure you installed it from: https://www.packer.io/downloads.html"
  exit 1
fi

echo "Retrieving information about latest MONARC release…"
export VERSION=$(curl --silent -H 'Content-Type: application/json' https://api.github.com/repos/CASES-LU/Fit4Cybersecurity/releases/latest | jq  -r '.tag_name')
# Latest commit hash of MONARC
export LATEST_COMMIT=$(curl --silent -H 'Content-Type: application/json' -s https://api.github.com/repos/CASES-LU/Fit4Cybersecurity/commits | jq -e -r '.[0] | .sha')

# SHAsums to be computed
SHA_SUMS="1 256 384 512"

# checkInstaller () {
# }

# Fetch and check installer
if [[ -f "scripts/INSTALL.sh" ]]; then
  echo "Checking checksums"
  #checkInstaller
else
  /usr/bin/wget -q -O scripts/INSTALL.sh https://raw.githubusercontent.com/CASES-LU/Fit4Cybersecurity/master/INSTALL/INSTALL.sh
  #checkInstaller
fi


# Fetching latest LICENSE
[[ ! -f /tmp/LICENSE ]] && wget -q -O /tmp/LICENSE https://raw.githubusercontent.com/CASES-LU/Fit4Cybersecurity/master/COPYING

echo "Generating a virtual machine for Fit4Cybersecurity $VERSION (commit id: $LATEST_COMMIT)…"
rm -Rf output/ 2> /dev/null
packer build ubuntu-20.04.json


# Cleaning…
# rm -Rf scripts/INSTALL.sh 2> /dev/null
