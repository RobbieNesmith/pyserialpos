from pyserialpos import LD220
from pyserialpos.constants import OverflowMode

def main():
  print("Enter serial port of your LD220")
  print("On Windows, this will look something like \"COM8\"")
  print("On Linux this will look something like \"/dev/ttyUSB0\"")
  port = input("? ")

  device = LD220(port, 9600)

  device.reset()
  device.set_macro_start_end()
  device.send_text("Don't mind me, just scrolling on by.    ")
  device.set_macro_start_end()
  device.set_overflow_mode(OverflowMode.HORIZONTAL_SCROLL)
  device.execute_and_quit_macro(5, 5)
  device.disconnect()

if __name__ == "__main__":
  main()