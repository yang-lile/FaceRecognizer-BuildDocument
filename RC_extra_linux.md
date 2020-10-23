## FaceRecognizer 额外包拓展

### 环境声明

- qt5
- cmake
- 涉及的其他的包都要自己编译

> #### 找不到 log4cplus

下载位置：[https://sourceforge.net/projects/log4cplus/files/log4cplus-stable/](https://sourceforge.net/projects/log4cplus/files/log4cplus-stable/)

同时更建议在GitHub上下载到源码来自己编译：[https://github.com/log4cplus/log4cplus.git](https://github.com/log4cplus/log4cplus.git)

使用文档里的命令来编译（但是文档没有）

尝试使用cmake常用命令

```bash
cd log4cplus
mkdir build
cd build
cmake ..
cmake --build . --config Release
sudo cmake --build . --config Release --target install
```

安装成功，但是不清楚如何使用该包，当编译FR时，找到了该模块，但是模块内的一个函数没有找到。

判断是版本不同的问题，尝试查询历史修改和直接解读源码

#### 其他模块

- ncnn
- facedetection
- SeetaFace
- OpenCV
