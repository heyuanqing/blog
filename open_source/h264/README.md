
H264
参考：https://www.jianshu.com/p/9522c4a7818d

编码过程：帧间和帧内预测（Estimation）、变换和反变换、量化和反量化、环路滤波、熵编码

H264是由一个接一个的NALU组成，

分为两层：视频编码层（VCL）和网络提取层

一帧被编码为多个片，片是宏块的载体

宏块是视频信息的主要承载者，因为它包含着每一个像素的亮度和色度信息。视频解码最主要的工作则是提供高效的方式从码流中获得宏块中的像素阵列。

组成部分：一个宏块由一个16×16亮度像素和附加的一个8×8 Cb和一个 8×8 Cr 

彩色像素块组成。每个图象中，若干宏块被排列成片的形式。
一个原始的H.264 NALU 单元常由 [StartCode] [NALU Header] [NALU Payload] 三部分组成

占一个字节，由三部分组成

forbidden_bit(1bit)，nal_reference_bit(2bits)（优先级），nal_unit_type(5bits)（类型）

forbidden_bit:禁止位。
nal_reference_bit：当前NAL的优先级，值越大，该NAL越重要。
nal_unit_type ：NAL类型。参见下表
 
SPS(Sequence Parameter Sets)：序列参数集，作用于一系列连续的编码图像。
PPS(Picture Parameter Set)：图像参数集，作用于编码视频序列中一个或多个独立的图像。
SEI(Supplemental enhancement information)：附加增强信息，包含了视频画面定时等信息，一般放在主编码图像数据之前，在某些应用中，它可以被省略掉。
IDR(Instantaneous Decoding Refresh)：即时解码刷新。
HRD(Hypothetical Reference Decoder)：假想码流调度器。

Sps 7

pps 8

I 5 


IDR（Instantaneous Decoding Refresh）--即时解码刷新。 

I帧:帧内编码帧是一种自带全部信息的独立帧，无需参考其它图像便可独立进行解码，视频序列中的第一个帧始终都是I帧。 

   I和IDR帧都是使用帧内预测的。它们都是同一个东西而已,在编码和解码中为了方便，要首个I帧和其他I帧区别开，所以才把第一个首个I帧叫IDR，这样就方便控制编码和解码流程。 IDR帧的作用是立刻刷新,使错误不致传播,从IDR帧开始,重新算一个新的序列开始编码。而I帧不具有随机访问的能力，这个功能是由IDR承担。 IDR会导致DPB（DecodedPictureBuffer 参考帧列表——这是关键所在）清空，而I不会。IDR图像一定是I图像，但I图像不一定是IDR图像。一个序列中可以有很多的I图像，I图像之后的图像可以引用I图像之间的图像做运动参考。一个序列中可以有很多的I图像，I图像之后的图象可以引用I图像之间的图像做运动参考。 

   对于IDR帧来说，在IDR帧之后的所有帧都不能引用任何IDR帧之前的帧的内容，与此相反，对于普通的I-帧来说，位于其之后的B-和P-帧可以引用位于普通I-帧之前的I-帧。从随机存取的视频流中，播放器永远可以从一个IDR帧播放，因为在它之后没有任何帧引用之前的帧。但是，不能在一个没有IDR帧的视频中从任意点开始播放，因为后面的帧总是会引用前面的帧 。

  收到 IDR 帧时，解码器另外需要做的工作就是：把所有的 PPS 和 SPS 参数进行更新。

  对IDR帧的处理(与I帧的处理相同)：(1) 进行帧内预测，决定所采用的帧内预测模式。(2) 像素值减去预测值，得到残差。(3) 对残差进行变换和量化。(4) 变长编码和算术编码。(5) 重构图像并滤波，得到的图像作为其它帧的参考帧。

P帧:前向预测编码帧

    在针对连续动态图像编码时，将连续若干幅图像分成P,B,I三种类型，P帧由在它前面的P帧或者I帧预测而来，它比较与它前面的P帧或者I帧之间的相同信息或数据，也即考虑运动的特性进行帧间压缩。P帧法是根据本帧与相邻的前一帧（I帧或P帧）的不同点来压缩本帧数据。采取P帧和I帧联合压缩的方法可达到更高的压缩且无明显的压缩痕迹。

P帧的预测与重构:P帧是以I帧为参考帧，在I帧中找出P帧“某点”预测值和运动矢量，取预测差值和运动矢量一起传送。在接收端根据运动矢量从I帧中找出P帧“某点”的预测值并与差值相加以得到P帧某点样值，从而可得到完整的P帧。

有的视频序列比较简单，就没有B帧，

B帧：双向预测内插编码帧

B帧的预测与重构

 B帧法是双向预测的帧间压缩算法。当把一帧压缩成B帧时，它根据相邻的前一帧、本帧以及后一帧数据的不同点来压缩本帧，也即仅记录本帧与前后帧的差值。只有采用B帧压缩才能达到200：1的高压缩。

 B帧是以前面的I或P帧和后面的P帧为参考帧，找出B帧“某点”的预测值和两个运动矢量，并取预测差值和运动矢量传送。接收端根据运动矢量在两个参考帧中。


=======
CBR（Constant Bit Rate）是以恒定比特率方式进行编码，有Motion发生时，由于码率恒定，只能通过增大QP来减少码字大小，图像质量变差，当场景静止时，图像质量又变好，因此图像质量不稳定。这种算法优先考虑码率(带宽)。

这个算法也算是码率控制最难的算法了，因为无法确定何时有motion发生，假设在码率统计窗口的最后一帧发生motion，就会导致该帧size变大，从而导致统计的码率大于预设的码率，也就是说每秒统计一次码率是不合理的，应该是统计一段时间内的平均码率，这样会更合理一些。

 

VBR（Variable Bit Rate）动态比特率，其码率可以随着图像的复杂程度的不同而变化，因此其编码效率比较高，Motion发生时，马赛克很少。码率控制算法根据图像内容确定使用的比特率，图像内容比较简单则分配较少的码率(似乎码字更合适)，图像内容复杂则分配较多的码字，这样既保证了质量，又兼顾带宽限制。这种算法优先考虑图像质量。

 

CVBR（Constrained VariableBit Rate）,这样翻译成中文就比较难听了，它是VBR的一种改进方法。但是Constrained又体现在什么地方呢？这种算法对应的Maximum bitRate恒定或者Average BitRate恒定。这种方法的兼顾了以上两种方法的优点：在图像内容静止时，节省带宽，有Motion发生时，利用前期节省的带宽来尽可能的提高图像质量，达到同时兼顾带宽和图像质量的目的。这种方法通常会让用户输入最大码率和最小码率，静止时，码率稳定在最小码率，运动时，码率大于最小码率，但是又不超过最大码率。比较理想的模型如下：





ABR (Average Bit Rate) 在一定的时间范围内达到设定的码率，但是局部码率峰值可以超过设定的码率，平均码率恒定
--------------------- 
作者：szfhy 
来源：CSDN 
原文：https://blog.csdn.net/szfhy/article/details/50820119 
版权声明：本文为博主原创文章，转载请附上博文链接！
>>>>>>> e756928a7ce34a45b6b84dc98ef77790a2bf6b7c
