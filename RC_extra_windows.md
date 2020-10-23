## FaceRecognizer 额外包拓展

### 环境声明

- virtual studio 14 2015
- qt 5.12.0
- cmake 3.18.4 win64 x64

### 第三方库声明

使用的已编译库

- windows_msvc15_x64_Release_qt5.13.2_v0.3.3

### 尝试使用方法

1. 解压已编译库后运行 `change_prefix.sh`
2. （不清楚是否需要点击 `setup_vars_opencv4.cmd` 配置openCV的环境变量）但是编写的时候点击了
3. 运行命令行：
   ```powershell
   cd FaceRecognizer/build
   cmake .. -DCMAKE_INSTALL_PREFIX=install ^
        -DCMAKE_BUILD_TYPE=Release ^
        -G "Visual Studio 14 2015 Win64" ^
        -DQt5_DIR=C:\Qt\Qt5.12.0\5.12.0\msvc2015_64\lib\cmake\Qt5 ^
        -DRabbitCommon_DIR=C:\Users\lilua\workspace\RabbitCommon ^
        -DUSE_OPENCV=TRUE ^
        -DOpenCV_DIR=C:\Users\lilua\workspace\extra\x64\vc15\lib ^
        -DUSE_YUV=TRUE ^
        -DYUV_DIR=C:\Users\lilua\workspace\extra\lib\cmake ^
        -DUSE_FFMPEG=TRUE ^
        -Dncnn_DIR=C:\Users\lilua\workspace\extra\lib\cmake\ncnn ^
        -DSeetaFace_DIR=C:\Users\lilua\workspace\extra\lib\cmake ^
        -Dfacedetection_DIR=C:\Users\lilua\workspace\extra\lib\cmake\facedetection ^
        -DENABLE_DOWNLOAD=ON ^
   ```
4. 根据报错
5. C:\Users\lilua\workspace\extra\lib\cmake

### 出现问题的解决

> #### 下载 `face_landmark_model.dat` 失败

根据 [https://www.jianshu.com/p/1389704c3167](https://www.jianshu.com/p/1389704c3167) 该博客中提到的，自己在 GitHub 上下载到文件，然后放入 `C:\Users\lilua\workspace\FaceRecognizer\model\Opencv` 目录下即可。

使用文件的地址： [https://raw.githubusercontent.com/opencv/opencv_3rdparty/8afa57abc8229d611c4937165d20e2a2d9fc5a12/face_landmark_model.dat](https://raw.githubusercontent.com/opencv/opencv_3rdparty/8afa57abc8229d611c4937165d20e2a2d9fc5a12/face_landmark_model.dat) 其中如果需要最新版，只需自己在 [https://raw.githubusercontent.com/opencv/opencv_3rdparty/](https://raw.githubusercontent.com/opencv/opencv_3rdparty/) 下寻找最新版本即可。

> #### 解决找不到OpenSSL的问题

其他平台不需多言，自己安装 `openssl-devel` 就可以使用，Windows下比较傻，点名批评。

##### 现在需要的环境：

1. perl
2. nasm

##### 需要的包

openssl

##### 安装教程

1. 在 [http://strawberryperl.com/](http://strawberryperl.com/) 下找到64位的 perl 包，下载并安装
2. 在 [https://www.nasm.us/pub/nasm/releasebuilds/?C=M;O=D](https://www.nasm.us/pub/nasm/releasebuilds/?C=M;O=D) 中下在 nasm 包，后面的参数是按日期降序，还挺不错
3. 配置 perl 和 nasm 环境，在系统环境变量PATH里添加：
   ```
   C:\Users\lilua\AppData\Local\bin\NASM
   C:\Strawberry\c\bin
   C:\Strawberry\perl\site\bin
   C:\Strawberry\perl\bin
   ```
4. 在 vs2015 里找一个你想要编译的版本，我们统一是 x64 ，即 `VS2015 x64 本机工具命令提示符` 
5. 找个目录开始执行命令行操作
   
   *注：请泡一杯咖啡来等待，Windows真垃圾。*
   ```powershell
   # 下载openssl，但是可能会因为网不好暴毙，建议在release里下载稳定版的包直接解压使用
   git clone --recursive https://github.com/openssl/openssl.git
   cd openssl
   # 编译文档在该目录下的 NOTES-Windows.txt 里，我们同样选择64位
   perl Configure VC-WIN64A
   nmake
   nmake test
   nmake install
   # 之后可能需要重启，我是不小心重启了，具体是否需要不清楚
   # 验证安装好了
   openssl.exe version
   ```

> #### 找不到 log4cplus

*注：找不到，自己编译啊。。。这就是Windows的环境吗，爱了爱了*

下载位置：[https://sourceforge.net/projects/log4cplus/files/log4cplus-stable/](https://sourceforge.net/projects/log4cplus/files/log4cplus-stable/)

同时更建议在GitHub上下载到源码来自己编译：[https://github.com/log4cplus/log4cplus.git](https://github.com/log4cplus/log4cplus.git)




