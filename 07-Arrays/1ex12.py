categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

i = 0
most_exp = 0
most_exp_cat = 0
for i in range(0,len(categories)):
    if expenses[i] > most_exp:
        most_exp = expenses[i]
        most_exp_cat = i
    i += 1

print(i)


print(most_exp)
print(categories[most_exp_cat])
