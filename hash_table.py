# Dictionary is python specific implementation of hash table
# Mode operation SUM / 100 (size) -> remainder

class HashTable:
  def __init__(self):
    self.MAX = 10
    self.arr = [[] for i in range(self.MAX)]

  def get_hash(self, key):
    hash = 0
    for char in key:
      hash += ord(char)
    return hash % self.MAX
  
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

  def __delitem__(self, key):
    h = self.get_hash(key)
    for idx, element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][idx]

t = HashTable()

t['march 6'] = 12
t['march 9'] = 30
t['march 17'] = 66
t['march 9'] = 99
# del t['march 9']


print(t.get_hash('march 6'))
print(t.get_hash('march 17'))

print(t['march 17'])
print(t.arr)