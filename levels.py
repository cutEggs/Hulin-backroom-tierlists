import os
from PIL import Image, ImageDraw, ImageFont

raw_levels = [
    "0", "0.01", "1", "1.5", "4", "5", "6", "6.2", "10", "10.1", "11", "13", "14", "28", "37", "37.2", "51", "68", "7.77", "83.1", "87", "197", "305", "330", "400", "483", "499", "590", "626.2", "995", "193", "810", "0.41", "2", "300", "19", "20", "4.3", "109", "0.7", "LX", "16", "335", "7", "47", "188", "27", "25", "870", "21", "161", "161.1", "8", "64", "9", "595", "399", "154", "72", "73", "146", "11.3", "11.11", "10.4", "194", "35", "36", "159", "699", "37.1", "666", "45", "312", "369", "3", "18.1", "89", "52", "142", "Fun", "799", "345", "94", "587", "91", "859", "85", "92", "5.1", "626", "38", "108", "0.5", "0.99", "611", "12", "0.2", "909", "927", "39", "9.31", "398", "214", "770", "0.02", "747", "238", "913", "427", "437", "413", "0.66", "26.1", "356", "43", "332", "948", "993", "412", "90", "70", "9.1", "118", "0.22", "24", "66", "3.1", "188.8", "880", "404", "54", "700", "37.6", "49", "14.2", "15", "483.5", "7.1", "37.9", "6.5", "69", "211", "355", "321", "143", "34", "84", "540", "690", "9.99", "396", "1000", "101", "17", "986", "154.1", "346", "0.11", "399.1", "63", "!", "306", "27.3", "198", "397", "154.1", "31", "33", "14.1", "140", "133", "7.7", "797", "722", "7.1", "711", "271", "1.01", "19.2", "1+",
    "The Void", "The Hub", "The End", "S.Horizon", "10.99", "960"
]

def sort_key(item):
    try:
        return (0, float(item))
    except ValueError:
        return (1, item)

unique_levels = sorted(list(set(raw_levels)), key=sort_key)

output_dir = "backrooms_tier_images"
os.makedirs(output_dir, exist_ok=True)

width, height = 300, 300
bg_color = (0, 0, 0)
text_color = (255, 0, 255)

font_path = "C:/Windows/Fonts/consola.ttf" 
font_size = 48

try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    font = ImageFont.load_default()
    print("警告：找不到指定字型路徑，已使用預設字型。")

special_names = {"The Void", "The Hub", "The End", "S.Horizon"}

for name in unique_levels:
    if name in special_names:
        display_text = name
    else:
        display_text = f"Level {name}"

    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    bbox = draw.textbbox((0, 0), display_text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    x = (width - w) / 2
    y = (height - h) / 2

    draw.text((x, y), display_text, fill=text_color, font=font)

    safe_filename = name.replace("!", "excl").replace("+", "plus").replace(".", "d")
    img.save(os.path.join(output_dir, f"{safe_filename}.png"))

print(f"更新完成！圖片已儲存至 '{output_dir}' 資料夾。")