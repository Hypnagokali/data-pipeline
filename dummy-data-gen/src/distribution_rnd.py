import numpy as np
from scipy.stats import norm

# do we really need weight?
def distribution(mu1, sigma1, weight1, mu2, sigma2, weight2):
    def bimodal_pdf(time_point):    
        pdf = weight1 * norm.pdf(time_point, mu1, sigma1) + weight2 * norm.pdf(time_point, mu2, sigma2)
        return pdf
    return bimodal_pdf
