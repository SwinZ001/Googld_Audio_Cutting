import subprocess
import os
dir_path= r'C:\Users\Administrator\Desktop\wav05\cc.mp4'
path = r'C:\Users\Administrator\Desktop\wav05'  # 待切割视频存储目录
video_list = os.listdir(path)
delta_X = 10  # 每10s切割
save_path = r'C:\Users\Administrator\Desktop\save'
mark = 0


# 获取视频的时长
def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return float(result.stdout)


for file_name in video_list:
    # file_name视频的分钟数
    # min = int(get_length(os.path.join(path, file_name))) // 60
    # file_name视频的秒数
    # second = int(get_length(os.path.join(path, file_name))) % 60
    # 获取视频总时长（秒）
    min = int(get_length(os.path.join(path, file_name)))
    # 获取文件大小M
    dir_size = os.path.getsize(dir_path)
    # dir_size = os.path.getsize(dir_path)/1024/1024
    # 视频分成多少个20m(四舍五入保留一位小数)
    dir_segmentation_size = int(dir_size/20971520)
    # 求出20m的视频多少秒（求出切割间隔）(四舍五入保留一位小数)
    min_segmentation = int(min/dir_segmentation_size)
    print(dir_segmentation_size,min_segmentation,)

    for i in range(0,int(dir_segmentation_size)+1):
        print(str(i*min_segmentation), str((i+1)*min_segmentation))
        command = 'ffmpeg -i C:\\Users\\Administrator\\Desktop\\wav05\\cc.mp4 -ss ' + str(i*min_segmentation) + ' -to ' + str((i+1)*min_segmentation) + ' -strict -2 C:\\Users\\Administrator\\Desktop\\wav05\\' + str(i) + '.mp4'
        os.system(command)










    # for i in range(min + 1):
    #     if second >= delta_X:  # 至少保证一次切割
    #         start_time = 0
    #         end_time = start_time + delta_X
    #         for j in range((second // 10) + 1):
    #             min_temp = str(i)
    #             start = str(start_time)
    #             end = str(end_time)
    #             # crop video
    #             # 保证两位数
    #             if len(str(min_temp)) == 1:
    #                 min_temp = '0' + str(min_temp)
    #             if len(str(start_time)) == 1:
    #                 start = '0' + str(start_time)
    #             if len(str(end_time)) == 1:
    #                 end = '0' + str(end_time)
    #
    #             # 设置保存视频的名字
    #             if len(str(mark)) < 6:
    #                 name = '0' * (6 - len(str(mark)) - 1) + str(mark)
    #             else:
    #                 name = str(mark)
    #             command = 'ffmpeg -i {} -ss 00:{}:{} -to 00:{}:{} -strict -2 {}'.format(os.path.join(path, file_name),
    #                                                                                     min_temp, start, min_temp, end,
    #                                                                                     os.path.join(save_path,
    #                                                                                                  'id' + str(
    #                                                                                                      name)) + '.mp4')
    #             mark += 1
    #             os.system(command)
    #             if i != min or (i == min and (end_time + delta_X) < second):
    #                 start_time += delta_X
    #                 end_time += delta_X
    #             elif (end_time + delta_X) <= second:
    #                 start_time += delta_X
    #                 end_time += delta_X
    #             elif (end_time + delta_X) > second:  # 最后不足delta_X的部分会被舍弃
    #                 break
