# OnionHost

### What Is OnionHost 

- `OnionHost`  allows you to easily host your website on the dark web using your Termux or Linux system. With OnionHost, your website is self-hosted, meaning it runs directly from your local server, giving you full control and privacy over your content. This tool empowers you to set up a hidden service on the Tor network, providing a secure and anonymous platform for your website without the need for third-party hosting services.

<img src="https://i.ibb.co/7XjbzT4/IMG-20240915-200320-556.jpg">

### Complete Setup For Termux 
First, make sure all your Termux packages are up to date. Open your Termux terminal and run:

```json
pkg update && pkg upgrade

```

- Install Python On termux 
```json
pkg install python -y

```
```json
pkg install python-pip -y

```

Install Tor On Termux 

```json
pkg install tor -y

```
- After installing Tor, you need to configure it to create a hidden service. This is where the torrc file comes into play. 

Create the necessary directories:



```javascript
mkdir -p /data/data/com.termux/files/home/tor-hidden-service

```

- Configure the torrc file: Edit or create a torrc file with the following settings:

```json
nano ~/torrc

```

- Add the following lines to your torrc file:


```python
HiddenServiceDir /data/data/com.termux/files/home/tor-hidden-service/
HiddenServicePort 80 127.0.0.1:8080

```

Save the file and exit (`CTRL + X, then Y to save`)

## Now Its Time to Run This Tool On Termux

- Installation Command 
```javascript
git clone https://github.com/BlackHat-Abhi/OnionHost.git
cd OnionHost
pip install - r requirements.txt
python main.py 
```
- If you are Using Termux So Select 1 And  Password `abhi`


#  Complate Setup For Linux 

- Install Required Packages:Python: Install Python 3 if not already installed.


```css
sudo apt-get update
sudo apt-get install python3 python3-pip
```
- Install Tor On Your Linux System 


```cpp
sudo apt-get install tor
```
#  Configure Tor:
- Edit the Tor configuration file (/etc/tor/torrc).

```css
sudo nano /etc/tor/torrc
```

- Add the following lines at the end of the file to set up a hidden service:


```html
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:8080
```


- Save the file and exit (`CTRL + X, then Y to save`)

# Create Hiden Service Dir

- Create the hidden service directory and set permissions.

```javascript
sudo mkdir -p /var/lib/tor/hidden_service/
sudo chown -R debian-tor:debian-tor /var/lib/tor/hidden_service/
sudo chmod 700 /var/lib/tor/hidden_service/
```

```html
sudo systemctl restart tor
```

```html
sudo journalctl -xe | grep tor
```
# Now Its Time Run this Tool 

- Installation Command 

```javascript
git clone https://github.com/BlackHat-Abhi/OnionHost.git
cd OnionHost
pip3 install - r requirements.txt
python3 main.py 
```
- If you are Using Linux So Select 2 And password `abhi`

## Screenshots

<img src="https://i.ibb.co/mq6ZcgD/IMG-20240916-003959-450.jpg">
<img src="https://i.ibb.co/6BwV50S/Screenshot-2024-09-15-23-31-06-81-84d3000e3f4017145260f7618db1d683.jpg">
<img src="https://i.ibb.co/8MmPFZq/Screenshot-2024-09-15-23-36-36-87-84d3000e3f4017145260f7618db1d683.jpg">

 Telegram Channel : [Channel](https://telegram.me/BlackHat_HackerX)

## Jai Shree Ram Enjoy This Tool By BlackHat-Abhi 

## CONNECT WITH US :


[![Instagram](https://img.shields.io/badge/INSTALGRAM-FOLLOW-red?style=for-the-badge&logo=instagram)](https://instagram.com/blackhat_abhi)


[![Whatsapp](https://img.shields.io/badge/WHATSAPP-CHANNEL-red?style=for-the-badge&logo=whatsapp)](https://bitly.ws/38Tf6)


[![Telegram](https://img.shields.io/badge/TELEGRAM-GROUP-red?style=for-the-badge&logo=telegram)](https://t.me/HackerX_Termux_Help)


[![Telegram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/BlackEagle_Sec)


[![Whatsapp](https://img.shields.io/badge/WHATSAPP-JOINGROUP-red?style=for-the-badge&logo=whatsapp)](https://bit.ly/3LiuRV9)

  



