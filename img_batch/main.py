import argparse
import sys
import os
import cv2

# 같은 패키지 내의 모듈 import (상대 경로 사용)
# 패키지로 실행 시: python -m img_batch.main
try:
    from .io_utils import get_image_files, ensure_output_dir
    from .ops import resize_image, blur_image, to_gray
except ImportError:
    # 혹시 단독 스크립트로 실행할 경우를 대비한 예외처리
    from io_utils import get_image_files, ensure_output_dir
    from ops import resize_image, blur_image, to_gray

def main():
    parser = argparse.ArgumentParser(description="폴더 이미지 일괄 변환기 (2025 OpenSW)")

    # 1. 인자 설정
    parser.add_argument("--input", "-i", required=True, help="입력 폴더 경로")
    parser.add_argument("--output", "-o", required=True, help="출력 폴더 경로")
    parser.add_argument("--mode", "-m", choices=['copy', 'resize', 'gray', 'blur'], default='copy', help="변환 모드")

    # 추가 설정 인자
    parser.add_argument("--width", type=int, help="리사이즈 가로 길이")
    parser.add_argument("--height", type=int, help="리사이즈 세로 길이")
    parser.add_argument("--ksize", type=int, default=5, help="블러 커널 크기 (홀수)")

    args = parser.parse_args()

    # 2. 인자 에러 핸들링
    
    # 입력 폴더 존재 여부 확인
    if not os.path.exists(args.input):
        print(f"[Error] 입력 폴더를 찾을 수 없습니다: {args.input}")
        sys.exit(1)
        
    if not os.path.isdir(args.input):
        print(f"[Error] 입력 경로는 폴더여야 합니다: {args.input}")
        sys.exit(1)

    # Resize 모드일 때 width/height 필수 체크
    if args.mode == 'resize':
        if not args.width or not args.height:
            print("[Error] 'resize' 모드는 --width와 --height 옵션이 반드시 필요합니다.")
            sys.exit(1)
        if args.width <= 0 or args.height <= 0:
            print("[Error] 가로/세로 길이는 양수여야 합니다.")
            sys.exit(1)

    # Blur 모드일 때 ksize 체크
    if args.mode == 'blur' and args.ksize and args.ksize <= 1:
        print("[Error] 블러 크기(ksize)는 1보다 커야 합니다.")
        sys.exit(1)

    # 3. 작업 시작
    print(f"=== 작업 시작: {args.mode} 모드 ===")

    # 파일 목록 가져오기 (io_utils)
    try:
        image_files = get_image_files(args.input)
    except Exception as e:
        print(f"[Error] {e}")
        sys.exit(1)

    if not image_files:
        print("[System] 처리할 이미지가 없습니다.")
        sys.exit(0)

    # 출력 폴더 생성 (io_utils)
    ensure_output_dir(args.output)

    success_cnt = 0
    fail_cnt = 0

    for path in image_files:
        # 이미지 읽기
        img = cv2.imread(str(path))
        if img is None:
            print(f"[Skip] 이미지 읽기 실패: {path.name}")
            fail_cnt += 1
            continue

        # 변환 로직 (ops)
        processed = img  # 기본은 copy
        
        if args.mode == 'resize':
            processed = resize_image(img, args.width, args.height)
        elif args.mode == 'gray':
            processed = to_gray(img)
        elif args.mode == 'blur':
            processed = blur_image(img, args.ksize)
        
        # 저장
        save_path = os.path.join(args.output, path.name)
        cv2.imwrite(save_path, processed)
        print(f"[OK] {path.name} 저장 완료")
        success_cnt += 1

    print("=" * 40)
    print(f"작업 완료! 성공: {success_cnt}, 실패: {fail_cnt}")
    print(f"결과 폴더: {args.output}")

if __name__ == "__main__":
    main()