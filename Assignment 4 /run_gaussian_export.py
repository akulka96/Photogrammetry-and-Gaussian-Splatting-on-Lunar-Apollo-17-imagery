
import sys
import torch
import numpy as np
from torch.serialization import add_safe_globals
from nerfstudio.scripts.exporter import entrypoint

# Allow NumPy-related types for safe deserialization
add_safe_globals([
    np.core.multiarray.scalar,
    np.dtype,
    np.float64,
    np.dtypes.Float64DType
])

# Set command-line arguments manually
sys.argv = [
    "ns-export",
    "gaussian-splat",
    "--load-config", "outputs/splating/unnamed/splatfacto/2025-05-11_113827/config.yml",
    "--output-dir", "render/GaussianImages"
]

entrypoint()
