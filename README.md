# 广东理工学院-宿舍电表数据
通过小程序接口, 拉取高要校区宿舍电费信息 的python脚本.抄表间隔很长, 没必要每秒拉取. 推荐间隔30分钟~1小时一次, 请勿滥用接口

## 使用
- ### import导入 GetRoomInfo(Roomname) 返回字典Dictionary
	```python
	import power_get.py

	data = power_get.GetRoomInfo("16621")
	if data['state']=='ok':   #建议判断返回状态是否ok再往下执行
	```

- ### 可直接执行 返回json 可同时获取多个宿舍
	```Shell
	python3 power_get.py 16621 16612 17101
	```
	```json
	{"state": "ok", "name": "16621", "Used": "8172.41", "Remaining": "16.62", "RecordTime": "2021/6/30 14:02:56", "TimeStamp": "1625032976"}
	{"state": "ok", "name": "16612", "Used": "8683.05", "Remaining": "42.48", "RecordTime": "2021/6/30 14:30:21", "TimeStamp": "1625034621"}
	{"state": "ok", "name": "17101", "Used": "5210.76", "Remaining": "20.60", "RecordTime": "2021/6/30 13:51:28", "TimeStamp": "1625032288"}
	```
## 贡献
学校有新建宿舍楼, 如不支持你所在的宿舍楼. 可以 [提交 issue](https://github.com/Moeyuuko/gdlgxy-ElecMeter/issues/new) 或自行 fork 修改后提交 pull request。
如果你要提交 pull request，请确保你的代码风格和项目已有的代码保持一致, 谢谢!