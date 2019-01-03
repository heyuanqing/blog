实时传输控制协议（Real-time Transport Control Protocol或RTP Control Protocol或简写RTCP）
是实时传输协议（RTP）的一个姐妹协议。RTCP为RTP媒体流提供信道外（out-of-band）控制。
TCP本身并不传输数据，但和RTP一起协作将多媒体数据打包和发送。
RTCP定期在流多媒体会话参加者之间传输控制数据。RTCP的主要功能是为RTP所提供的服务质量（Quality of Service）提供反馈。

RTCP收集相关媒体连接的统计信息，例如：传输字节数，传输分组数，丢失分组数，jitter，单向和双向网络延迟等等。
网络应用程序可以利用RTCP所提供的信息试图提高服务质量，比如限制信息流量或改用压缩比较小的编解码器。
RTCP本身不提供数据加密或身份认证。SRTCP可以用于此类用途
