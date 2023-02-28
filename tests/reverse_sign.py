import sys
sys.path.append(sys.path[0].split('tests')[0])

from commands.reverse_sign import ReverseSign


c = ReverseSign('5')
print(c.execute()) # -5

c = ReverseSign('-5')
print(c.execute()) # 5
