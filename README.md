# WeCom
企业微信通知PY文件

## 操作步骤
### 第一步：添加群机器人

1. 打开企业微信 PC 端或网页版。
2. 进入你想发送通知的群聊。
3. 点击右上角【群设置】。
4. 下拉点击【群机器人】。
5. 点击【添加机器人】 → 选择【自定义】。
6. 填写机器人名称和头像（可自定义）。
7. 完成后会生成一个 Webhook 地址，类似于：
`https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
8. 复制此链接，保存备用。

### 第二步：设置定时任务
1. 打开终端，运行：
`crontab -e`
2. 添加以下行（表示每周一到周五 17:00 执行脚本）：
`0 17 * * 1-5 /usr/bin/python3 /Users/你用户名/路径/wechat_notify.py`可以直接拖动文件到终端显示路径，注意**/python3 **后面有一个空格
> 使用 which python3 查看你 Python 的路径

### 第三步：安装 requests 模块
1. 打开 终端
2.运行以下命令（确保是你实际使用的 Python 版本）：
`python3 -m ensurepip --upgrade`
`python3 -m pip install requests`

### 第三步：编辑 crontab 模块 （注意切换英文）
`crontab -l` 查看当前任务列表
`crontab -e` 打开编辑列表
`i` 开始编辑
先按esc再`:wq`退出编辑
`:q!`强制退出不保存


