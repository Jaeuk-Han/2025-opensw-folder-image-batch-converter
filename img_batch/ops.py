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
