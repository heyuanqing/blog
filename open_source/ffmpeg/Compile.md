./configure --target-os=linux 
--arch=arm \
--prefix=/root/android/ffmpeg/ffmpeg-4.0.2/android/arm \
--enable-shared \
 --disable-static \
 --disable-doc \
 --disable-ffmpeg \
 --disable-ffplay \
 --disable-ffprobe \
 --disable-doc \
 --disable-symver \
 --enable-cross-compile --cross-prefix=/root/android/ndk/ndk-build/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi- \
 --sysroot=/root/android/ndk/ndk-build/platforms/android-21/arch-arm \
 --extra-cflags=-fpic \
 --sysinclude=/root/android/ndk/ndk-build/sysroot/usr/include \
 --extra-cflags=-I/root/android/ndk/ndk-build/sysroot/usr/include \
 --extra-cflags=-I/root/android/ndk/ndk-build/sysroot/usr/include/arm-linux-androideabi \
 --disable-ffserver

