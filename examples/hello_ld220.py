from pyserialpos import LD220

def main():
  print("Enter serial port of your LD220")
  print("On Windows, this will look something like \"COM8\"")
  print("On Linux this will look something like \"/dev/ttyUSB0\"")
  port = input("? ")

  device = LD220(port, 9600)

  device.reset()
  device.send_text("Hello, World!")

  device.disconnect()

if __name__ == "__main__":
  main()