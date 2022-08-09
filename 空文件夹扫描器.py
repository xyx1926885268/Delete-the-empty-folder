import os
import threading
from datetime import datetime
lists=[]
ls=[]
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
			print(datetime.now(),"正在删除",ls[m])
			ls.clear()
			scanFile(filePath)
if __name__ == '__main__':
	filePath=input("请输入想扫描的路径：")
	for y in range(5):#开启5条线程
		t1 = threading.Thread(target=scanFile(filePath))
		t1.start()
	# 	scanFile(filePath)
	print("删除完成")
	os.system("pause")