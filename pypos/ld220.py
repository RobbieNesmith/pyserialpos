# Based on gist by
# JP Mens, January 2015
# for HP LD220 POS
# https://gist.github.com/jpmens/f0681100ffcec1c5275d

import serial
from .constants.characters import *

class LD220:
  def __init__(self, device, baud):
    self.ser = serial.Serial(device, baud, timeout=5)

  def send(self, *data):
    self.ser.write(bytes(data))

  def send_text(self, text):
    self.send(*(text.encode("UTF-8")))

  def cursor_left(self):
    self.send(BS)
  
  def cursor_right(self):
    self.send(HT)
  
  def cursor_up(self):
    self.send(US, LF)
  
  def cursor_down(self):
    self.send(LF)

  def cursor_end(self):
    self.send(US, CR)
  
  def cursor_start(self):
    self.send(CR)

  def cursor_home(self):
    self.send(HOM)
  
  def cursor_bottom(self):
    self.send(US, 0x42)

  def xy(self, x, y):
    self.send(US, 0x24, x, y)

  def show_cursor(self, should_show):
    self.send(US, 0x43, should_show)

  def clear_screen(self):
    self.send(CLR)

  def clear_line(self):
    self.send(CAN)

  def set_brightness(self, brightness):
    self.send(US, 0x58, brightness)

  def blink(self, duration=0):
    self.send(US, 0x45, duration)

  def reset(self):
    self.send(ESC, 0x40)

  def select_character_code_table(self, table_id):
    self.send(ESC, 0x74, table_id)

  def select_international_charset(self, charset):
    self.send(ESC, 0x52, charset.value)

  def invert_characters(self, should_invert):
    self.send(US, 0x72, should_invert)

  def set_overflow_mode(self, mode):
    self.send(US, mode.value)

  def display_period(self, character):
    self.send(US, 0x2E, character)
  
  def display_comma(self, character):
    self.send(US, 0x2C, character)
  
  def display_semicolon(self, character):
    self.send(US, 0x3B, character)

  def display_annunciator(self, column, should_show):
    self.send(US, 0x23, should_show, column)

  def define_characters(self, start_char, end_char, patterns):
    self.send(ESC, 0x26, 0x01, start_char, end_char, *patterns)

  def cancel_characters(self, character):
    self.send(ESC, 0x3F, character)

  def use_defined_characters(self, should_use):
    self.send(ESC, 0x25, should_use)

  def set_window_range(self, window_count, should_use, x1, y1, x2, y2):
    self.send(ESC, 0x57, window_count, should_use, x1, y1, x2, y2)

  def set_peripheral_device(self, peripheral_type):
    self.send(ESC, 0x3D, peripheral_type.value)

  def set_macro_start_end(self):
    self.send(US, 0x3A)

  def execute_and_quit_macro(self, display_interval, macro_interval):
    self.send(US, 0x5E, display_interval, macro_interval)

  def self_test(self):
    self.send(US, 0x40)

  def show_time(self, hour, minute):
    self.send(0x1F, 0x54, hour, minute)

  def show_time_counter(self):
    self.send(US, 0x55)

  def disconnect(self):
    self.ser.close()