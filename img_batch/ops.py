# img_batch/ops.py
from __future__ import annotations

import cv2
import numpy as np


def resize_image(img: np.ndarray, width: int, height: int) -> np.ndarray:
    """
    이미지를 (width, height) 크기로 리사이즈한다.
    """
    if width <= 0 or height <= 0:
        raise ValueError("width와 height는 0보다 커야 합니다.")
    return cv2.resize(img, (width, height))


def blur_image(img: np.ndarray, ksize: int = 5) -> np.ndarray:
    """
    이미지를 가우시안 블러로 흐리게 만든다.
    ksize는 1보다 큰 홀수여야 한다.
    """
    if ksize <= 1:
        raise ValueError("ksize는 1보다 큰 값이어야 합니다.")
    if ksize % 2 == 0:
        ksize += 1  # 짝수면 +1 해서 홀수로 맞춤
    return cv2.GaussianBlur(img, (ksize, ksize), 0)


def to_gray(img: np.ndarray) -> np.ndarray:
    """
    BGR 이미지를 그레이스케일로 변환한다.
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def rotate_image(img: np.ndarray, angle: float) -> np.ndarray:
    """
    이미지를 중심 기준으로 angle(도 단위) 만큼 회전시킨다.
    양수: 반시계 방향, 음수: 시계 방향
    """
    h, w = img.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    return rotated


def flip_image(img: np.ndarray, mode: str = "horizontal") -> np.ndarray:
    """
    이미지를 좌우/상하 반전한다.

    mode:
        - "horizontal" : 좌우 반전
        - "vertical"   : 상하 반전
    """
    if mode == "horizontal":
        return cv2.flip(img, 1)
    elif mode == "vertical":
        return cv2.flip(img, 0)
    else:
        raise ValueError("mode는 'horizontal' 또는 'vertical' 이어야 합니다.")

def adjust_brightness_contrast(
    img: np.ndarray,
    alpha: float = 1.0,
    beta: float = 0.0,
) -> np.ndarray:
    """
    이미지의 대비(contrast)와 밝기(brightness)를 조절한다.

    alpha: 대비 계수 (1.0: 원본, >1.0: 대비 증가, 0~1.0: 대비 감소)
    beta : 밝기 오프셋 (0: 원본, >0: 더 밝게, <0: 더 어둡게)
    """
    # convertScaleAbs는 내부적으로 img * alpha + beta 를 계산한 뒤
    # 0~255 범위로 클리핑하고 uint8로 변환해 준다.
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return adjusted


def edge_detect(
    img: np.ndarray,
    threshold1: int = 100,
    threshold2: int = 200,
) -> np.ndarray:
    """
    Canny 엣지 검출을 이용해 윤곽선을 추출한다.

    threshold1, threshold2:
        Canny 알고리즘에서 사용하는 하한/상한 임계값.
        값이 낮을수록 더 많은 엣지가 검출된다.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    return edges