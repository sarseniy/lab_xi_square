x = []
y = []
dy = []

W = 0

xy_slash = 0
x_slash = 0
x2_slash = 0
y_slash = 0
y2_slash = 0

with open('data.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        if line.startswith('#') or line == '':
            continue
        x_1, y_1, dy_1 = line.split(' ')
        x.append(float(x_1))
        y.append(float(y_1))
        dy.append(float(dy_1))

for dy_1 in dy:
    W += 1/(dy_1 ** 2)

for i in range(5):
    xy_slash += x[i] * y[i] * (1 / (dy[i] ** 2))

xy_slash /= W

for i in range(5):
    x_slash += x[i] * (1 / (dy[i] ** 2))

x_slash /= W

for i in range(5):
    x2_slash += x[i] ** 2 * (1 / (dy[i] ** 2))

x2_slash /= W

for i in range(5):
    y_slash += y[i] * (1 / (dy[i] ** 2))

y_slash /= W

for i in range(5):
    y2_slash += y[i] ** 2 * (1 / (dy[i] ** 2))

y2_slash /= W

k = (xy_slash - x_slash * y_slash) / (x2_slash - x_slash ** 2)

b = y_slash - k * x_slash

sigma_k = ((1/3) * ((y2_slash - y_slash ** 2) / (x2_slash - x_slash ** 2) - k ** 2)) ** 0.5

sigma_b = sigma_k * x2_slash ** 0.5

print('k = ' + str(k) + ' +- ' + str(sigma_k))
print('b = ' + str(b) + ' +- ' + str(sigma_b))
