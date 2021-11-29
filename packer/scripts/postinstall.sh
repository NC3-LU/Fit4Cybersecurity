#! /usr/bin/env bash


echo "--- Configuring systemd service… ---"
sudo bash -c "cat << EOF > /etc/systemd/system/fit4cybersecurity.service
[Unit]
Description=$TOOL_NAME service
After=network.target

[Service]
User=ubuntu
Environment=LANG=en_US.UTF-8
Environment=LC_ALL=en_US.UTF-8
WorkingDirectory=$PROJECT_PATH
ExecStart=/home/ubuntu/.local/bin/poetry run python manage.py runserver $SERVICE_HOST:$SERVICE_PORT
Restart=always

[Install]
WantedBy=multi-user.target
EOF"

sudo systemctl daemon-reload > /dev/null
sleep 1
sudo systemctl enable fit4cybersecurity.service > /dev/null
sleep 3
sudo systemctl restart fit4cybersecurity.service > /dev/null


echo "--- Configuring hostname to $HOSTNAME… ---"
sudo hostnamectl set-hostname $HOSTNAME


echo "--- Configuring /etc/issue… ---"
sudo bash -c "cat << EOF > /etc/issue
Welcome to the $TOOL_NAME Virtual Machine!

The Web interface is available at: http://\4:$SERVICE_PORT

If you find any bugs:
https://github.com/CASES-LU/Fit4Cybersecurity/issues


EOF"
