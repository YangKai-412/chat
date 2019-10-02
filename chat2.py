
#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:	#用 for 迴圈 讀取 f 每一行叫做一個 line
			lines.append(line.strip())  #把檔案每一行裝進 lines 清單 
	return lines #把 lines 這個清單回傳出來 

#convert 轉換
def convert(lines): 
	end = []
	person = None  #預設值設定為 None ＝ 無
	Allen_word_count = 0 #Allen_字_計數
	Viki_word_count = 0  #Viki_字_計數
	Allen_sticker_count = 0 #Allen_貼圖_計數
	Viki_sticker_count = 0  #Viki_貼圖_計數
	Allen_image_count = 0 #Allen_圖片_計數
	Viki_image_count = 0  #Viki_圖片_計數
	for line in lines:
		s = line.split(' ') #使用 line(字串) 裡面的 split(分割)
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				Allen_sticker_count += 1 #sticker(貼圖)
			elif s[2] == '圖片':			 
				Allen_image_count += 1   #image(圖片)
			else:						 
				for m in s[2:]:
					Allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count += 1 
			elif s[2] == '圖片':
				Viki_image_count += 1
			else:
				for m in s[2:]:
					Viki_word_count += len(m)
	print('Allen說了', Allen_word_count, '個字')
	print('Allen傳了', Allen_sticker_count, '個貼圖')
	print('Allen傳了', Allen_image_count, '張圖片')

	print('Viki說了', Viki_word_count, '個字')
	print('Viki傳了', Viki_sticker_count, '個貼圖')
	print('Viki傳了', Viki_image_count, '張圖片')
	
	end.append(['Allen說了', Allen_word_count, '個字'])
	end.append(['Allen傳了', Allen_sticker_count, '個貼圖'])
	end.append(['Allen傳了', Allen_image_count, '張圖片'])

	end.append(['Viki說了', Viki_word_count, '個字'])
	end.append(['Viki傳了', Viki_sticker_count, '個貼圖'])
	end.append(['Viki傳了', Viki_image_count, '張圖片'])
	return end
#寫入檔案
def write_file(filename, end):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in end:
			f.write(str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '\n')

def main():
	lines = read_file('LINE-Viki.txt') #投入參數後 filename 就會轉換成參數可以隨意讀取各種檔案
	end = convert(lines) #把上一個 lines 轉換完後在存回 lines 
	write_file('output1.csv', end) 

main()

