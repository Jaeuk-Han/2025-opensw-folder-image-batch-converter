import argparse
import sys
from pathlib import Path

import cv2

#프로젝트 루트 경로를 모듈 검색 경로에 추가
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from img_batch.io_utils import get_image_files, ensure_output_dir
from img_batch.ops import resize_image, blur_image, to_gray


def process_folder(input_dir: str,
                   output_dir: str,
                   mode: str = "copy",
                   width: int = None,
                   height: int = None,
                   ksize: int = None):
    """
    input_dir 폴더의 이미지를 읽어서
    - mode에 따라 변환한 뒤
    - output_dir 폴더에 같은 파일 이름으로 저장

    mode:
      - "copy"   : 원본 그대로 저장
      - "gray"   : 흑백 변환
      - "blur"   : 블러(흐리게) 처리
      - "resize" : 지정한 크기로 리사이즈
    """

    #input_dir 폴더의 이미지들을 읽어 output_dir 폴더에 그대로 복사하는 작업 수행

    try:
        image_files = get_image_files(input_dir)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"ERROR {e}")
        return

    if not image_files:
        print(f"No such image files: {input_dir}")
        return

    output_path = ensure_output_dir(output_dir)

    print(f"Found Images: {len(image_files)}")
    print(f"Output Folder: {output_path}")
    print(f"Mode {mode}")

    success = 0
    failed = 0

    for img_path in image_files:
        img = cv2.imread(str(img_path))

        if img is None:
            print(f"Unreadable image, skipped: {img_path.name}")
            failed += 1
            continue

        #모드에 따라 이미지 변환
        if mode == "gray":
            img = to_gray(img)

        elif mode == "blur":
            if ksize is None:
                ksize = 5  #기본 블러 커널 크기
            img = blur_image(img, ksize)

        elif mode == "resize":
            if width is None or height is None:
                print(f"Resize mode but width/height is not set, save in original size: {img_path.name}")
            else:
                img = resize_image(img, width, height)

        #mode == "copy" 인 경우는 원본 그대로

        save_path = output_path / img_path.name

        if cv2.imwrite(str(save_path), img):
            print(f"OK {img_path.name} -> {save_path}")
            success += 1
        else:
            print(f"Failed to save: {img_path.name}")
            failed += 1

    print(f"Successfully Saved - Success: {success}items, Failed: {failed}items")


def main():
    parser = argparse.ArgumentParser(
        description="Converts images in the input folder according to the mode and saves them in the output folder."
    )
    parser.add_argument("--input", required=True, help="input folder path")
    parser.add_argument("--output", required=True, help="output folder path")

    #처리 모드 선택
    parser.add_argument(
        "--mode",
        choices=["copy", "gray", "blur", "resize"],
        default="copy",
        help="image processing mode (Select one: copy, gray, blur, resize. Default: copy)",
    )

    #리사이즈 옵션
    parser.add_argument("--width", type=int, help="Horizontal size to use in resize mode")
    parser.add_argument("--height", type=int, help="Vertical size to use in resize mode")

    #블러 옵션
    parser.add_argument("--ksize", type=int, help="Kernel size to use in blur mode (odd number like 3, 5, 7)")

    args = parser.parse_args()

    process_folder(
        args.input,
        args.output,
        mode=args.mode,
        width=args.width,
        height=args.height,
        ksize=args.ksize,
    )


if __name__ == "__main__":
    main()
