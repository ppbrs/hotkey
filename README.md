# hotkey


# Known limitations

## root access

The application requires root access to `keyboard` library.
Install the application with
```
sudo python3 -m pip install -e .
```
and run it with
```
sudo hotkey
```
Consider using https://pypi.org/project/pynput/ or reading from /dev/input/input* directly.
