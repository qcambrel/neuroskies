import constants
import numpy as np
import scipy.signal as signal

class Interpolator:
    def __init__(self, model: str):
        self.model: str = model