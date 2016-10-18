#!/usr/bin/env python
"""Module for GCMSE --- Gradient Conduction Mean Square Error."""
import numpy as np
from scipy import ndimage
	
def GCMSE(ref_image, work_image, kappa=0.5, option=1):
    """GCMSE --- Gradient Conduction Mean Square Error.

    Computation of the GCMSE. An image quality assessment measurement 
    for image filtering, focused on edge preservation evaluation. 

    Both input images are compared, returning a float number. As little
    as the GCMSE is, more similar the images are. This metric is edge
    preservation oriented, thus differences between border regions will
    contribute more to the final result.

    The borders are obtained from the reference image, and it only works
    with images of the same scale, size and geometry. This metric is not
    intended to measure any image processing applications but filtering 
    i.e.: it will NOT work for assessing the quality of compression,
    contrast stretching...

    Parameters
    ---------    
    ref_image[]: Array of pixels. Pixel values 0 to 255.
        Reference image. The border regions will be obtained from it. 
        This image is the ideal objective, and the filtered images must
        be as much similar to it as possible.
        
    work_image[]: Array of pixels. Pixel values 0 to 255.
        Image that is compared to the reference one.
        
    kappa: decimal number. Values 0 to 1
        Conductance parameter. It increases the amount of the images
        that are analyzed, as it defines the permisivity for pixels to 
        belong to border regions, and how high is their contribution.
        
    option: integer. Values: 1 or 2
        Select which of the Perona-Malik equations will be used.
        
    Returns
    -------
    gcmse: float
        Value of the GCMSE metric between the 2 provided images. It gets
        smaller as the images are more similar.

    weight: float
        Amount of the image that has been taken into account.     
	"""
	# Normalization of the images to [0,1] values.
    ref_image_float = ref_image.astype('float32')
    work_image_float = work_image.astype('float32')	
    normed_ref_image = ref_image_float / 255
    normed_work_image = work_image_float / 255
    
    # Initialization and calculation of south and east gradients arrays.
    gradient_S = np.zeros_like(normed_ref_image)
    gradient_E = gradient_S.copy()
    gradient_S[:-1,: ] = np.diff(normed_ref_image, axis=0)
    gradient_E[: ,:-1] = np.diff(normed_ref_image, axis=1)
    
    # Image conduction is calculated using the Perona-Malik equations.
    if option == 1:
        cond_S = np.exp(-(gradient_S/kappa) ** 2)
        cond_E = np.exp(-(gradient_E/kappa) ** 2)
    elif option == 2:
        cond_S = 1.0 / (1 + (gradient_S/kappa)**2)
        cond_E = 1.0 / (1 + (gradient_E/kappa)**2)
        
    # New conduction components are initialized to 1 in order to treat
    # image corners as homogeneous regions
    cond_N = np.ones_like(normed_ref_image)
    cond_W = cond_N.copy()
    # South and East arrays values are moved one position in order to
    # obtain North and West values, respectively. 
    cond_N[1:, :] = cond_S[:-1, :]
    cond_W[:, 1:] = cond_E[:, :-1]
    
    # Conduction module is the mean of the 4 directional values.
    conduction = (cond_N + cond_S + cond_W + cond_E) / 4
    conduction = np.clip (conduction, 0., 1.)
    G = 1 - conduction
    
    # Calculation of the GCMSE value 
    num = ((G*(normed_ref_image - normed_work_image)) ** 2).sum()
    gcmse = num * normed_ref_image.size / G.sum()
    weight = G.sum() / G.size
    
    return [gcmse, weight]


