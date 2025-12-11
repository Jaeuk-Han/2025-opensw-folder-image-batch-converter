import argparse
import sys

def main():
    # 1. 파서 생성 및 설명 작성
    parser = argparse.ArgumentParser(description="폴더 이미지 일괄 변환기 (2025 OpenSW)")

    # 2. 필수 인자 (입력/출력 폴더)
    parser.add_argument("--input", "-i", required=True, help="입력 폴더 경로")
    parser.add_argument("--output", "-o", required=True, help="출력 폴더 경로")
    
    # 3. 모드 선택 (copy, resize, gray, blur)
    parser.add_argument("--mode", "-m", choices=['copy', 'resize', 'gray', 'blur'], default='copy', help="변환 모드 선택")
    
    # 4. 추가 옵션 (크기, 블러 강도)
    parser.add_argument("--width", type=int, help="리사이즈 가로 길이")
    parser.add_argument("--height", type=int, help="리사이즈 세로 길이")
    parser.add_argument("--ksize", type=int, default=5, help="블러 커널 크기 (홀수)")

    # 인자 파싱 테스트
    args = parser.parse_args()
    print(f"[Init] 설정된 모드: {args.mode}")
    print(f"[Init] 입력 경로: {args.input}")

if __name__ == "__main__":
    main()