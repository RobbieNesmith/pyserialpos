from pyserialpos import LD220

def main():
  print("Enter serial port of your LD220")
  print("On Windows, this will look something like \"COM8\"")
  print("On Linux this will look something like \"/dev/ttyUSB0\"")
  port = input("? ")

  device = LD220(port, 9600)

  device.reset()
  device.send_text("Top Left")
  device.xy(9,2)
  device.send_text("Bottom Right")

  # Back on the top line since the last text reached the end of the screen
  device.cursor_end()
  for _ in range(4):
    device.cursor_left()
  device.send_text("Test!")
  device.cursor_right()
  device.send_text("Hi!")

  device.disconnect()

if __name__ == "__main__":
  main()