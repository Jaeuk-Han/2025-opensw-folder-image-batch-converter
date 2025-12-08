import argparse
import sys
from pathlib import Path

import cv2

# 프로젝트 루트 경로를 모듈 검색 경로에 추가
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from img_batch.io_utils import get_image_files, ensure_output_dir


def process_folder(input_dir: str, output_dir: str):
  
    #input_dir 폴더의 이미지들을 읽어 output_dir 폴더에 그대로 복사하는 작업 수행

    try:
        image_files = get_image_files(input_dir)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"ERROR {e}")
        return

    if not image_files:
        print(f"No image files found in: {input_dir}")
        return

    output_path = ensure_output_dir(output_dir)

    print(f"Found Images: {len(image_files)}")
    print(f"Output Folder: {output_path}")

    success = 0
    failed = 0

    for img_path in image_files:
        img = cv2.imread(str(img_path))

        if img is None:
            print(f"Unreadable image, skipped: {img_path.name}")
            failed += 1
            continue

        save_path = output_path / img_path.name

        if cv2.imwrite(str(save_path), img):
            print(f"OK {img_path.name} -> {save_path}")
            success += 1
        else:
            print(f"Failed to save: {img_path.name}")
            failed += 1

    print(f"Successfully Saved - Success: {success}, Failed: {failed}")


def main():
    parser = argparse.ArgumentParser(
        description="Converts images in the input folder according to the mode and saves them in the output folder."
    )
    parser.add_argument("--input", required=True, help="input folder path")
    parser.add_argument("--output", required=True, help="output folder path")

    args = parser.parse_args()

    process_folder(args.input, args.output)


if __name__ == "__main__":
    main()
