seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

print(seating_chart[2][1])

for i, row in enumerate(seating_chart):
  for a, name in enumerate(row):
    print(f"{name} is in row, seat [{i+1}, {a+1}]")
  
    