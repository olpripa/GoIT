VALUE = 0.5

temps = [0.5, 0.0, -3.5, 0.0, 2.0, 3.5, 0.5, -4.0, -3.5, -0.5, -3.5, -10.5, -14.0, -1.0, -1.0]

fix_t = [t + VALUE for t in temps]
print(fix_t)

unique_t = {t + VALUE for t in temps}
print(unique_t)

tr_t = {t: t + VALUE for t in temps}
print(tr_t)