
import numpy as np
import torch
from torch.serialization import add_safe_globals

# Allow NumPy internals needed for deserialization
add_safe_globals([
    np.core.multiarray.scalar,
    np.dtype,
    np.float64,
    np.int64
])

# Patch torch.load to default to weights_only=False
_original_load = torch.load
def patched_load(*args, **kwargs):
    kwargs.setdefault("weights_only", False)
    return _original_load(*args, **kwargs)
torch.load = patched_load

# Import viewer after patch
from nerfstudio.scripts.viewer import run_viewer

if __name__ == "__main__":
    run_viewer.entrypoint()
