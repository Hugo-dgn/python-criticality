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
    """
    -data: data to fit
    -discrete: if data is discrete

    return: law, lawFit
        -law: powerlaw.Fit object
        -lawFit: powerlaw.Power_Law object
    
    Here law is the fit to the data and lawFit is the power law with the parameters of the fit
    """
    law = powerlaw.Fit(data, discrete=discrete)
    alpha = law.power_law.alpha
    xmin = law.power_law.xmin
    lawFit = powerlaw.Power_Law(xmin=xmin, parameters=[alpha], discrete=discrete)
    return law, lawFit

def fitPowerFunction(uniqueLifetime, area):
    """
    -uniqueLifetime: unique values of lifetime
    -area: area of the data

    return: m, c
        -m: gamma parameter (slope of the linear fit)
        -c: constant parameter (intercept of the linear fit)
    """
    log_unqiueLifetime = np.log(uniqueLifetime)
    log_area = np.log(area)

    A = np.vstack([log_unqiueLifetime, np.ones(len(log_unqiueLifetime))]).T
    m, c = np.linalg.lstsq(A, log_area, rcond=None)[0]
    return m, c

def plotPowerFunction(uniqueLifetime, area, m, c):
    plt.loglog(uniqueLifetime, area, 'bo', label='Empirical')
    plt.loglog(uniqueLifetime, np.exp(m*np.log(uniqueLifetime) + c), 'r', label=f'Fit (gamma = {m:.2f}')

def getArea(lifetime, size):
    uniqueLifetime = np.unique(lifetime)
    uniqueLifetime = np.sort(uniqueLifetime)
    area = np.zeros(uniqueLifetime.shape)
    for i, t in enumerate(uniqueLifetime):
        area[i] = np.sum(size[lifetime == t])

    return uniqueLifetime, area