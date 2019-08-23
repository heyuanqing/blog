1、ffmpeg不同版本之间不能直接切换  有可能存在内存泄漏

## 问题1 编译动态库时报错

```
/usr/bin/ld: libavcodec/mqc.o: relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
libavcodec/mqc.o: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
make: *** [libavcodec/libavcodec.so.57] Error 1
```

