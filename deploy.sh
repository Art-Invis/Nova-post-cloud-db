#!/usr/bin/env bash
set -e

cd /home/ubuntu/nova-post-cloud-db

# оновлюємо код з GitHub
git fetch --all
git reset --hard origin/main

# активуємо virtualenv
source venv/bin/activate
pip install --upgrade pip
pip install -r app/tracking_project/requirements.txt
deactivate

# перезапускаємо сервіс
sudo systemctl daemon-reload
sudo systemctl restart tracking.service

echo "Deploy finished: $(date)"
