import torch
import platform

print('*** Matrix multiplication test ***\t')
print('Pytorch version\t:', torch.__version__)
print('CUDA version\t:', torch.version.cuda)
print('GPU\t\t:',torch.cuda.get_device_name())
print('Platform\t:', platform.platform())

import inspect
from collections import defaultdict
import pandas as pd
from torch.utils import benchmark
from tqdm import tqdm

import argparse

pd.options.display.precision = 3

def var_dict(*args):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return dict([(name, val) for name, val in callers_local_vars if val is arg][0]
                for arg in args)

def walltime(stmt, arg_dict, duration=3):
    return benchmark.Timer(stmt=stmt, globals=arg_dict).blocked_autorange(
        min_run_time=duration).median

matmul_tflops = defaultdict(lambda: {})

# argparser = argparse.ArgumentParser()
# argparser.add_argument('--gpu', type=int, default=0)
# args = argparser.parse_args()

d = torch.device("cuda")
for n in tqdm([128, 512, 2048, 8192, 16384]):
    for dtype in (torch.float64, torch.float32, torch.float16):
        a = torch.randn(n, n, dtype=dtype, device=d)
        b = torch.randn(n, n, dtype=dtype, device=d)
        t = walltime('a @ b', var_dict(a, b))
        matmul_tflops[f'n={n}'][dtype] = 2*n**3 / t / 1e12
        del a, b

print(pd.DataFrame(matmul_tflops))
torch.cuda.empty_cache()


vector = defaultdict(lambda: {})
for n in [1024*64, 1024*256, 1024*1024, 1024*1024*4]:
    a = torch.randn(n).cuda()
    t = walltime('a * 1.2', var_dict(a))
    vector[n]['TFLOPS'] = n / t / 1e12
    vector[n]['GB/s'] = 8 * n / t / 1e9
    
print(pd.DataFrame(vector))

