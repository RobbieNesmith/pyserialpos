# Based on gist by
# JP Mens, January 2015
# for HP LD220 POS
# https://gist.github.com/jpmens/f0681100ffcec1c5275d

import serial
from . character_constants import *

class LD220:
  def __init__(self, device, baud):
    self.ser = serial.Serial(device, baud, timeout=5)

  def send(self, *data):
    self.ser.write(bytes(data))

  def send_text(self, text):
    self.send(*(text.encode("UTF-8")))

  def reset(self):
    self.send(ESC, 0x40)

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

  def clear_line(self):
    self.send(CAN)

  def clear_screen(self):
    self.send(CLR)

  def define_characters(self, start_char, end_char, patterns):
    self.send(ESC, 0x26, 0x01, start_char, end_char, *patterns)

  def use_defined_characters(self, should_use):
    self.send(ESC, 0x25, should_use)

  def blink(self, duration=0):
    self.send(US, 0x45, duration)

  def xy(self, x, y):
    self.send(US, 0x24, x, y)

  def show_time(self, hour, minute):
    self.send(0x1F, 0x54, hour, minute)

  def disconnect(self):
    self.ser.close()