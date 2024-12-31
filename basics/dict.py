taste ={"Masala":"spicy","Ginger":"zesty","Green":"mild"}
print(taste)
print(taste["Ginger"])
print(taste.get("black"))
print(taste["Green"])
taste["Green"]="fresh"
print (taste)
for chai in taste:
        print(chai)
for chai in taste:
        print(chai,taste[chai])
for key,value in taste.items():
        print(key,value)
if "Masala" in taste:
        print("i have the tea")
print(len(taste))
taste["Black"]="bitter"
print(taste)
print(taste.pop("Ginger"))
print(taste.popitem())
del taste["Green"]
print(taste)
taste_copy=taste
taste_copy["Mint"]="refreshing"
print(taste)
print(taste_copy)
taste_copy_real=taste.copy()
taste_copy_real["milk"]="sweet"
print(taste)
print(taste_copy_real)

Tea_shop = {
    "chai": {"Masala": "spicy", "Ginger": "zesty"},
    "herbal": {"Mint": "refreshing", "black": "bitter"}
}
print(Tea_shop)
print(Tea_shop["chai"])
print(Tea_shop["chai"]["Ginger"])

squared_nums = {x: x*x for x in range(1,10)}
print(squared_nums)
squared_nums.clear()
print(squared_nums)

keys=["a","b","c","d"]
default_value=0
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)
