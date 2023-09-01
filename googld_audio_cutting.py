from google.cloud import vision
import pandas as pd

# 设置Google Cloud Vision凭证的路径
credential_path = r'C:\Users\Administrator\Desktop/resolute-radar-397710-c11161370c00.json'
# 设置要识别的图片路径
image_path = r'C:\Users\Administrator\Desktop/11.png'

# 初始化Google Cloud Vision客户端
client = vision.ImageAnnotatorClient.from_service_account_json(credential_path)

# 读取图片文件
with open(image_path, 'rb') as image_file:
    content = image_file.read()

# 创建图像对象
image = vision.Image(content=content)

# 使用OCR进行图像文本识别
response = client.text_detection(image=image)
texts = response.text_annotations

# 将识别到的文本提取成表格数据
rows = []
for text in texts[1:]:
    description = text.description.strip()
    rows.append({'Text': description})

# 创建表格数据结构
df = pd.DataFrame(rows)

# 保存为CSV文件
df.to_csv('output.csv', index=False)