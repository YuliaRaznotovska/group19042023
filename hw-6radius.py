import math

from _decimal import *

user_radius = int(input('Enter the radius >>> '))

PI = math.pi

multiplication_list = [3, user_radius, PI]

sphere_volume = math.prod(multiplication_list) / 4
sphere_volume_result = Decimal(str(sphere_volume)).quantize(Decimal('0.01'))

print('Sphere volume >>> ', sphere_volume_result)
