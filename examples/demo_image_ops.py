# examples/demo_image_ops.py
"""
img_batch 패키지의 이미지 변환 함수들을 간단히 테스트하는 스크립트.

사용 예시:
    poetry run python examples/demo_image_ops.py \
        --input examples/input/sample.png \
        --output-dir examples/output_demo
"""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2

from img_batch import resize_image, blur_image, to_gray  # 우리 패키지에서 가져옴


def parse_args():
    parser = argparse.ArgumentParser(
        description="img_batch 이미지 변환 함수 테스트 (resize / gray / blur)"
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="입력 이미지 파일 경로 (예: examples/input/sample.png)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="출력 이미지 저장 폴더 (예: examples/output_demo)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    input_path: Path = args.input
    output_dir: Path = args.output_dir

    if not input_path.exists():
        print(f"[ERROR] 입력 이미지 파일을 찾을 수 없습니다: {input_path}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)

    # 1) 이미지 로드
    img = cv2.imread(str(input_path))
    if img is None:
        print(f"[ERROR] 이미지를 읽어올 수 없습니다: {input_path}")
        return 1

    print(f"[INFO] 입력 이미지 크기: {img.shape[1]}x{img.shape[0]} (W x H)")

    # 파일 이름/확장자 나누기
    stem = input_path.stem
    suffix = input_path.suffix  # .jpg, .png 등

    # 2) 리사이즈 테스트 (예: 300x300)
    resized = resize_image(img, width=300, height=300)
    out_resize = output_dir / f"{stem}_resize_300x300{suffix}"
    cv2.imwrite(str(out_resize), resized)
    print(f"[INFO] 리사이즈 결과 저장: {out_resize}")

    # 3) 그레이스케일 테스트
    gray = to_gray(img)
    # 그레이스케일은 보통 .jpg 그대로 저장해도 되고, 필요하면 png로 바꿔도 됨
    out_gray = output_dir / f"{stem}_gray{suffix}"
    cv2.imwrite(str(out_gray), gray)
    print(f"[INFO] 그레이스케일 결과 저장: {out_gray}")

    # 4) 블러 테스트 (예: ksize=9)
    blurred = blur_image(img, ksize=9)
    out_blur = output_dir / f"{stem}_blur_ksize9{suffix}"
    cv2.imwrite(str(out_blur), blurred)
    print(f"[INFO] 블러 결과 저장: {out_blur}")

    print("[DONE] img_batch 테스트용 변환 3종 완료")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
