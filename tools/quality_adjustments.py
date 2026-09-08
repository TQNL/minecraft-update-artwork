"""Deterministic, bounded tonal adjustments; no spatial warping or generation.

Requires numpy, Pillow and OpenCV. Apply to the immutable F-branch checkpoint,
not to already processed outputs. Parameters and source hashes live in the review.
"""
import numpy as np
import cv2

def smooth(v):
    v=np.clip(v,0,1)
    return v*v*(3-2*v)

def edge_weight(shape, left, right, feather):
    x=np.arange(shape[1])[None,:]
    return np.broadcast_to(1-smooth((x-left)/feather)*smooth((right-x)/feather),shape[:2]).copy()

def clarity(rgb, weight, amount=.3, sigma=1.0, cap=3., threshold=.7):
    """Boost luminance detail only, with a noise floor and local overshoot guard."""
    a=rgb.astype(np.float32)
    lum=a@np.array([.2126,.7152,.0722],np.float32)
    detail=lum-cv2.GaussianBlur(lum,(0,0),sigma)
    signal=np.sign(detail)*np.maximum(np.abs(detail)-threshold,0)
    delta=np.clip(signal*amount,-cap,cap)*weight
    local_min=cv2.erode(lum,np.ones((3,3),np.uint8))
    local_max=cv2.dilate(lum,np.ones((3,3),np.uint8))
    target=np.clip(lum+delta,local_min,local_max)
    return np.rint(a+(target-lum)[...,None]).clip(0,255).astype(np.uint8)

def apply(rgb,aid):
    h,w=rgb.shape[:2]
    if aid in ['R17','R16']:
        weight=edge_weight(rgb.shape,150,w-150,140)
        if aid=='R16':
            yy,xx=np.mgrid[:h,:w]
            breeze=smooth((xx-759)/30)*smooth((1409-xx)/30)*smooth((yy-715)/30)*smooth((1227-yy)/30)
            weight=np.maximum(weight,.7*breeze)
        return clarity(rgb,weight,amount=.3,sigma=.9,cap=2.5)
    if aid=='R23':
        return clarity(rgb,np.ones((h,w),np.float32),amount=.25,sigma=1.1,cap=2.5,threshold=1.)
    if aid in ['R40A','R40B']:
        weight=edge_weight(rgb.shape,820,3500,240)
        out=clarity(rgb,weight,amount=.45,sigma=1.3,cap=3.,threshold=.85)
        # Gentle transition in acutance at the nominal edges of the native
        # centre. This mixes neighboring pixels only, never source variants.
        # Broad feathering prevents a new hard border around the adjustment.
        x=np.arange(w)[None,:]
        band=.28*(np.exp(-((x-900)/85)**2)+np.exp(-((x-3400)/85)**2))
        out=np.rint(out*(1-band[...,None])+cv2.GaussianBlur(out,(0,0),.65)*band[...,None]).clip(0,255).astype(np.uint8)
        if aid=='R40B':
            # Exact title overlay is reapplied by the driver from R40A/R40B
            # differences; never sharpen the title a second time.
            pass
        return out
    return rgb.copy()
