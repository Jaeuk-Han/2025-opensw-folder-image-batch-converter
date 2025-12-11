import argparse
import sys
import os

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

    print(f"[Check] 옵션 검증 통과. (모드: {args.mode})")

if __name__ == "__main__":
    main()