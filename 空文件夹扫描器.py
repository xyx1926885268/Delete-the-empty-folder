import os
import threading
from datetime import datetime
from time import strftime
from time import gmtime
lists=[]
ls=[]
fp=open("folder.log","w+")
times=0
def scanFile(filePath):
	for	path in os.walk(filePath):
		lists.append(path[0])
	for i in lists:
		try:
			if len(os.listdir(i))!=0:
				continue
			else:
				ls.append(i)
		except:
			continue
	for m in range(len(ls)):
		for x in ls:
			os.rmdir(ls[m])
			with open("folder.log","a+") as f:
				data =ls[m]
				f.write(data)
				f.write('\n')
			print(datetime.now(),"正在删除",ls[m])
			ls.clear()
			scanFile(filePath)
if __name__ == '__main__':
	filePath=input("请输入想扫描的路径：")
	start_time=datetime.now()
# 	for y in range(5):#开启5条线程
# 		s = threading.Thread(target=scanFile(filePath))
# 		s.start()
	scanFile(filePath)
	end_time=datetime.now()
	times=end_time-start_time
	print("共花费了",times,"s")
	print("删除完成")
	os.system("pause")