#!/usr/bin/env python3
# encoding=utf-8

import re
import sys
import os
from optparse import OptionParser

def clip_path(path):
    print("正在剪辑 " + path + "...")
    start_time = input('请输入剪切起始时间：')
    stop_time = input('请输入剪切结束时间：')
    file_dir, filename = os.path.split(path)     # 分割文件名与目录
    name, suffix = os.path.splitext(filename)    # 分离文件名与扩展名
    clips_path = os.path.join(file_dir,'clips')
    if not os.path.exists(clips_path):
        os.makedirs(clips_path)
    output_file = os.path.join(clips_path,name) + '-' + start_time + '-' + stop_time + suffix
    os.system("ffmpeg -ss {2} -to {3} -accurate_seek -i {0} -c copy -avoid_negative_ts 1 {1}".format(path,output_file,start_time,stop_time))

def clip_dir(directory):
    for root, dirs, files in os.walk(directory, topdown=True):
        for name in files:
            if (name.endswith(".mp4")): #or .avi, .mpeg, whatever.
                clip_path(os.path.join(root, name))

def process(opt):
    # clip, merge = opt.clip, opt.merge
    clip = opt.clip
    if clip:
        # clip is a file path
        if os.path.isfile(clip):
            print("下面输入的时间支持两种格式：")
            print("1. 纯数字格式，以秒为单位。如输入 60 表示视频的第 60 秒；")
            print("2. 时:分:秒格式。如输入 00:03:40 表示视频的 3 分 40 秒。\n")
            clip_path(clip)
            exit("视频剪切成功！请前往源视频目录下查看剪切的视频。")
        elif os.path.isdir(clip):
            print("下面输入的时间格式支持两种格式：")
            print("1. 纯数字格式，以秒为单位。如输入 60 表示视频的第 60 秒；")
            print("2. 时:分:秒格式。如输入 00:03:40 表示视频的 3 分 40 秒。\n")
            clip_dir(clip)
            exit("视频剪切成功！请前往源视频目录下查看剪切的视频。")
        else:
            print('输入视频读取源地址有误，请重新输入。读取源地址需要是一个文件路径或者目录。')
            exit(1)
    # elif merge:
    #     if os.path.isfile(merge):
    #     elif os.path.isdir(merge):
    #     else:
    #         print('Please specify a file path or a directory path as the argument.')
    else:
        print('请选定一个选项，执行 `covideo -h` 列出所有选项。')

def exe_main():
    parser = OptionParser(version="%prog 0.0.2")
    parser.set_defaults(verbose=True)
    parser.add_option("-c", "--clip", dest="clip", type="string",
                      help="Use this option to clip mp4 videos; receive one argument that can be a file path or a directory", metavar="CLIP")
    # parser.add_option("-m", "--merge", dest="merge", type="string",
    #                   help="Merge mp4 videos", metavar="MERGE")
    options, args = parser.parse_args()
    process(options)