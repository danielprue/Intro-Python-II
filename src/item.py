class Item:
  name=''
  description=''

  def __init__(self, name, description):
    self.name=name
    self.description=description

  def on_take(self):
    print(f'You have picked up {self.name}\n')

  def on_drop(self):
    print(f'You have dropped {self.name}\n')
  