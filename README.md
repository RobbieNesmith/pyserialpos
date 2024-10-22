![pyserialpos running on an HP LD220 VFD pole display](https://github.com/RobbieNesmith/pyserialpos/blob/main/screenshot.jpg)

pyserialpos is a package for interacting with serial POS pole displays. It is in very early development so there may be significant usage changes.

## How to use
1. Find the serial port your display is using
   - On Windows, this will look something like `COM8`
   - On Linux, this will look something like `/dev/ttyUSB0`
2. Import your display model and send some commands
3. `disconnect()` when you are done to close the serial port

## Example
```python
from pyserialpos import LD220

d = LD220("COM8")
d.reset()
d.send_text("Hello, World!")
d.disconnect()
```

## Supported Devices
Currently this project only supports the HP LD220 in Epson command mode. Feel free to add support for other devices.

## References
- https://hugepdf.com/download/vfd-ld220-user-manualv23_pdf
- https://github.com/bklang/ld220
- https://gist.github.com/jpmens/f0681100ffcec1c5275d
- https://github.com/playfultechnology/arduino-VFD-RS232