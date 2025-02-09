import constants
import numpy as np
import scipy.optimize as opt
import scipy.signal as signal

class Evolver:
    def __init__(self, model: str) -> None:
        self.model: str = model