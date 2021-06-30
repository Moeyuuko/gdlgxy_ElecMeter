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
	{'state': 'ok', 'name': '16621', 'Used': '8169.97', 'Remaining': '19.06', 'RecordTime': '2021/6/30 12:07:16', 'TimeStamp': '1625026036'}
	{'state': 'ok', 'name': '16612', 'Used': '8680.66', 'Remaining': '44.87', 'RecordTime': '2021/6/30 12:34:42', 'TimeStamp': '1625027682'}
	{'state': 'ok', 'name': '17101', 'Used': '5209.58', 'Remaining': '21.78', 'RecordTime': '2021/6/30 11:55:26', 'TimeStamp': '1625025326'}
	```
