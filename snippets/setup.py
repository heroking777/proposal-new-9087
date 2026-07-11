#!/bin/bash

# Update package list and install necessary packages
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv nginx git

# Create a directory for the project
mkdir /opt/sponsor_match_service
cd /opt/sponsor_match_service

# Clone the repository (replace with actual repo URL)
git clone https://github.com/yourusername/sponsor-match-service.git .
git checkout main  # or the appropriate branch

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure Nginx
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /opt/sponsor_match_service/deploy/nginx.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Set up systemd service for the application
sudo cp deploy/sponsor-match-service.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable sponsor-match-service
sudo systemctl start sponsor-match-service

# Clean up
deactivate

echo "Setup complete. The service should now be running."