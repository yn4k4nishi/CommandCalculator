import sys
sys.path.append(sys.path[0].split('tests')[0])

from commands.input_dot import InputDot


c = InputDot('3')
print(c.execute()) # 3.

c = InputDot('3.14')
print(c.execute()) # 3.14
