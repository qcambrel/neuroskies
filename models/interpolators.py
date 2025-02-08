import numpy as np
import scipy.signal as signal

SUPPORTED_MODELS: tuple = (
    "wavelet_phase", 
    "optical_flow", 
    "csp", 
    "mls", 
    "arap", 
    "beier_neely", 
    "tps"
)

class Interpolator:
    def __init__(self, model: str):
        self.model: str = model