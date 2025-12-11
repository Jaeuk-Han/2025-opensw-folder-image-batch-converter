# 2025 OpenSW – Folder Image Batch Converter

## 현재까지 구현된 내용 (이미지 처리 파트)

1단계로 리사이즈, 흑백, 블러 등의 모드를 지원하는 이미지 처리 함수를 패키지 형태로 구현해 두었습니다.  

폴더 단위로 이미지를 불러와 copy/gray/blur/resize 모드로 일괄 변환하는 스크립트(`folder_copy_basic.py`)가 추가되었습니다.


`img_batch` 모듈을 import 해서 단일 이미지를 처리하면 됩니다.
폴더 단위 처리는 examples/folder_copy_basic.py에서 수행할 수 있습니다.

자세한 사용법은 아래 예시 코드나 **examples/demo_image_ops.py**를 참고해주세요.
폴더 일괄 변환 예시인 examples/folder_copy_basic.py를 참고해주세요.

의존성에 대해서는 pyproject.toml 확인하시면 됩니다.

현재 제공되는 주요 함수:

- `resize_image(img, width, height)`
- `blur_image(img, ksize)`
- `to_gray(img)`
- `rotate_image(img, angle)`
- `flip_image(img, mode)`  (`"horizontal"` / `"vertical"`)
- `adjust_brightness_contrast(img, alpha, beta)`
- `edge_detect(img, threshold1, threshold2)`

추가된 폴더 처리 기능 (folder_copy_basic.py):

- 입력 폴더에서 이미지 파일 목록 읽기 (get_image_files)
- 출력 폴더 자동 생성 (ensure_output_dir)
- --mode 옵션을 통해 copy / gray / blur / resize 선택 가능
- resize 모드에서 --width, --height 지정 가능
- blur 모드에서 --ksize 지정 가능
- 변환된 이미지를 원래 파일명 그대로 출력 폴더에 저장
  
---

## 현재 디렉토리 구조 (요약)

```text
2025-opensw-folder-image-batch-converter/
├─ examples/
│ ├─ input/
│ │ └─ sample.png # 데모용 입력 이미지
│ ├─ output_demo/ # 데모 실행 결과 (gitignore 권장)
│ ├─ demo_image_ops.py # img_batch 사용 예제 스크립트
│ └─ folder_copy_basic.py # 폴더 단위 일괄 처리(copy/gray/blur/resize)
├─ img_batch/ # 이미지 처리 패키지
│ ├─ init.py
│ ├─ ops.py
│ └─ io_utils.py
├─ .gitignore
├─ LICENSE
├─ poetry.lock
├─ pyproject.toml
└─ README.md
```

---

## img_batch 패키지 사용 예시

```py
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

# 이미지 불러오기
img = cv2.imread("path/to/input.png")

# 예시: 리사이즈 + 엣지 검출
resized = resize_image(img, width=300, height=300)
edges = edge_detect(resized, threshold1=100, threshold2=200)

cv2.imwrite("output_resize.png", resized)
cv2.imwrite("output_edges.png", edges)
```
---

## 테스트용 데모 코드(demo_image_ops.py) 사용 예시

`img_batch` 모듈의 기능 예시와 테스트를 위한 코드의 실행 예시입니다.

poetry가 아닌 다른 환경에서 진행하실때는 앞에 **poetry run** 빼시고 CLI에 입력하시면 됩니다.

```bash
poetry run python examples/demo_image_ops.py \
    --input examples/input/sample.png \
    --output-dir examples/output_demo
```

---

## 폴더 단위 이미지 일괄 변환(folder_copy_basic.py) 실행 예시

```bash
python examples/folder_copy_basic.py \
    --input examples/input \
    --output examples/output_demo \
    --mode copy
```

흑백 변환(gray):

```py
python examples/folder_copy_basic.py \
    --input examples/input \
    --output examples/output_gray \
    --mode gray
```

블러 처리(blur):

```py
python examples/folder_copy_basic.py \
    --input examples/input \
    --output examples/output_blur \
    --mode blur \
    --ksize 7
```

리사이즈(resize):

```py
python examples/folder_copy_basic.py \
    --input examples/input \
    --output examples/output_resize \
    --mode resize \
    --width 800 \
    --height 600
```

## Repo Clone 예시

```bash
git clone https://github.com/Jaeuk-Han/2025-opensw-folder-image-batch-converter.git
cd 2025-opensw-folder-image-batch-converter
```
