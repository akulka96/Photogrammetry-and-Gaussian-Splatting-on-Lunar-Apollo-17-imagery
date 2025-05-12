
import torch
import numpy as np
from torch.serialization import add_safe_globals
from nerfstudio.scripts import render as ns_render

# Allow required numpy types for deserialization
add_safe_globals([np.core.multiarray.scalar, np.dtype, np.float64, np.int64])

# Patch torch.load to default to weights_only=False
_original_load = torch.load
def safe_load(*args, **kwargs):
    kwargs.setdefault('weights_only', False)
    return _original_load(*args, **kwargs)
torch.load = safe_load

# Launch NeRFStudio renderer
ns_render.entrypoint()
