# Internet Radio Player

Internet Radio Player with an web interface.

[![Build Status](https://travis-ci.org/jakubthedeveloper/PythonInternetRadio.svg?branch=master)](https://travis-ci.org/jakubthedeveloper/PythonInternetRadio)

## Dependencies

mpd and mpc - music player daemon

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
               [--bluetooth-speaker-device BLUETOOTH_SPEAKER_DEVICE]
               [--show-volume-controls {yes,no}]

Internet radio with Web interface for Linux or Raspbian.

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           Web ui host
  --port PORT           Web ui port
  --bluetooth-speaker-device BLUETOOTH_SPEAKER_DEVICE
                        Bluetooth device identifier (taken from bluetoothctl)
  --show-volume-controls {yes,no}
                        Show volume controls, choices: yes / no, default: yes
```

## Control Panel
<kbd>
  <img src="https://i1.wp.com/programisty-dzien-powszedni.pl/wp-content/uploads/2019/11/RadioControl.png" />
</kbd>

With default values, the control panel works on address:

`http://127.0.0.1:1234/`

If you have specified custom host and/or port, create the url by schema:

`http://<host>:<port>/`

## Station list

You can manage the station list in the stations.yml file.

## Run tests

`sh test.sh`

## Installation on Raspberry Pi with Raspbian OS.

```
sudo apt-get update
sudo apt-get install git python3 mpd mpc python-pip
sudo pip3 install -U Flask oyaml
git clone https://github.com/jakubthedeveloper/PythonInternetRadio.git radio
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

# Bluetooth speaker

In you want to connect a Bluetooth speaker to Raspberry Pi you have to install Bluez-alsa. I managed to do it using the instruction on the page [how-to-stream-sound-to-a-bluetooth-device-from-a-raspberry-pi-zero](https://raspberrypi.stackexchange.com/questions/90267/how-to-stream-sound-to-a-bluetooth-device-from-a-raspberry-pi-zero)

Here is my audio output config in /etc/mpd.conf that works with Creative Muvo 2c bluetooth speaker:

```
audio_output {
       type            "alsa"
       name            "BluetoothSpeaker"
       device          "bluealsa:DEV=XX:XX:XX:XX:XX:XX,PROFILE=a2dp" # replace XX:XX:XX:XX:XX:XX with bluetooth device id
}
```

# Example ecosystem

![Example ecosystem for Raspberry Radio](https://i0.wp.com/programisty-dzien-powszedni.pl/wp-content/uploads/2019/11/radio-1.png)


# Blog

[PL] Artykuł na blogu: [Python – odtwarzacz radia internetowego – Linux i Raspberry Pi](https://programisty-dzien-powszedni.pl/python-odtwarzacz-radia-internetowego-linux-i-raspberry-pi/)
