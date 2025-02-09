SUPPORTED_MODELS: dict = {
    "evolver": ("nevergrad", "pso"),
    "upsampler": ("nearest", "bilinear", "bicubic", "lanczos"),
    "interpolator": ("wavelet_phase", "optical_flow", "csp", "mls", "arap", "beier_neely", "tps")
}