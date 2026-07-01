# rgt_desk
Absolutely life-changing dashboard experience unlike anything you have ever seen before. Truly eye-opening. Let's grind!

# Dependencies
Make sure you have a recent version of nodejs installed. I would recommend using nvm like this:
```bash
nvm install 24
```

Also install nginx:
```bash
sudo apt update && sudo apt install nginx
sudo systemctl disable nginx.service --now # We will use our own service for this
```

# Install

1. Clone this repo:
```bash
git clone https://github.com/alexmnr/rgt_desk.git
```

2. Run the install script:
```bash
cd rgt_desk && ./install.sh
