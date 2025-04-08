#Lists

tea_varieties = ['Black','Green','Oolong','White']
tea_varieties[3] = 'Herbal'
print(tea_varieties)

tea_varieties[1:2] = ['Lemon']
print(tea_varieties)

tea_varieties.append("Green")

print(tea_varieties)

tea_varieties.pop()

print(tea_varieties)

tea_varieties_copy = tea_varieties.copy()

tea_varieties_copy.append("Lemon")

print(tea_varieties)
