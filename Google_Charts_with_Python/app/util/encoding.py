import chardet
with open("D:\Datasets\Ambition_Box_Dataset\Ambition_Box_Latest.csv", 'rb') as f:
    result = chardet.detect(f.read(10000))  # Read a chunk for detection
print(result['encoding'])
