# 自定义打包过程
from cx_Freeze import setup, Executable
# 指定入口点
setup(
    name='MyApp',
    version='0.1',
    description='A simple example',
    executables=[Executable('test.py')]
)

# 修改生成的可执行文件名
setup(
    name='MyApp',
    version='0.1',
    description='A simple example',
    executables=[Executable('test.py', base='MyApp')]
)