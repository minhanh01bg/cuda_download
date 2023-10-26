import cv2
import numpy as np

# Đọc ảnh nhiệt
thermal_image = cv2.imread("./img/images.jpeg", cv2.IMREAD_COLOR)

# Hiển thị ảnh gốc
cv2.imshow("Original Thermal Image", thermal_image)
cv2.waitKey(0)

# Cân bằng nhiệt độ
thermal_image = cv2.cvtColor(thermal_image, cv2.COLOR_BGR2GRAY)
thermal_image_equalized = cv2.equalizeHist(thermal_image)

# Hiển thị ảnh sau khi cân bằng nhiệt độ
cv2.imshow("Equalized Thermal Image", thermal_image_equalized)
cv2.waitKey(0)

# Loại bỏ nhiễu
kernel = np.ones((3, 3), np.uint8)
thermal_image_equalized = cv2.morphologyEx(thermal_image_equalized, cv2.MORPH_OPEN, kernel)

# Hiển thị ảnh sau khi loại bỏ nhiễu
cv2.imshow("Noise Removed", thermal_image_equalized)
cv2.waitKey(0) 

# Làm sáng và tương phản
alpha = 1.2  # Faktor sáng
beta = 10    # Faktor tương phản
thermal_image_brightness_contrast = cv2.convertScaleAbs(thermal_image_equalized, alpha=alpha, beta=beta)
# Hiển thị ảnh sau khi làm sáng và tương phản
cv2.imshow("Brightness and Contrast Adjusted", thermal_image_brightness_contrast)
cv2.waitKey(0)

# Đóng cửa sổ hiển thị
cv2.destroyAllWindows()
