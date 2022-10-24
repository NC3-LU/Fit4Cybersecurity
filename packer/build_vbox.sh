#!/usr/bin/env bash

GOT_PACKER=$(which packer > /dev/null 2>&1; echo $?)
if [[ "$GOT_PACKER" == "0" ]]; then
  echo "Packer detected, version: $(packer -v)"
  PACKER_RUN=$(which packer)
else
  echo "No packer binary detected, please make sure you installed it from: https://www.packer.io/downloads.html"
  exit 1
fi

echo "Retrieving information about latest Fit4Cybersecurity release…"
export VERSION=$(curl --silent -H 'Content-Type: application/json' https://api.github.com/repos/NC3-LU/Fit4Cybersecurity/releases/latest | jq  -r '.tag_name')
# Latest commit hash of MONARC
export LATEST_COMMIT=$(curl --silent -H 'Content-Type: application/json' -s https://api.github.com/repos/NC3-LU/Fit4Cybersecurity/commits | jq -e -r '.[0] | .sha')

# SHAsums to be computed
SHA_SUMS="1 256 512"

checkInstaller () {
  for sum in $(echo ${SHA_SUMS}); do
    /usr/bin/wget -q -O scripts/INSTALL.sh.sha${sum} https://raw.githubusercontent.com/NC3-LU/Fit4Cybersecurity/master/INSTALL/INSTALL.sh.sha${sum}
    INSTsum=$(shasum -a ${sum} scripts/INSTALL.sh | cut -f1 -d\ )
    chsum=$(cat scripts/INSTALL.sh.sha${sum} | cut -f1 -d\ )

    if [[ "$chsum" == "$INSTsum" ]]; then
      echo "sha${sum} matches"
    else
      echo "sha${sum}: ${chsum} does not match the installer sum of: ${INSTsum}"
      echo "Deleting installer, please run again."
      rm scripts/INSTALL.sh
      exit 1
    fi
  done
}

# Fetch and check installer
if [[ -f "scripts/INSTALL.sh" ]]; then
  echo "Checking checksums"
  checkInstaller
else
  /usr/bin/wget -q -O scripts/INSTALL.sh https://raw.githubusercontent.com/NC3-LU/Fit4Cybersecurity/master/INSTALL/INSTALL.sh
  checkInstaller
fi


# Fetching latest LICENSE
[[ ! -f /tmp/LICENSE ]] && wget -q -O /tmp/LICENSE https://raw.githubusercontent.com/NC3-LU/Fit4Cybersecurity/master/COPYING

echo "Generating a virtual machine for Fit4Cybersecurity $VERSION (commit id: $LATEST_COMMIT)…"
rm -Rf output/ 2> /dev/null
packer build ubuntu-20.04.json


# Cleaning…
rm -Rf scripts/INSTALL.sh scripts/INSTALL.sh.sha1 scripts/INSTALL.sh.sha256 scripts/INSTALL.sh.sha512 2> /dev/null
