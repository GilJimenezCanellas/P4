import numpy as np
import matplotlib.pyplot as plt

# Load data
datos_lp = np.loadtxt('lp.txt')
coef_2_lp = datos_lp[:, 0]
coef_3_lp = datos_lp[:, 1]

datos_lpcc = np.loadtxt('lpcc.txt')
coef_2_lpcc = datos_lpcc[:, 0]
coef_3_lpcc = datos_lpcc[:, 1]

datos_mfcc = np.loadtxt('mfcc.txt')
coef_2_mfcc = datos_mfcc[:, 0]
coef_3_mfcc = datos_mfcc[:, 1]

sz = 5

# Plot LP
plt.subplot(3, 1, 1)
plt.scatter(coef_2_lp, coef_3_lp, s=sz, c=[0, 0.7, 0.7], edgecolors=[0, 0.5, 0.5], linewidth=0.5)
plt.title('Parametrización LP')
plt.xlabel('Coeficiente 2')
plt.ylabel('Coeficiente 3')
plt.grid(True)

# Plot LPCC
plt.subplot(3, 1, 2)
plt.scatter(coef_2_lpcc, coef_3_lpcc, s=sz, c=[0.3, 0, 0.7], edgecolors=[0.3, 0, 0.5], linewidth=0.5)
plt.title('Parametrización LPCC')
plt.xlabel('Coeficiente 2')
plt.ylabel('Coeficiente 3')
plt.grid(True)

# Plot MFCC
plt.subplot(3, 1, 3)
plt.scatter(coef_2_mfcc, coef_3_mfcc, s=sz, c=[0.7, 0.2, 0], edgecolors=[0.5, 0.2, 0], linewidth=0.5)
plt.title('Parametrización MFCC')
plt.xlabel('Coeficiente 2')
plt.ylabel('Coeficiente 3')
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
