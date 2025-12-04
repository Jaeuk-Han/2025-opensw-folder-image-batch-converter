# 2025 OpenSW – Folder Image Batch Converter

## 현재까지 구현된 내용 (이미지 처리 파트)

1단계로 리사이즈, 흑백, 블러 등의 모드를 지원하는 이미지 처리 함수를 패키지 형태로 구현해 두었습니다.  

`img_batch` 모듈을 import 해서 사용하면 됩니다.  

자세한 사용법은 아래 예시 코드나 **examples/demo_image_ops.py**를 참고해주세요.

현재 제공되는 주요 함수:

- `resize_image(img, width, height)`
- `blur_image(img, ksize)`
- `to_gray(img)`
- `rotate_image(img, angle)`
- `flip_image(img, mode)`  (`"horizontal"` / `"vertical"`)
- `adjust_brightness_contrast(img, alpha, beta)`
- `edge_detect(img, threshold1, threshold2)`

---

## 현재 디렉토리 구조 (요약)

```text
2025-opensw-folder-image-batch-converter/
├─ examples/
│  ├─ input/
│  │  └─ sample.png          # 데모용 입력 이미지
│  ├─ output_demo/           # 데모 실행 결과 (gitignore 권장)
│  └─ demo_image_ops.py      # img_batch 사용 예제 스크립트
├─ img_batch/                # 이미지 처리 패키지
│  ├─ __init__.py
│  └─ ops.py
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

## Repo Clone 예시

```bash
git clone https://github.com/Jaeuk-Han/2025-opensw-folder-image-batch-converter.git
cd 2025-opensw-folder-image-batch-converter
```
