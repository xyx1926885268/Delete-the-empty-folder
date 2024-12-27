import os
from datetime import datetime
import threading
try:
	os.remove("folder.log")
except:
	pass
lists = []
ls = []
fp = open ( "folder.log", "w+" )
times = 0

def scanFile (filePath) :
	for path in os.walk ( filePath ) :
		lists.append ( path [0] )
	for i in lists :
		try :
			if len ( os.listdir ( i ) ) != 0 :
				continue
			else :
				ls.append ( i )
		except :
			continue
	lists.clear()
	with open ( "folder.log", "a+" ) as f :
		for m in range ( len ( ls ) ) :
			for x in ls :
				os.rmdir ( ls [m] )
				f.write ( ls [m]+"\n")
				print ( datetime.now ( ), "正在删除", ls [m] )
				ls.clear ( )
				scanFile ( filePath )
				

if __name__ == '__main__' :
	filePath = input ( "请输入想扫描的路径：" )
	start_time = datetime.now ( )
	threads = []
	try :
		for y in range ( 500 ) :  # 开启5条线程
			s = threading.Thread ( target = scanFile ( filePath ) )
			threads.append ( s )
		for t in threads :
			t.start ( )
			t.join ( )
	except:
		print("线程开启失败")
	# scanFile(filePath)
	end_time = datetime.now ( )
	times = end_time - start_time
	print ( "共花费了", times, "s" )
	print ( "删除完成" )
	os.system ( "pause" )
