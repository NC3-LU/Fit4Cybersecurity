#! /usr/bin/env bash

echo "--- Post configurations… ---"
sudo bash -c "cat << EOF > /etc/issue
Welcome to the $TOOL_NAME Virtual Machine!

The Web interface is available at: http://\4:$SERVICE_PORT

If you find any bugs:
https://github.com/CASES-LU/Fit4Cybersecurity/issues


EOF"
