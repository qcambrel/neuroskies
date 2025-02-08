import numpy as np
import scipy.signal as signal

SUPPORTED_MODELS: tuple = (
    "nearest", 
    "bilinear", 
    "bicubic", 
    "lanczos"
)

class Upsampler:
    def __init__(self, model: str) :
        self.model: str = model