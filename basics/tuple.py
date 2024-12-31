# tuple--immutable list--mutable

tea_types=("black","herbal","green")
print(tea_types[0])
print(tea_types[2])
print(len(tea_types))
more_tea_types=("white","oolong")
all_tea_types=tea_types+more_tea_types
print(all_tea_types)

if "black" in all_tea_types:
    print("i have the tea")
more_tea_types=("white","oolong","white")
print(more_tea_types.index("white"))
print(more_tea_types.count("herb"))
(White,Oolong,Black)=more_tea_types
print(White)
type(more_tea_types)


variable=("a","b","c",(1,2,3))
print(variable)
print(variable[3][1])