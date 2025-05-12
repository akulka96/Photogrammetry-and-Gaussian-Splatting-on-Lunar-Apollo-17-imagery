
import torch
import numpy as np
from torch.serialization import add_safe_globals
from pathlib import Path
from nerfstudio.scripts.viewer.run_viewer import RunViewer

# Allow NumPy internal types needed for deserialization
add_safe_globals([
    np.core.multiarray.scalar,
    np.dtype,
    np.float64,
    np.dtypes.Float64DType
])

# Run viewer using a specific config path
config_path = Path("/home/atharv/gaussianssplat/outputs/splating/unnamed/splatfacto/2025-05-11_113827/config.yml")
viewer = RunViewer(load_config=config_path)
viewer.main()
