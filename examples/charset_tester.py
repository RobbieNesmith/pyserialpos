from pyserialpos import LD220
import time

# Commands
#
# n/p: next/previous row of characters
# nc/pc: next/previous international character code table
# nt/pt: next/previous international font set table
# cust: show custom defined characters
# q: quit

def show_chars(device, offset):
  device.clear_screen()
  device.send_text(f"{offset:02x}:")
  device.send(*range(offset, offset + 0x10))
  device.send_text("\r\n")
  device.send_text(f"{offset + 0x10:02x}:")
  device.send(*range(offset + 0x10, offset + 0x20))

def character_test(device):
  offset = 0x20
  table = 0
  charset = 0
  custom = False
  cmd = ""
  show_chars(device, offset)
  while cmd != "q":
    cmd = input(">")
    if cmd == "n" and offset < 0xE0:
      offset += 0x10
    if cmd == "p" and offset > 0x20:
      offset -= 0x10
    if cmd == "nt":
      table += 1
      device.select_character_code_table(table)
      device.clear_screen()
      device.send_text(f"Selected table: {table}")
      time.sleep(1)
    if cmd == "pt":
      table -= 1
      device.select_character_code_table(table)
      device.clear_screen()
      device.send_text(f"Selected table: {table}")
      time.sleep(1)
    if cmd == "nc":
      charset += 1
      device.select_international_charset(charset)
      device.clear_screen()
      device.send_text(f"Selected charset: {charset}")
      time.sleep(1)
    if cmd == "pc":
      charset -= 1
      device.select_international_charset(charset)
      device.clear_screen()
      device.send_text(f"Selected charset: {charset}")
      time.sleep(1)
    if cmd == "cust":
      custom = not custom
      device.clear_screen()
      if custom:
        device.send_text("Using ")
      else:
        device.send_text("Not using ")
      device.send_text("custom chars.")
      device.use_defined_characters(custom)
      time.sleep(1)
    show_chars(device, offset)

def main():
  print("Enter serial port of your LD220")
  print("On Windows, this will look something like \"COM8\"")
  print("On Linux this will look something like \"/dev/ttyUSB0\"")
  port = input("? ")

  device = LD220(port, 9600)
  character_test(device)
  device.reset()
  device.disconnect()


if __name__ == "__main__":
  main()