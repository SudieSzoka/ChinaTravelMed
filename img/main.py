import os
from PIL import Image

def convert_images_to_webp(source_dir, target_dir):
    # 确保目标目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 遍历源目录下的文件
    for filename in os.listdir(source_dir):
        # 检查文件是否为.jpg或.png
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 构建完整的文件路径
            source_path = os.path.join(source_dir, filename)
            # 新的文件名，替换扩展名为.webp
            base_name = os.path.splitext(filename)[0]
            target_filename = f"{base_name}.webp"
            target_path = os.path.join(target_dir, target_filename)
            
            try:
                # 打开图片并转换为webp
                with Image.open(source_path) as img:
                    img.save(target_path, "WEBP")
                print(f"Converted {filename} to {target_filename}")
            except IOError as e:
                print(f"Cannot convert {filename}: {e}")

# 当前工作目录
current_dir = os.getcwd()
# 目标目录为当前目录下的'144'文件夹
target_folder = os.path.join(current_dir, "webp")

# 调用函数执行转换
convert_images_to_webp(current_dir, target_folder)