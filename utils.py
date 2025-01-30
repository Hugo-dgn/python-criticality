import matplotlib.pyplot as plt
import numpy as np

import powerlaw

def pdf(data, xmin=None, xmax=None):
    edges, hist = powerlaw.pdf(data, xmin=xmin, xmax=xmax)
    bin_centers = (edges[1:]+edges[:-1])/2
    indeces = hist > 0
    bin_centers = bin_centers[indeces]
    hist = hist[indeces]
    return bin_centers, hist

def plot_pdf_empirical(power_law):
    data = power_law.data
    bin_centers, hist = pdf(data)
    plt.loglog(bin_centers, hist, 'bo', label='Empirical')

def plot_pdf_fit(power_law, power_law_fit, x):
    pdfSize = power_law_fit.pdf(x)
    alpha = power_law_fit.alpha
    xmin = power_law_fit.xmin
    plt.plot(x[x >= power_law.xmin], pdfSize, 'r', label=f'Fit (alpha = {alpha:.2f} and xmin = {xmin:.2f})')
    plt.axvline(power_law.xmin, color='black', linestyle='--')

def load(path):
    data = np.loadtxt(path)
    size = data[:,0]
    lifetime = data[:,1].astype(np.int64)
    return size, lifetime

def fit(data, discrete=False):
    law = powerlaw.Fit(data, discrete=discrete)
    alpha = law.power_law.alpha
    xmin = law.power_law.xmin
    lawFit = powerlaw.Power_Law(xmin=xmin, parameters=[alpha], discrete=discrete)
    return law, lawFit