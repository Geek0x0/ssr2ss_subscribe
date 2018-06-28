# ssr2ss_subscribe（仅支持 iOS）
转换机场提供的 SSR 订阅到 SS 订阅（目前 Quantumult 和 Shadowrocket 均支持 SS 订阅）  
程序使用 Python2 语言，依赖于 Flask、Requests 第三方库  
使用前请先确定机场是否提供 SS 支持，并且将配置修改给 SS/SSR 可用
  
如何测试：  
1. 先将您的订阅地址写入 ssr_subscribe 中(请自定义名称)  
2. 运行 python2 app.py  
3. 在软件中添加订阅 http://your_ip/CordCloud  
