import numpy as np
import scipy.optimize as opt

SUPPORTED_MODELS: tuple = ("nevergrad", "pso")

class Evolver:
    def __init__(self, model: str) -> None:
        self.model: str = model