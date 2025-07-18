from typing import List, Optional, Tuple
import torch
import sglang as sgl

def update_weights_from_tensor_helper_engine(
    engine: sgl.Engine,
    params: List[Tuple[str, torch.Tensor]],
    load_format: Optional[str] = None,
    flush_cache: bool = True,
):
    pass

def update_weights_from_tensor_helper_server(
        url: str,
        params: List[Tuple[str, torch.Tensor]],
        load_format: Optional[str] = None,
        flush_cache: bool = True,
):
    pass
    
    