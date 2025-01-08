import numpy as np
from scipy.stats import norm

def bimodal_pdf(x):
    # Parameters for the two Gaussian distributions
    mu1, sigma1, weight1 = 7.5, 0.5, 0.3  # Morning peak
    mu2, sigma2, weight2 = 20, 0.5, 0.7    # Evening peak (is maximum)
    
    # PDF as a mixture of two Gaussians
    pdf = weight1 * norm.pdf(x, mu1, sigma1) + weight2 * norm.pdf(x, mu2, sigma2)
    return pdf

def test():
    result = bimodal_pdf(8)
    print("import works. result = " + str(result))