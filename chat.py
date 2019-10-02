
#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:	#用 for 迴圈 讀取 f 每一行叫做一個 line
			lines.append(line.strip())  #把檔案每一行裝進 lines 清單 strip清除換行符號
	return lines #把 lines 這個清單回傳出來 


#convert 轉換
def convert(lines):
	new = [] 
	person = None  #預設值設定為 None ＝ 無
	for line in lines:
		if line == 'Allen':
			person = 'Allen' #把 Allen 暫存到 person
			continue 
		elif line == 'Tom':
			person = 'Tom'
			continue		
		if person:
			new.append(person + ': ' + line) # person 人名
	return new

#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt') #投入參數後 filename 就會轉換成參數可以隨意讀取各種檔案
	lines = convert(lines) #把上一個 lines 轉換完後在存回 lines
	write_file('output.txt', lines) 

main()

