**MP4格式分析**                  

　　**MP4**(MPEG-4 Part 14)是一种常见的多媒体容器格式，它是在“ISO/IEC 14496-14”标准文件中定义的，属于MPEG-4的一部分，是“ISO/IEC 14496-12(MPEG-4 Part 12 ISO base media file format)”标准中所定义的媒体格式的一种实现，后者定义了一种通用的媒体文件结构标准。MP4是一种描述较为全面的容器格式，被认为可以在其中嵌入任何形式的数据，各种编码的视频、音频等都不在话下，不过我们常见的大部分的MP4文件存放的**AVC(H.264)**或**MPEG-4(Part 2)**编码的视频和**AAC**编码的音频。MP4格式的官方文件后缀名是“.mp4”，还有其他的以mp4为基础进行的扩展或者是缩水版本的格式，包括：**M4V**,  **3GP**, **F4V**等。

　　mp4是由一个个“box”组成的，大box中存放小box，一级嵌套一级来存放媒体信息。box的基本结构是：

![img](https://ask.qcloudimg.com/http-save/yehe-2041299/l0mqkrl2mz.jpeg?imageView2/2/w/1620)

　　其中，size指明了整个box所占用的大小，包括header部分。如果box很大(例如存放具体视频数据的mdat box)，超过了uint32的最大数值，size就被设置为1，并用接下来的8位uint64来存放大小。

典型结构：

![img](https://upload-images.jianshu.io/upload_images/691344-3984e8f384d31dd5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)



　一个mp4文件有可能包含非常多的box，在很大程度上增加了解析的复杂性，这个网页上<http://mp4ra.org/atoms.html>记录了一些当前注册过的box类型。看到这么多box，如果要全部支持，一个个解析，怕是头都要爆了。还好，大部分mp4文件没有那么多的box类型，下图就是一个简化了的，常见的mp4文件结构：

![img](https://ask.qcloudimg.com/http-save/yehe-2041299/9tocuugcm9.jpeg?imageView2/2/w/1620)

一般来说，解析媒体文件，最关心的部分是视频文件的宽高、时长、码率、编码格式、帧列表、关键帧列表，以及所对应的时戳和在文件中的位置，这些信息，在mp4中，是以特定的算法分开存放在stbl box下属的几个box中的，需要解析stbl下面所有的box，来还原媒体信息。下表是对于以上几个重要的box存放信息的说明：

![img](https://ask.qcloudimg.com/http-save/yehe-2041299/cu848vtmsi.jpeg?imageView2/2/w/1620)

MP4的重要组成部分：

　ftyp

File Type Box，一般在文件的开始位置，描述的文件的版本、兼容协议等。

![img](https://upload-images.jianshu.io/upload_images/691344-c331c1737c53d2c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)



## moov

Movie Box，包含本文件中所有媒体数据的宏观描述信息以及每路媒体轨道的具体信息。一般位于ftyp之后，也有的视频放在文件末尾。注意，当改变moov位置时，内部一些值需要重新计算。

![img](https://upload-images.jianshu.io/upload_images/691344-e693dd87df0376b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)



## mdat

Media Data Box，存放具体的媒体数据。

![img](https://upload-images.jianshu.io/upload_images/691344-43cd3fddd5a7f93d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

# Moov Insider

mp4的媒体数据信息主要存放在Moov Box中，是我们需要分析的重点。moov的主要组成部分如下：

## mvhd

Movie Header Box，记录整个媒体文件的描述信息，如创建时间、修改时间、时间度量标尺、可播放时长等。

下图示例中，可以获取文件信息如时长为3.637秒。

![img](https://upload-images.jianshu.io/upload_images/691344-223bbfd0bb5e6847.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)



## udta

User Data Box，自定义数据。

## track

Track Box，记录媒体流信息，文件中可以存在一个或多个track，它们之间是相互独立的。每个track包含以下几个组成部分：



### tkhd

Track Header Box，包含关于媒体流的头信息。

下图示例中，可以看到流信息如视频流宽度720，长度1280。

![img](https://upload-images.jianshu.io/upload_images/691344-7c92d3906ae67fc8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

### mdia

Media Box，这是一个包含track媒体数据信息的container box。子box包括：
 mdhd：Media Header Box，存放视频流创建时间，长度等信息。
 hdlr：Handler Reference Box，媒体的播放过程信息。
 minf：Media Information Box，解释track媒体数据的handler-specific信息。minf同样是个container box，其内部需要关注的内容是stbl，这也是moov中最复杂的部分。stbl包含了媒体流每一个sample在文件中的offset，pts，duration等信息。想要播放一个mp4文件，必须根据stbl正确找到每个sample并送给解码器。
 mdia展开如下图所示：

![img](https://upload-images.jianshu.io/upload_images/691344-b2f7553df2343256.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

# Stbl Insider

Sample Table Box，上文提到mdia中最主要的部分是存放文件中每个sample信息的stbl。在解析stbl前，我们需要区分chunk和sample这两个概念。
 在mp4文件中，sample是一个媒体流的基本单元，例如视频流的一个sample代表实际的nal数据。chunk是数据存储的基本单位，它是一系列sample数据的集合，一个chunk中可以包含一个或多的sample。

![img](https://upload-images.jianshu.io/upload_images/691344-34a4543e02b31716.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/257/format/webp)

stbl用来描述每个sample的信息，包含以下几个主要的子box：

## stsd

Sample Description Box，存放解码必须的描述信息。

下图示例中，对于h264的视频流，其具体类型为`avc1`，extensions中其中存放有sps，pps等解码必要信息。

![img](https://upload-images.jianshu.io/upload_images/691344-e7e5fb42fb969d23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)



## stts

Time-to-Sample Box，定义每个sample时长。Time-To-Sample的table entry布局如下：



![img](https:////upload-images.jianshu.io/upload_images/691344-6f46180dbd69f167.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/407/format/webp)

stts table entry布局

sample count：sample个数
 sample duration：sample持续时间
 持续时间相同的连续sample可以放到一个entry里达到节省空间的目的。

下图示例中，第1个sample时间为33362微秒，第2-11个sample时间为33363微秒：

![img](https://upload-images.jianshu.io/upload_images/691344-d525cd4c99f0fc40.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)



## stss

Sync Sample Box，同步sample表，存放关键帧列表，关键帧是为了支持随机访问。
 stss的table entry布局如下：



![img](https:////upload-images.jianshu.io/upload_images/691344-0660a94c953dc244.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/291/format/webp)

stss table entry布局

下图示例中，该视频track只有一个关键帧即第1帧：



![img](https:////upload-images.jianshu.io/upload_images/691344-7672bf51ccc08844.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

stss内容

## stsc

Sample-To-Chunk Box，sample-chunk映射表。上文提到mp4通常把sample封装到chunk中，一个chunk可能会包含一个或者几个sample。Sample-To-Chunk Atom的table entry布局如下图所示：



![img](https:////upload-images.jianshu.io/upload_images/691344-d7fa9e8008394215.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/634/format/webp)

stsc table entry布局

First chunk：使用该表项的第一个chunk序号
 Samples per chunk：使用该表项的chunk中包含有几个sample
 Sample description ID：使用该表项的chunk参考的stsd表项序号

下图示例中，可以看到该视频track一共有两个stsc表项，chunk序列1-108，每个chunk包含一个sample，chunk序列109开始，每个chunk包含两个sample。



![img](https:////upload-images.jianshu.io/upload_images/691344-2c0d13e518997c1c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

stsc内容

## stsz

Sample Size Box，指定了每个sample的size。Sample Size Atom包含两sample总数和一张包含了每个sample size的表。
 sample size 表的entry布局如下图：



![img](https:////upload-images.jianshu.io/upload_images/691344-9e2f454fbfa4b29f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/287/format/webp)

stsz table entry布局

下图示例中，该视频流一共有110个sample，第1个sample大小为42072字节，第2个sample大小为7354个字节。



![img](https:////upload-images.jianshu.io/upload_images/691344-cef3e59d586bb21d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

stsz内容

## stco

Chunk Offset Box，指定了每个chunk在文件中的位置，这个表是确定每个sample在文件中位置的关键。该表包含了chunk个数和一个包含每个chunk在文件中偏移位置的表。每个表项的内存布局如下：



![img](https:////upload-images.jianshu.io/upload_images/691344-030aa800f98835fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/267/format/webp)

stco table entry布局

需要注意，这里stco只是指定的每个chunk在文件中的偏移位置，并没有给出每个sample在文件中的偏移。想要获得每个sample的偏移位置，需要结合 Sample Size box和Sample-To-Chunk 计算后取得。

下图示例中，该视频流第1个chunk在文件中的偏移为4750，第1个chunk在文件中的偏移为47007。



![img](https:////upload-images.jianshu.io/upload_images/691344-1f740030a6f46c91.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

stco内容

# 如何计算sample偏移位置

上文提到通过stco并不能直接获取某个sample的偏移位置，下面举例说明如何获取某一个pts对应的sample在文件中的位置。大体需要以下步骤：

- 1.将pts转换到媒体对应的时间坐标系
- 2.根据stts计算某个pts对应的sample序号
- 3.根据stsc计算sample序号存放在哪个chunk中
- 4.根据stco获取对应chunk在文件中的偏移位置
- 5.根据stsz获取sample在chunk内的偏移位置并加上第4步获取的偏移，计算出sample在文件中的偏移

例如，想要获取3.64秒视频sample数据在文件中的位置：

- 1.根据time scale参数，将3.64秒转换为视频时间轴对应的3640000
- 2.遍历累加下表所示stts所有项目，计算得到3640000位于第110个sample

```
type    stts
size    224
flags   0
version 0
sample_counts   1,10,1,1,11,1,1,2,1,25,1,1,1,17,1,10,1,1,1,7,1,1,1,1,10,1
sample_deltas   33362,33363,33362,33364,33363,33362,33364,33363,33362,33363,33362,33364,33362,33363,33362,33363,33362,33364,33362,33363,33362,33364,33363,33362,33363,0
```

- 3.查询下表所示stsc所有项目，计算得到第110个sample位于第109个chunk，并且在该chunk中位于第2个sample

```
type    stsc
size    40
flags   0
version 0
first_chunk 1,109
samples_per_chunk   1,2
sample_description_index    1,1
```

- 4.查询下表所示stco所有项目，得到第109个chunk在文件中偏移位置为1710064

```
Property name   Property value
type    stco
size    452
flags   0
version 0
chunk_offsets   4750,47007,54865,61967,75519,88424,105222,117892,133730,149529,165568,182034,194595,210776,225470,240756,255358,270711,285459,300135,315217,330899,347372,363196,376409,394509,407767,424615,438037,455603,469784,487287,505197,519638,536714,553893,567187,584744,599907,615298,630669,645918,662605,678655,693510,708980,724061,738946,754170,771520,787233,800847,816997,832490,847814,862559,877929,898379,911054,925810,943883,956497,974403,991527,1009478,1025198,1041806,1062609,1078401,1091360,1105142,1118748,1132815,1145281,1156966,1171871,1186742,1202760,1218235,1236688,1249330,1263163,1280880,1297903,1313162,1332885,1345726,1359017,1376283,1391401,1405512,1419550,1433644,1452103,1475241,1492689,1511291,1522606,1535368,1559413,1575331,1588853,1609829,1626623,1642798,1658640,1674160,1693972,1710064
```

- 5.查询下表所示stsz所有项目，得到第109个sample的size为14808。计算得到3.64秒视频sample数据在文件中
   offset：1710064+14808 = 1724872
   size：17930

```
type    stsz
size    460
flags   0
version 0
sample_sizes    42072,7354,6858,13110,12684,16416,12490,15497,15630,15865,16116,12387,15775,14519,14929,14433,15181,14390,14496,14717,15507,16101,15643,12843,17911,13070,16455,13221,17186,14002,17139,17737,14251,16708,16999,12911,17356,14801,15213,15016,15062,16505,15689,14657,15053,14907,14527,15048,17161,15308,13432,15777,15307,14971,14568,14987,20264,12494,14382,17873,12235,17718,16770,17766,15366,16420,20623,15403,12761,13394,13390,13714,12295,11505,14541,14689,15635,15291,18091,12458,13645,17346,16847,14902,19530,12446,13105,16872,14937,13944,13657,13908,18092,22959,17080,18421,11129,12400,23844,15564,13340,20603,16609,15984,15474,15339,19451,15719,14808,17930
sample_size 0
sample_count    110
```

- 验证：用编辑器打开mp4文件，定位到文件偏移1724872位置，前4字节值为0x00004606。在avcc中一个sample的前4个字节代表这个包的大小，转换为十进制是17926，正好等于17930减去四个长度字节。

  

  ![img](https:////upload-images.jianshu.io/upload_images/691344-50d5823d9c76b855.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

  image.png





看吧，要获取到mp4文件的帧列表，还挺不容易的，需要一层层解析，然后综合stts stsc stsz stss stco等这几个box的信息，才能还原出帧列表，每一帧的时戳和偏移量。而且，你要照顾可能出现或者可能不出现的那些box。。。可以看的出来，mp4把帧sample进行了分组，也就是chunk，需要间接的通过chunk来描述帧，这样做的理由是可以压缩存储空间，缩小媒体信息所占用的文件大小。这里面，stsc box的解析相对来说比较复杂，它用了一种巧妙的方式来说明sample和chunk的映射关系，特别介绍一下。

![img](https://ask.qcloudimg.com/http-save/yehe-2041299/twptwiotex.jpeg?imageView2/2/w/1620)

这是stsc box的结构，前几项的意义就不解释了，可以看到stsc box里每个entry结构体都存有三项数据，它们的意思是：“从**first_chunk**这个chunk序号开始，每个chunk都有**samples_per_chunk**个数的sample，而且每个sample都可以通过**sample_description_index**这个索引，在stsd box中找到描述信息”。也就是说，每个entry结构体描述的是一组chunk，它们有相同的特点，那就是每个chunk包含**samples_per_chunk**个sample，好，那你要问，这组相同特点的chunk有多少个？请通过下一个entry结构体来推算，用下一个entry的**first_chunk**减去本次的**first_chunk**，就得到了这组chunk的个数。最后一个entry结构体则表明从该**first_chunk**到最后一个chunk，每个chunk都有**sampls_per_chunk**个sample。很拗口吧，不过，就是这个意思**:)**。由于这种算法无法得知文件所有chunk的个数，所以你必须借助于stco或co64。直接上代码可能会清楚些：

这是stsc box的结构，前几项的意义就不解释了，可以看到stsc box里每个entry结构体都存有三项数据，它们的意思是：“从**first_chunk**这个chunk序号开始，每个chunk都有**samples_per_chunk**个数的sample，而且每个sample都可以通过**sample_description_index**这个索引，在stsd box中找到描述信息”。也就是说，每个entry结构体描述的是一组chunk，它们有相同的特点，那就是每个chunk包含**samples_per_chunk**个sample，好，那你要问，这组相同特点的chunk有多少个？请通过下一个entry结构体来推算，用下一个entry的**first_chunk**减去本次的**first_chunk**，就得到了这组chunk的个数。最后一个entry结构体则表明从该**first_chunk**到最后一个chunk，每个chunk都有**sampls_per_chunk**个sample。很拗口吧，不过，就是这个意思**:)**。由于这种算法无法得知文件所有chunk的个数，所以你必须借助于stco或co64。

直接上代码可能会清楚些：

![img](https://ask.qcloudimg.com/http-save/yehe-2041299/yqontf9zux.jpeg?imageView2/2/w/1620)



