#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Install Nginx if not installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Remove existing symbolic link and create new one
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
NGINX_CONFIG="/etc/nginx/sites-available/default"

sudo sed -i '35i\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' "$NGINX_CONFIG"

# Restart Nginx
sudo service nginx restart
