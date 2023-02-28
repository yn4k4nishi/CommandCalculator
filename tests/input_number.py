import sys
sys.path.append(sys.path[0].split('tests')[0])

from commands.input_number import InputNumber


c = InputNumber('3', '9')
print(c.execute()) # 39

c = InputNumber('3.14', '1')
print(c.execute()) # 3.141
