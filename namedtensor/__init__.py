from .core import assert_match
from .torch_base import ntorch
from .torch_helpers import NamedTensor, build, contract
import numpy as np

version = "0.0.1"


## (Just for the blog post)
##
def _im_init():
    ## PRINT SETUP
    from PIL.Image import fromarray
    from IPython import get_ipython
    import torch

    def numpy_to_png(a):
        return fromarray(np.array(np.clip(a, 0, 1) * 255, dtype="uint8"))._repr_png_()

    png = get_ipython().display_formatter.formatters["image/png"]
    txt = get_ipython().display_formatter.formatters["text/plain"]

    png.for_type(torch.Tensor, lambda t: numpy_to_png(t.numpy()))
    txt.for_type(torch.Tensor, lambda *x: "")
    png.for_type(NamedTensor, lambda t: numpy_to_png(t.tensor.numpy()))
    txt.for_type(NamedTensor, lambda *x: "")
