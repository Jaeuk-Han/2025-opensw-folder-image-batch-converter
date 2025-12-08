from pathlib import Path

VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}

def get_image_files(input_dir: str):

    #input_dir 폴더 안에서 이미지 파일 리스트를 반환

    input_path = Path(input_dir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input folder not found: {input_dir}")

    if not input_path.is_dir():
        raise NotADirectoryError(f"Input path is not a folder: {input_dir}")

    files = []

    for p in input_path.iterdir():
        # 파일이면서 확장자가 이미지인 경우만 추가
        if p.is_file() and p.suffix.lower() in VALID_EXTENSIONS:
            files.append(p)

    return files

def ensure_output_dir(output_dir: str):

    #output_dir 폴더가 없으면 만든 뒤 path 객체를 반환

    output_path = Path(output_dir)

    output_path.mkdir(parents=True, exist_ok=True)
    return output_path
