# 用于编译代码时^不可识别的问题，生成一行命令行

s = r'''cmake .. -DCMAKE_INSTALL_PREFIX=install ^
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
        -DENABLE_DOWNLOAD=ON '''
a = s.replace("^\n","")
print(a)