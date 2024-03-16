# without for loop
expenses = [1200, 1300, 1500, 1700]
total_expenses = expenses[0] + expenses[1] + expenses[2] + expenses[3]
print(f'without loop {total_expenses}')
total_expenses = 0

# with for loop
for expense in expenses:
    total_expenses += expense

print(f'with loop {total_expenses}')

total_expenses = 0
# range function
for expense in range(len(expenses)):
    total_expenses += expenses[expense]
print(f'with range {total_expenses}')
total_expenses = 0
for index, expense in enumerate(expenses):
    total_expenses += expenses[index]
    print(f'Month {index +1}: {total_expenses}')




