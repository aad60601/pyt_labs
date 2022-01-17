import district
#from district import *
#from district.central_street import *
#from district.soviet_street import *
#from district.soviet_street.house1 import *
#from district import central_street, soviet_street
a = district.central_street.house1.room1.folks + district.central_street.house1.room2.folks + district.central_street.house2.room1.folks + district.central_street.house2.room2.folks + district.soviet_street.house1.room1.folks + district.soviet_street.house1.room2.folks + district.soviet_street.house2.room1.folks + district.soviet_street.house2.room2.folks
#f = [district.soviet_street.house1.room1.folks + district.soviet_street.house1.room2.folks + district.soviet_street.house2.room1.folks + district.soviet_street.house2.room2.folks]
f = [",".join(a)]
print(f'На районе живут:{f}')

в init.py from . import central_street, soviet_street
in init.py in soviet str from . import house1, house2
in house init from .  import room1, room2
