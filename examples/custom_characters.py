from pyserialpos import LD220

def main():
  print("Enter serial port of your LD220")
  print("On Windows, this will look something like \"COM8\"")
  print("On Linux this will look something like \"/dev/ttyUSB0\"")
  port = input("? ")

  device = LD220(port, 9600)

  #       # 01
  # ##### # 02
  # ##### # 04
  # ##### # 08
  # ##### # 10
  # ##### # 20
  #       # 40

  square = [0x3E, 0x3E, 0x3E, 0x3E, 0x3E]

  #       # 01
  #  ###  # 02
  # ##### # 04
  # ##### # 08
  # ##### # 10
  #  ###  # 20
  #       # 40

  circle = [0x1C, 0x3E, 0x3E, 0x3E, 0x1C]

  #   #   # 01
  #   #   # 02
  #  ###  # 04
  #  ###  # 08
  # ##### # 10
  # ##### # 20
  #       # 40

  triangle = [0x30, 0x3C, 0x3F, 0x3C, 0x30]

  #       # 01
  #  # #  # 02
  #  # #  # 04
  #       # 08
  # #   # # 10
  #  ###  # 20
  #       # 40

  smiley = [0x10, 0x26, 0x20, 0x26, 0x10]

  device.reset()
  device.define_characters(ord("A"), ord("D"), [*square, *circle, *triangle, *smiley])
  device.send_text("Square:     Circle:\r\n")
  device.send_text("Triangle:   Smiley: ")
  device.use_defined_characters(True)

  device.xy(8,1)
  device.send_text("A")
  device.xy(20,1)
  device.send_text("B")
  device.xy(10,2)
  device.send_text("C")
  device.xy(20,2)
  device.send_text("D")
  device.disconnect()

if __name__ == "__main__":
  main()