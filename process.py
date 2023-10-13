import cv2
import numpy as np
# Đọc bức ảnh nhiệt
image = cv2.imread('thermal_image.jpg', cv2.IMREAD_COLOR)

# Cân bằng nhiệt độ
equ = cv2.equalizeHist(image)

# Làm sáng hình ảnh nhiệt
alpha = 2  # Tùy chỉnh giá trị alpha tùy theo nhu cầu
beta = 50  # Tùy chỉnh giá trị beta tùy theo nhu cầu
brightened = cv2.convertScaleAbs(equ, alpha=alpha, beta=beta)

# Hiển thị hình ảnh gốc và hình ảnh sau khi tiền xử lý
cv2.imshow('Original Image', image)
cv2.imshow('Preprocessed Image', brightened)

# Lưu hình ảnh sau khi tiền xử lý (nếu cần)
cv2.imwrite('preprocessed_image.jpg', brightened)

# Chờ người dùng nhấn phím bất kỳ để đóng cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()
