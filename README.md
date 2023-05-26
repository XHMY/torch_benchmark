# PyTorch Simple Benchmark

## How to use

### Docker

```shell
docker compose up
```

### Run Directly 

You have to [install PyTorch](https://pytorch.org/get-started/locally/) and `pandas`.

```shell
bash run.sh
```

## Reference Result

### GeForce RTX™ 4090 GAMING OC (WSL)

```
*** Matrix multiplication test ***	
Pytorch version	: 2.1.0a0+fe05266
CUDA version	: 12.1
GPU		: NVIDIA GeForce RTX 4090
Platform	: Linux-5.15.90.1-microsoft-standard-WSL2-x86_64-with-glibc2.29
               n=128   n=512   n=2048   n=8192  n=16384
torch.float64  0.135   1.173    1.186    1.185    1.198
torch.float32  0.430  21.183   81.196   84.598   84.876
torch.float16  0.494  24.622  160.143  165.298  170.569
        65536    262144   1048576   4194304
TFLOPS    0.008    0.028    0.109     0.342
GB/s     63.610  223.732  872.909  2732.257
*** PyTorch Vision Models Training Test ***	
Pytorch version	: 2.1.0a0+fe05266
CUDA version	: 12.1
GPU		: NVIDIA GeForce RTX 4090
Platform	: Linux-5.15.90.1-microsoft-standard-WSL2-x86_64-with-glibc2.29
       model_name  float16  img_size  batch_size  images per second
11  convnext_base    False       224          64         171.666996
5     densenet201    False       224          64         331.996900
3        resnet50    False       224          64         640.764125
9       swin_v2_b    False       224          64         152.428852
1           vgg13    False       224          64         419.025517
7        vit_b_16    False       224          64         336.902513
10  convnext_base     True       224          64         362.240264
4     densenet201     True       224          64         524.890332
2        resnet50     True       224          64        1220.042709
8       swin_v2_b     True       224          64         352.809262
0           vgg13     True       224          64         716.156016
6        vit_b_16     True       224          64         746.106620
*** PyTorch 3D Convolutional Network Benchmark ***	
Pytorch version	: 2.1.0a0+fe05266
CUDA version	: 12.1
GPU		: NVIDIA GeForce RTX 4090
Platform	: Linux-5.15.90.1-microsoft-standard-WSL2-x86_64-with-glibc2.29
float 16 time: 0.09117490291595459 
float 32 time: 0.1799030590057373
````

### NVIDIA TITAN RTX (Ubuntu 22.04.2 LTS)

*** Matrix multiplication test ***
Pytorch version : 2.1.0a0+fe05266
CUDA version    : 12.1
GPU             : NVIDIA TITAN RTX
Platform        : Linux-5.19.0-42-generic-x86_64-with-glibc2.29
               n=128   n=512  n=2048  n=8192  n=16384
torch.float64  0.054   0.456   0.506   0.511    0.528
torch.float32  0.489   9.340  13.374  14.205   14.387
torch.float16  0.445  24.715  86.287  95.710   92.192
        65536    262144   1048576  4194304
TFLOPS    0.010    0.038    0.079    0.073
GB/s     77.992  305.432  630.105  583.572
*** PyTorch Vision Models Training Test ***
Pytorch version : 2.1.0a0+fe05266
CUDA version    : 12.1
GPU             : NVIDIA TITAN RTX
Platform        : Linux-5.19.0-42-generic-x86_64-with-glibc2.29
       model_name  float16  img_size  batch_size  images per second
11  convnext_base    False       224          64          62.658015
5     densenet201    False       224          64         153.498083
3        resnet50    False       224          64         248.471759
9       swin_v2_b    False       224          64          66.316263
1           vgg13    False       224          64         193.123607
7        vit_b_16    False       224          64          87.815196
10  convnext_base     True       224          64         259.193908
4     densenet201     True       224          64         279.943765
2        resnet50     True       224          64         596.043434
8       swin_v2_b     True       224          64         162.800096
0           vgg13     True       224          64         461.465438
6        vit_b_16     True       224          64         395.141974
*** PyTorch 3D Convolutional Network Benchmark ***
Pytorch version : 2.1.0a0+fe05266
CUDA version    : 12.1
GPU             : NVIDIA TITAN RTX
Platform        : Linux-5.19.0-42-generic-x86_64-with-glibc2.29
float 16 time: 0.17795355319976808
float 32 time: 0.6057921314239502

