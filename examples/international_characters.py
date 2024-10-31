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
  # コンニチハ、 セカイ！
  device.send(0xBA, 0xDD, 0xC6, 0xC1, 0xCA, 0xA4, 0xBE, 0xB6, 0xB2, ord("!"))
  device.send_text("\r\n")
  device.select_character_code_table(CodeTable.CYRILLIC.value)
  # Привіт, світ!
  device.send(0x8F, 0xE0, 0xA8, 0xA2, 0xA5, 0xE2, ord(","), ord(" "), 0xAC, 0xA8, 0xE0, ord("!"))
  input("Press Enter...")
  device.clear_screen()
  device.select_character_code_table(CodeTable.HEBREW.value)
  # שלום, עולם!
  # LD220 does not handle right to left languages
  device.xy(10, 1)
  device.send(ord("!"), 0xED, 0xEC, 0xEF, 0xF2, ord(" "), ord(","), 0xED, 0xEF, 0xEC, 0xF9)
  device.select_character_code_table(CodeTable.GREEK.value)
  # Γεια σου κόσμο!
  device.send(0xC3, 0xE5, 0xE9, 0xE1, ord(" "), 0xF3, 0xEF, 0xED, ord(" "), 0xEA, 0xFC, 0xF3, 0xEC, 0xEF, ord("!"))
  device.disconnect()

if __name__ == "__main__":
  main()