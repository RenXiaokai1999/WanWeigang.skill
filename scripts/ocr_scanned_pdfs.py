"""
扫描版PDF OCR处理脚本
目标：将无书名号资料_分卷01-08.pdf 转为可读 Markdown
工具：rapidocr_onnxruntime + Pillow（内嵌JPEG提取，无需poppler）
用法：python ocr_scanned_pdfs.py [分卷编号，如1或all]
"""
import sys, io, os, re
import numpy as np
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

SOURCE_DIR = "H:/environment/claude prj/万维刚skill/万维刚精英日课一二三四五六季pdf markdown"
OUTPUT_DIR = "C:/Users/11789/.claude/skills/万维钢-perspective/references/sources/articles"

def extract_jpegs_from_pdf(pdf_path, min_size=50000):
    """从PDF中提取内嵌JPEG图像（不需要poppler）"""
    with open(pdf_path, 'rb') as f:
        data = f.read()
    jpegs = []
    pos = 0
    while True:
        idx = data.find(b'\xff\xd8\xff', pos)
        if idx == -1:
            break
        end = data.find(b'\xff\xd9', idx + 3)
        if end == -1:
            pos = idx + 3
            continue
        size = end - idx + 2
        if size >= min_size:
            jpegs.append(data[idx:end+2])
        pos = end + 2
    return jpegs

def ocr_long_image(img_bytes, ocr_engine, chunk_height=1500, overlap=100):
    """对长图进行分块OCR，返回完整文本"""
    img = Image.open(io.BytesIO(img_bytes))
    w, h = img.size
    all_text = []
    prev_last_line = ""

    for start_y in range(0, h, chunk_height - overlap):
        end_y = min(start_y + chunk_height, h)
        chunk = img.crop((0, start_y, w, end_y))
        chunk_np = np.array(chunk)
        result, _ = ocr_engine(chunk_np)
        if result:
            lines = [r[1].strip() for r in result if r[1].strip()]
            # 去重：避免重叠区域产生重复行
            if prev_last_line and lines and lines[0] == prev_last_line:
                lines = lines[1:]
            all_text.extend(lines)
            if lines:
                prev_last_line = lines[-1]

    return "\n".join(all_text)

def process_volume(vol_num):
    """处理单个分卷"""
    fname = f"无书名号资料_分卷0{vol_num}.pdf"
    pdf_path = os.path.join(SOURCE_DIR, fname)
    if not os.path.exists(pdf_path):
        print(f"[跳过] 文件不存在: {fname}")
        return

    out_path = os.path.join(OUTPUT_DIR, f"无书名号资料_分卷0{vol_num}_ocr.md")
    if os.path.exists(out_path):
        print(f"[跳过] 已存在OCR结果: {out_path}")
        return

    print(f"\n处理 {fname}...")
    jpegs = extract_jpegs_from_pdf(pdf_path)
    print(f"  提取到 {len(jpegs)} 张图像")

    ocr = RapidOCR()
    all_articles = []

    for i, jpeg_bytes in enumerate(jpegs):
        print(f"  OCR图像 {i+1}/{len(jpegs)}...", end="", flush=True)
        try:
            text = ocr_long_image(jpeg_bytes, ocr)
            if text.strip():
                all_articles.append(f"\n---\n<!-- 图像 {i+1} -->\n{text}")
                print(f" {len(text)}字")
            else:
                print(" (空)")
        except Exception as e:
            print(f" 错误: {e}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(f"# 无书名号资料 分卷0{vol_num} OCR结果\n\n")
        f.write(f"来源：{fname}\n")
        f.write(f"图像数：{len(jpegs)}\n\n")
        f.write("\n".join(all_articles))

    print(f"  完成 → {out_path}")

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "all"
    if arg == "all":
        for i in range(1, 9):
            process_volume(i)
    else:
        process_volume(int(arg))
    print("\n全部完成。")
