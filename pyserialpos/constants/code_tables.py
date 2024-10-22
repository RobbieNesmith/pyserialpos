from enum import Enum

class CodeTable(Enum):
  LATIN_US = 0x00 # DOS 437 but with € as 0x80
  CANADA_FRENCH = 0x01
  
  CYRILLIC = 0x03


  LATIN_II = 0x06 # DOS 852
  HEBREW = 0x07 # Windows 1255

  GREEK = 0x09 # Windows 1253-ish
  JAPANESE_KATAKANA = 0x0A # CP 942 with other symbols instead of double-byte characters

  # These tables result in garbled characters
  RESERVED_1 = 0x0C
  RESERVED_2 = 0x0D
  RESERVED_3 = 0x0E
  RESERVED_4 = 0x0F