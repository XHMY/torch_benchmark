import torch
import torchvision
from tqdm import tqdm
import time
import pandas as pd
import platform

torch.backends.cudnn.benchmark = True

print('*** PyTorch Vision Models Training Test ***\t')
print('Pytorch version\t:', torch.__version__)
print('CUDA version\t:', torch.version.cuda)
print('GPU\t\t:',torch.cuda.get_device_name())
print('Platform\t:', platform.platform())

res_dict = []

for model_name in tqdm(['vgg13', 'resnet50', 'densenet201', 'vit_b_16', 'swin_v2_b', 'convnext_base']):
    for half_status in [True, False]:
        model = eval(f'torchvision.models.{model_name}(){".half()" if half_status else ""}.cuda()')
        # model = torch.compile(model)
        loss = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
        start_time = time.time()
        batch_size = 64
        epochs = 100
        img_size = 224
        for i in tqdm(range(epochs)):
            optimizer.zero_grad()
            output = model(torch.randn(batch_size, 3, img_size, img_size, dtype=torch.float16 if half_status else torch.float32, device='cuda'))
            l = loss(output, torch.randint(0,5,(batch_size, ), device='cuda'))
            l.backward()
            optimizer.step()

        end_time = time.time()
        res_dict.append({
            "model_name": model_name,
            "float16": half_status,
            "img_size": img_size,
            "batch_size": batch_size,
            "images per second": batch_size * epochs / (end_time - start_time)
            })

res_df = pd.DataFrame(res_dict)
print(res_df.sort_values(["float16", "model_name"]))