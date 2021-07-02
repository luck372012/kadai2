import csv
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=[]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
  
    if word in source:
        print("{}が見つかりした".format(word))
        return
    print("{}が見つかりません".format(word))
    source.append(word)
    print(source)

# dataを読み込み
def read_csv(csv_path,source):
    
    with open("./data.csv") as f:
       l_strip = [s.strip() for s in f.readlines()]
       source.extend(l_strip)      
    return source

# data1csvに書き込み
def wrire_csv():

    with open("utf8.data1.csv", mode="w", encoding='utf8') as f:
       writer = csv.writer(f)
       writer.writerow(source)
      
if __name__ == "__main__":
    read_csv("csv_path",source)
    search() 
    wrire_csv() 