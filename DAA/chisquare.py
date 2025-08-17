from random import randint


val = [0.34, 0.90, 0.25, 0.89, 0.87, 0.44, 0.12, 0.21, 0.46, 0.61, 0.83, 0.76, 0.79, 0.64, 0.70, 0.81, 0.94, 0.74, 0.22, 0.74, 0.96, 0.99, 0.77, 0.67, 0.56, 0.41, 0.52, 0.73, 0.99, 0.02, 0.70, 0.16, 0.21, 0.12, 0.76, 0.37, 0.23, 0.69, 0.8, 0.70, 0.46, 0.22, 0.74, 0.77, 0.89, 0.87, 0.66, 0.19, 0.47, 0.16, 0.64, 0.42, 0.94, 0.48, 0.29, 0.62, 0.83, 0.08, 0.39, 0.62, 0.63, 0.15, 0.34, 0.06, 0.08, 0.03, 0.66, 0.74, 0.65, 0.19, 0.97, 0.65, 0.88, 0.86, 0.11, 0.62, 0.39, 0.6, 0.25, 0.21, 0.29, 0.07, 0.06, 0.97, 0.8, 0.39, 0.56, 0.08, 0.36, 0.31, 0.09, 0.91, 0.78, 0.82, 0.45, 0.89, 0.5, 0.24, 0.27, 0.59]
#print(val)

chi_test_value = 16.9

observed = [0 for i in range(10)]
estimated = [10 for i in range(10)]
diff_squared=[0 for i in range(10)]


for num in val:
    observed[int(num*10)]+=1

diff_squared = [(pow(observed[i]-estimated[i], 2))/estimated[i] for i in range(10)]

X = sum(diff_squared)

print(f'Class\t Observed\t Estimated\t ((Oi-Ei)^2)/Ei')
for i in range(10):
    print(f'{i+1}\t {observed[i]}\t\t {estimated[i]}\t\t\t {diff_squared[i]}')


if (X < chi_test_value):
    print("\n\nThe data is uniformly distributed")

else:
    print("\n\nThe data is not uniformly distributed")