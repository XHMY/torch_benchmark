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
