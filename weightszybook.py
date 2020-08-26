weight = []
count = 1

while len(weight) < 4:
    p_weight = input('Enter weight {}:\n'.format(count))
    weight.append(p_weight)
    count += 1

weight = [float(i) for i in weight]
print('Weights: {}\n'.format(weight))

print('Average weight: {:.2f}'.format(sum(weight) / len(weight)))
print('Max weight: {:.2f}\n'.format(max(weight)))

index = int(input('Enter a list location (1 - 4):\n'))
index -= 1
print('Weight in pounds: {:.2f}'.format(weight[index]))
print('Weight in kilograms: {:.2f}\n'.format(weight[index] / 2.2))

print('Sorted list: {}'.format(weight.sorted))