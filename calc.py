class calc:
  def __init__(self):
    pass

  def sum(self, x1, x2):
    return x1 + x2

  def multiply(self, x1, x2):
    return x1 * x2

  def subtract(self, x1, x2):
    return x1 - x2

  def divide(self, x1, x2):
    if x2 != 0:
      return x1 / x2
    else:
      return "Error"
