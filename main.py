import matplotlib.pyplot as plt
import argparse


import utils

def main():

    parser = argparse.ArgumentParser(description='Fit power law to data')
    parser.add_argument('path', type=str, help='Path to data file')
    
    args = parser.parse_args()

    size, lifetime = utils.load(args.path)

    lawLifetime, lawFitLiftime = utils.fit(lifetime, discrete=True)
    lawSize, lawFitSize = utils.fit(size, discrete=False)

    uniqueLifetime, area = utils.getArea(lifetime, size)
    m, c = utils.fitPowerFunction(uniqueLifetime, area)
    
    plt.figure()
    plt.subplot(221)
    utils.plot_pdf_empirical(lawSize)
    utils.plot_pdf_fit(lawSize, lawFitSize, size)
    plt.xlabel('Size')
    plt.ylabel('PDF')
    plt.legend()

    plt.subplot(222)
    utils.plot_pdf_empirical(lawLifetime)
    utils.plot_pdf_fit(lawLifetime, lawFitLiftime, lifetime)
    plt.xlabel('Lifetime')
    plt.ylabel('PDF')
    plt.legend()

    plt.subplot(223)
    utils.plotPowerFunction(uniqueLifetime, area, m, c)
    plt.xlabel('Lifetime')
    plt.ylabel('Area')
    plt.legend()

    plt.tight_layout()
    plt.show()
    


if __name__ == '__main__':
    main()