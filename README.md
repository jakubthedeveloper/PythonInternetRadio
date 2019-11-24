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

PyYAML - YAML parser and emitter for Python.

```
pip install pyyaml
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

`http://127.0.0.1:1234/`

## Station list

You can manage the station list in the stations.yml file.
