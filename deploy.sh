cd src/
rm -r __pycache__/
git fetch
git reset --hard origin/main

sudo apt update
sudo apt upgrade -y
sudo apt install gunicorn python3-flask -y
sudo apt autoremove -y
sudo apt clean

sudo systemctl restart website
neofetch
