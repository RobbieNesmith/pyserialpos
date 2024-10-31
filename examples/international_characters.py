from pyserialpos import LD220
from pyserialpos.constants.code_tables import CodeTable

def main():
  print("Enter serial port of your LD220")
  print("On Windows, this will look something like \"COM8\"")
  print("On Linux this will look something like \"/dev/ttyUSB0\"")
  port = input("? ")

  device = LD220(port, 9600)
  device.reset()
  device.select_character_code_table(CodeTable.JAPANESE_KATAKANA.value)
  device.send(0xBA, 0xDD, 0xC6, 0xC1, 0xCA, 0xA4, ord(" "), 0xBE, 0xB6, 0xB2, ord("!"))
  device.disconnect()

if __name__ == "__main__":
  main()