jelly = {'name':"Mango", 'type':'절임','ingredient': ['mango','sugar','yellow dye'],'origin':'필리핀'}
for i,value in jelly.items():
    print(i, value, end=' ')
print()
print(jelly['ingredient'][0])

print(jelly['origin'])

jelly_keys_values = list(jelly.items())
print(jelly_keys_values) 