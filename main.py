import speech_recognition as sr

# 创建一个 Recognizer 对象
r = sr.Recognizer()

# 读取音频文件
for i in range(1,2):
    with sr.AudioFile('C:\\Users\\Administrator\\Desktop\\3.wav') as source:
        audio = r.record(source)

    # 识别音频文件中的文字recognize_google是在线翻译（需要联网），recognize_sphinx是脱机运行（不需要联网）
    text = r.recognize_google(audio,language="zh-CN")
    print(text)




# # mp4转wav
# import os
# from ffmpy3 import FFmpeg
#
# filepath = r"E:\youtube小视频" #添加路径
# os.chdir(filepath)
# filename = os.listdir() #得到文件夹下的所有文件名称
#
# outputpath = r"E:\youtube小视频" #添加路径
# #os.mkdir(outputpath)
# os.chdir(outputpath)
#
# for i in range(len(filename)):
#     changefile = filepath+"\\"+filename[i]
#     outputfile = outputpath+"\\"+filename[i].replace('mp3','wav')
#     ff = FFmpeg(executable=r'D:\develop\python\ffmpeg-6.0-full_build\bin\ffmpeg.exe',
#             inputs={changefile: None},
#             outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'}
#             )
#     print(ff.cmd)
#     ff.run()





# # 图片文字识别1
# import pytesseract
# from PIL import Image
#
# def demo():
#     # 打开要识别的图片
#     image = Image.open(r'C:\Users\Administrator\Desktop\13.png')
#     # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
#     text = pytesseract.image_to_string(image, lang='chi_sim')
#
#     # 输入所识别的文字
#     print(text)
#
#
# if __name__ == '__main__':
#     demo()

# # 图片文字识别2
# import pytesseract
# import cv2
# import numpy as np
# from scipy import stats
# import os
# import matplotlib.pyplot as plt
#
# if __name__ == '__main__':
#     path = "C:\\Users\\Administrator\\Desktop\\cc.mp4"
#     print(path)
#     cap = cv2.VideoCapture(path)
#     frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     print(frame_count)
#     i = 0
#     # print("1")
#     while i < frame_count:
#         cap.set(cv2.CAP_PROP_POS_FRAMES, i)
#         # print("2")
#         _, frame = cap.read(i)
#         # print("3")
#         if i == 48:
#             cv2.imwrite('20210701.jpg', frame)
#             # print("4")
#         shape = frame.shape
#         # print("5")
#         print(shape)
#         # cv2.imshow("Frame-1", frame[580:630, 10:1270])
#         # print("6")
#         # img = frame[630:680, 50:1270]
#         # cv2.imshow("Frame-1", frame[890:980, 130:2200])
#         # print("6")
#         img = frame[890:980, 130:2200]
#         plt.imshow(img)
#         plt.axis("off")
#         plt.show()
#         # cv2.imshow(img)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图
#         cv2.imshow("Frame-2:Gray", img)            #显示灰度图
#         _, img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)  # 图像，阈值，映射的最大值，使用什么算法一般为cv2.thresh_binary
#         cv2.imshow("Frame-3:Binary", img)            #显示灰度图
#         word = pytesseract.image_to_string(img,lang='chi_sim')
#         print(word)
#         i = i + 24 * 2
#
#         if cv2.waitKey(10) & 0xff == ord("q"):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()


# # 图片文字识别3
# import pytesseract
# import cv2
#
# # 读取视频文件
# cap = cv2.VideoCapture('video.mp4')
#
# # 设置字幕区域
# x, y, w, h = 100, 100, 500, 300
#
# # 循环读取每一帧
# while cap.isOpened():
#     ret, frame = cap.read()
#
#     if ret:
#         # 裁剪字幕区域
#         subtitle = frame[y:y+h, x:x+w]
#
#         # 转换为灰度图像
#         gray = cv2.cvtColor(subtitle, cv2.COLOR_BGR2GRAY)
#
#         # 应用二值化
#         thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#
#         # 应用腐蚀和膨胀
#         kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
#         opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
#
#         # 识别字幕文本
#         subtitle_text = pytesseract.image_to_string(opening, lang='eng')
#
#         # 显示识别结果
#         cv2.imshow('Subtitle', opening)
#         print(subtitle_text)
#
#         # 按下q键退出
#         if cv2.waitKey(1) == ord('q'):
#             break
#     else:
#         break
#
# # 释放资源
# cap.release()
# cv2.destroyAllWindows()