# robot-wechat

## 依赖
本程序使用python3，请在python3环境下运行
#### Python 3
- PIL: pip3 install pillow
- pyecharts：pip3 install pyecharts
- pip3 install itchat
- pip3 install jieba

地图数据包：  
pip3 install echarts-china-provinces-pypkg  
pip3 install echarts-countries-pypkg

## 运行
#### 获取用户信息
    需要将get_user_info.py第73行的指定昵称，改成随意一个好友的名字,自我发送不起效，做了限制可以移除，页面有注释。 
    ```
    python3 get_user_info.py
    ```
    执行后会在data目录下生成friends.json
    会在images目录下存放所有好友的头像，已注释此功能，开启会导致启动慢。

#### 统计用户信息，后续增加
python3 analyse.py
会在analyse文件夹下生产合成后的图片以及可视化的文件
