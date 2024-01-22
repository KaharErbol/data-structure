class KeyDoesNotExistError(Exception):
  def __init__(self, key):
    self.key = key
    self.message= f"The key '{key}' does not exist."

class HashMap:
  def __init__(self) -> None:
    self.MAX = 10
    self.arr = [[] for i in range(self.MAX)]
  
  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    return h % self.MAX

  def __setitem__(self, key, val):
    h = self.get_hash(key)
    found = False

    for idx, element in enumerate(self.arr[h]):
      if len(element) == 2 and element[0] == key:
        self.arr[h][idx] = (key, val)
        found = True
        break

    if not found:
      self.arr[h].append((key, val))  

  def __getitem__(self, key):
    h = self.get_hash(key)
    for element in self.arr[h]:
      if element[0] == key:
        return element[1]

  def if_exist(self, h, key):
    if self.arr[h] == []:
      raise KeyDoesNotExistError(key)
    
  def __delitem__(self, key):
    h = self.get_hash(key)

    try:
      self.if_exist(h, key)
    except KeyDoesNotExistError as e:
      print(f"Error: {e}")
    
    for idx, element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][idx]

t = HashMap()

t["march 6"] = 99
t['march 17'] = 12

del t['march']