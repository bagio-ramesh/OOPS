expenses = [10000,12000,15000,13000,17000,16000,14000,18000,19000,20000,21000,22000]
len_expenses = len(expenses)

expenses[2] = 22000
print(expenses)

min_expens = min(expenses)
print("min expense:",min_expens)

max_expens = max(expenses)
print("max expense:",max_expens)
 
tottal_yearly = sum(expenses)
print("Total yearly Expense:",tottal_yearly)

average_monthly = tottal_yearly / len_expenses
print("average of month:",average_monthly)

second_largest = sorted(expenses,reverse=True)
print("second largest is:",second_largest[2]) 
