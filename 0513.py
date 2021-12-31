import matplotlib.pyplot as plt
import numpy as np
import math
temps=[  873, 900, 1073, 1173]
d= [4.106691801184468e-08, 8.854853626252537e-08, 6.619182044626977e-08, 3.2684305477009534e-08]
y=np.log(d)
'''c=3.843908270799531e-08
Ea=-0.013159439372325039
k=1.3806505e-23
arr = c* np.exp(-Ea / (k  * np.array(temps)))'''
t_1 = 1000 / np.array(temps)
plt.plot( t_1, y, "k--", marktersize=10)
plt.text(
        0.6,
        0.85,
        "E$_a$ = {:.0f} meV".format(26),
        fontsize=10,
    )
plt.ylabel("D (cm$^2$/s)")
plt.xlabel("1000/T (K$^{-1}$)")
plt.title('arrhenius')
#plt.plot(t_1, y,  "ko", markersize=10)
#plt.plot(t_1, y, "k--", markersize=10)
plt.show()

