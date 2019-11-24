# Internet Radio Player

Internet Radio Player with an web interface.

## Dependencies

mpc and mpc - music player daemon

```
sudo apt-get update
sudo apt-get install mpd mpc
```

flask - lightweight web application framework

```
sudo apt-get install python-pip
pip install -U Flask
```

oyaml - YAML parser which preserves dict ordering

```
pip install oyaml
```

## Usage:

```
python3 main.py [-h] [--host HOST] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Web ui host, default: 0.0.0.0
  --port PORT  Web ui port, default: 1234
```

## Control Panel

With default values, the control panel works on address:

`http://127.0.0.1:1234/`

If you have specified custom host and/or port, create the url by schema:

`http://<host>:<port>/`

## Station list

You can manage the station list in the stations.yml file.

## Installation on Raspberry Pi with Raspbian OS.

```
sudo apt-get update
sudo apt-get install git python3 mpd mpc python-pip
sudo pip3 install -U Flask oyaml
git clone git@github.com:jakubthedeveloper/PythonInternetRadio.git radio
```

Create startup script, for example in path /home/pi/radio-start.sh, with contents:

```
cd /home/pi/radio
python3 main.py
```

You can set custom host and port in the command above.

Test the web ui in your computer/phone/tablet browser, in my network the Raspberry Pi has the address: 192.168.123.7, so I open the following url in my browser:

```
http://192.168.123.7:1234/
```

Connect headphones or speakers to the Raspberry Pi and click play in Web UI.

## Cron

Add startup script to cron:

```

crontab -e
```

and enter the following line:

```
@reboot sh /home/pi/radio-start.sh
```

Reboot Rasperry Pi to check if the cron entry works:

```
sudo reboot
```
