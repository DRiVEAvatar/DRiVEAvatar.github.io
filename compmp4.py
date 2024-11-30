import os
import subprocess

def compress_video(input_file, output_file):
    # 使用 ffmpeg 压缩视频文件
    command = [
        'ffmpeg',
        '-i', input_file,  # 输入文件
        '-vcodec', 'libx264',  # 设置视频编解码器
        '-crf', '28',  # 压缩质量控制，数值越高压缩越大，质量越差
        '-preset', 'fast',  # 压缩速度设置（fast 是折衷，适合一般需求）
        '-acodec', 'aac',  # 设置音频编解码器
        '-b:a', '192k',  # 设置音频比特率
        output_file  # 输出文件
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def compress_directory(directory):
    # 遍历目标目录及其子目录
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp4'):  # 只处理 MP4 格式的视频文件
                input_file = os.path.join(root, file)
                output_file = os.path.join(root, f"compressed_{file}")
                print(f"Compressing: {input_file}")
                compress_video(input_file, output_file)
                print(f"Compressed video saved as: {output_file}")

if __name__ == "__main__":
    target_directory = "/Users/yisuanwang/Developer/DRiVEAvatar.github.io/static/images/Anypose_anime_inputs"  # 替换为目标目录路径
    compress_directory(target_directory)
