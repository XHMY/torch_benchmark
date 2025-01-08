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


### GeForce RTX™ 4090 GAMING OC (Ubuntu 22.04.2 LTS)

```
*** Matrix multiplication test ***	
Pytorch version	: 2.1.0a0+fe05266
CUDA version	: 12.1
GPU		: NVIDIA GeForce RTX 4090
Platform	: Linux-5.19.0-42-generic-x86_64-with-glibc2.29
               n=128   n=512   n=2048   n=8192  n=16384
torch.float64  0.139   1.192    1.208    1.209    1.205
torch.float32  1.017  28.959   82.870   86.069   86.406
torch.float16  0.991  46.028  163.917  167.680  171.077
        65536    262144    1048576   4194304
TFLOPS    0.020    0.081     0.318     0.474
GB/s    163.038  648.931  2545.951  3791.159
*** PyTorch Vision Models Training Test ***	
Pytorch version	: 2.1.0a0+fe05266
CUDA version	: 12.1
GPU		: NVIDIA GeForce RTX 4090
Platform	: Linux-5.19.0-42-generic-x86_64-with-glibc2.29
       model_name  float16  img_size  batch_size  images per second
11  convnext_base    False       224          64         206.842381
5     densenet201    False       224          64         385.002822
3        resnet50    False       224          64         697.398160
9       swin_v2_b    False       224          64         186.133231
1           vgg13    False       224          64         467.028589
7        vit_b_16    False       224          64         350.083329
10  convnext_base     True       224          64         567.728980
4     densenet201     True       224          64         632.903872
2        resnet50     True       224          64        1296.704699
8       swin_v2_b     True       224          64         379.712459
0           vgg13     True       224          64         778.508125
6        vit_b_16     True       224          64         766.554800
*** PyTorch 3D Convolutional Network Benchmark ***	
Pytorch version	: 2.1.0a0+fe05266
CUDA version	: 12.1
GPU		: NVIDIA GeForce RTX 4090
Platform	: Linux-5.19.0-42-generic-x86_64-with-glibc2.29
float 16 time: 0.08919850826263427 
float 32 time: 0.17720082759857178

```

### NVIDIA TITAN RTX (Ubuntu 22.04.2 LTS)

```
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
```

### NVIDIA H100 80GB HBM3

```
*** Matrix multiplication test ***
Pytorch version : 2.1.1
CUDA version    : 12.1
GPU             : NVIDIA H100 80GB HBM3
Platform        : Linux-5.14.0-162.23.1.el9_1.x86_64-x86_64-with-glibc2.34
               n=128   n=512   n=2048   n=8192  n=16384
torch.float64  0.530  29.986   52.492   46.701   48.948
torch.float32  0.536  17.703   51.137   51.514   53.009
torch.float16  0.520  33.500  401.502  626.037  658.557
        65536    262144    1048576   4194304
TFLOPS    0.014    0.056     0.225     0.468
GB/s    112.115  447.139  1800.379  3743.574
*** PyTorch Vision Models Training Test ***
Pytorch version : 2.1.1
CUDA version    : 12.1
GPU             : NVIDIA H100 80GB HBM3
Platform        : Linux-5.14.0-162.23.1.el9_1.x86_64-x86_64-with-glibc2.34
       model_name  float16  img_size  batch_size  images per second
11  convnext_base    False       224          64         232.561327
5     densenet201    False       224          64         557.317382
3        resnet50    False       224          64        1380.650486
9       swin_v2_b    False       224          64         243.054995
1           vgg13    False       224          64        1070.426841
7        vit_b_16    False       224          64         353.716016
10  convnext_base     True       224          64         834.098826
4     densenet201     True       224          64         626.646100
2        resnet50     True       224          64        1674.054897
8       swin_v2_b     True       224          64         534.375826
0           vgg13     True       224          64        1459.862171
6        vit_b_16     True       224          64        1592.188819
```

### NVIDIA H200 141GB

```
Pytorch version : 2.5.1                                                                                                                                  
CUDA version    : 12.4                                                                                                                                   
GPU             : NVIDIA H200 MIG 7g.141gb                                                                                                               
Platform        : Linux-5.14.0-427.42.1.el9_4.x86_64-x86_64-with-glibc2.34

*** Matrix multiplication test ***
               n=128   n=512   n=2048   n=8192  n=16384                                                                                                  
torch.float64  0.214  25.517   53.091   47.667   49.345                                                                                                  
torch.float32  0.218  17.423   50.257   51.505   53.539                                                                                                  
torch.float16  0.219  25.778  399.811  650.830  663.996                                                                                                  
        65536    262144    1048576   4194304                                                                                                             
TFLOPS    0.013    0.050     0.197     0.559                                                                                                             
GB/s    101.300  398.265  1577.591  4469.536

*** PyTorch Vision Models Training Test ***
       model_name  float16  img_size  batch_size  images per second
11  convnext_base    False       224          64         253.450538
5     densenet201    False       224          64         657.076050
3        resnet50    False       224          64        1498.406707
9       swin_v2_b    False       224          64         259.752509
1           vgg13    False       224          64        1264.374322
7        vit_b_16    False       224          64         363.216864
10  convnext_base     True       224          64         917.461097
4     densenet201     True       224          64         709.649110
2        resnet50     True       224          64        1812.262740
8       swin_v2_b     True       224          64         582.280866
0           vgg13     True       224          64         875.882406
6        vit_b_16     True       224          64        1922.492505
```
