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

from img_batch import (
    resize_image,
    blur_image,
    to_gray,
    rotate_image,
    flip_image,
    adjust_brightness_contrast,
    edge_detect,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="img_batch 이미지 변환 함수 테스트 (resize / gray / blur / rotate / flip / brightness / edge)"
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

    stem = input_path.stem
    suffix = input_path.suffix  # .png, .jpg 등

    # 2) 리사이즈 테스트 (예: 300x300)
    resized = resize_image(img, width=300, height=300)
    out_resize = output_dir / f"{stem}_resize_300x300{suffix}"
    cv2.imwrite(str(out_resize), resized)
    print(f"[INFO] 리사이즈 결과 저장: {out_resize}")

    # 3) 그레이스케일 테스트
    gray = to_gray(img)
    out_gray = output_dir / f"{stem}_gray{suffix}"
    cv2.imwrite(str(out_gray), gray)
    print(f"[INFO] 그레이스케일 결과 저장: {out_gray}")

    # 4) 블러 테스트 (예: ksize=9)
    blurred = blur_image(img, ksize=9)
    out_blur = output_dir / f"{stem}_blur_ksize9{suffix}"
    cv2.imwrite(str(out_blur), blurred)
    print(f"[INFO] 블러 결과 저장: {out_blur}")

    # 5) 회전 테스트 (예: 90도)
    rotated_90 = rotate_image(img, angle=90.0)
    out_rotate_90 = output_dir / f"{stem}_rotate_90{suffix}"
    cv2.imwrite(str(out_rotate_90), rotated_90)
    print(f"[INFO] 회전(90도) 결과 저장: {out_rotate_90}")

    # 6) 플립 테스트 (좌우 / 상하)
    flipped_h = flip_image(img, mode="horizontal")
    out_flip_h = output_dir / f"{stem}_flip_horizontal{suffix}"
    cv2.imwrite(str(out_flip_h), flipped_h)
    print(f"[INFO] 좌우 반전 결과 저장: {out_flip_h}")

    flipped_v = flip_image(img, mode="vertical")
    out_flip_v = output_dir / f"{stem}_flip_vertical{suffix}"
    cv2.imwrite(str(out_flip_v), flipped_v)
    print(f"[INFO] 상하 반전 결과 저장: {out_flip_v}")

    # 7) 밝기/대비 조절 테스트 (예: alpha=1.2, beta=30)
    brighter = adjust_brightness_contrast(img, alpha=1.2, beta=30.0)
    out_bright = output_dir / f"{stem}_bright_a1.2_b30{suffix}"
    cv2.imwrite(str(out_bright), brighter)
    print(f"[INFO] 밝기/대비 조절 결과 저장: {out_bright}")

    # 8) 엣지 검출 테스트 (예: threshold1=100, threshold2=200)
    edges = edge_detect(img, threshold1=100, threshold2=200)
    out_edge = output_dir / f"{stem}_edge_t100_200{suffix}"
    cv2.imwrite(str(out_edge), edges)
    print(f"[INFO] 엣지 검출 결과 저장: {out_edge}")

    print("[DONE] img_batch 테스트용 변환 8종 완료")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())