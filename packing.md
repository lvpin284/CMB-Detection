# Pyinstaller

## 打包

```shell
pyinstaller test.py ^
--hidden-import ultralytics --collect-all ultralytics ^
--hidden-import torch --collect-all torch ^
--add-data dataset;dataset ^
--add-data runs/detect/best.pt;runs/detect ^
--add-data CMB_Segmentation;CMB_Segmentation ^
--clean -y --log-level=INFO
```

- [x] 测试1

会读取当前python环境中的一些包，也会读取到项目中依赖的资源文件

```shell
.\dist\test\test.exe
```

- [x] 测试2

脱离虚拟环境和项目资源文件测试程序可用性。  
进入dist目录，打开一个CMD，执行打包好的exe文件

- [ ] 测试3

将打包好的目录复制到其他地方执行看看有没有问题