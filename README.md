# ssr2ss_subscribe（仅支持 iOS）
转换机场提供的 SSR 订阅到 SS 订阅（目前 Quantumult 和 Shadowrocket 均支持 SS 订阅）  
程序使用 Python2 语言，依赖于 Flask、Requests 第三方库  
使用前请先确定机场是否提供 SS 支持，并且将配置修改给 SS/SSR 可用
  
如何测试：  
1. 先将您的订阅地址写入 ssr_subscribe 中(请自定义名称)  
2. 运行 python2 app.py  
3. 在软件中添加订阅 http://your_ip/CordCloud  

增加公共转换服务：
目前仅支持两家机场 CordCloud 和 SSRCloud  
如何使用：  
CordCloud: 订阅地址为 http://convertsubscribe.applinzi.com/CordCloud/your_link_key  
SSRCloud: 订阅地址为 http://convertsubscribe.applinzi.com/SSRCloud/your_link_key  
通过以上订阅地址进行订阅后得到SSR 转 SS 订阅  

如何获取link_key：  
CordCloud：订阅连接为 https://www.cordcloud.me/link/SSNNCCDD12EEFF?mu=0 则 Key SSNNCCDD12EEFF  
SSRCloud：订阅连接为 https://mikucloud.ml/link/AABBCCDD12EEFF?mu=0 则 Key 为AABBCCDD12EEFF
