class Breakfast:
  def __init__(self):
    self.reset()

  def reset(self):
    self.coffee = 0
    self.cappuccino = 0
    self.brioche = 0
    self.mignon = 0

  def toMessage(self):
    msg = 'And the winner are...'
    msg = msg + "\n  - Caffe: " + str(self.coffee)
    msg = msg + "\n  - Cappuccini: " + str(self.cappuccino)
    msg = msg + "\n  - Brioche: " + str(self.brioche)
    msg = msg + "\n  - Mignon: " + str(self.mignon)
    return msg
