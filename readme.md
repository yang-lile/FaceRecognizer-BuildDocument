## FaceRecognizer 编译文档

*编辑时间: 2020.10.15，若时间太老，文档可能失效。*

- [FaceRecognizer 编译文档](#facerecognizer-编译文档)
  - [Windows 环境下](#windows-环境下)
    - [环境列表（建议）](#环境列表建议)
    - [环境搭建步骤](#环境搭建步骤)
    - [环境配置](#环境配置)
    - [编译](#编译)
    - [执行程序](#执行程序)

### Windows 环境下

#### 环境列表（建议）

- virtual studio 14 2015
- qt 5.12.0
- cmake 3.18.4 win64 x64

#### 环境搭建步骤

1. 安装 vs2015
   1. 资源包来自网盘，或者自己在微软申请历史版本的 2015 Update3 版
   2. 安装时勾选 Windows 通用开发，其他的根据需求安装，若没有安装 git ，可以在通用工具内一起安装
   3. (用于安卓开发) C++ 移动开发
2. 安装 qt5
   1. 在 [https://github.com/KangLin/RabbitThirdLibrary/releases](https://github.com/KangLin/RabbitThirdLibrary/releases) 上选择已经编译成功的 qt 版本来构建，成功率更高
   2. 不清楚具体需要什么包的可以直接选择该版本的直接安装程序。
   3. qt 安装需要注册一个 qt 账号，自行准备邮箱
   4. 在安装选项中选择以下必选包
      1. MSVC 2015 64-bit
      2. MinGW 7.3.0 64-bit
      3. (用于安卓开发) Android ARM64-v8a
      4. Sources
      5. Qt 系列的控件
3. 安装 cmake

#### 环境配置

1. cmake 需要添加系统环境变量到 Path ，值类似： `C:\Program Files\CMake\bin`

#### 编译

*以下皆为我的环境下的命令行操作：*

```powershell
git clone --recursive https://github.com/KangLin/FaceRecognizer.git
git clone https://github.com/KangLin/RabbitCommon.git
cd RabbitCommon
git pull
cd ../FaceRecognizer
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=install ^
       -DCMAKE_BUILD_TYPE=Release ^
       -DQt5_DIR=C:\Qt\Qt5.12.0\5.12.0\msvc2015_64\lib\cmake\Qt5 ^
       -DRabbitCommon_DIR=C:\Users\xxx\workspace\RabbitCommon
        -G "Visual Studio 14 2015 Win64"
.\FaceRecognizer.sln
# 然后在vs里选择Release和x64
# 编译完成后会报拒绝访问，但是没有关系，回到命令行继续执行
cmake --build . --config Release
cmake --build . --config Release --target install
```

> 注： xxx 为你的用户名， cmake 要修改的是你的 `-DQt5_DIR` 和 `-DRabbitCommon_DIR` 到对应的目录下
> 
> 注：这里直接 `-DCMAKE_BUILD_TYPE` 使用 `Release` 参数，这个参数要和之后的 vs 编译版本一致
> 
> 注：做完以上步骤后， cmake 将会自动为你安装到 window 软件目录下，找到 FaceRecognizer 文件夹，在里面运行 `FaceRecognizerApp.exe` 文件，即可看到编译结果。
> 
> 注：如果发现这一长串cmake命令报错，把^和回车去掉，缩成一行命令再执行

#### 执行程序

```powershell
cd .\install\bin\
.\FaceRecognizerApp.exe
```
