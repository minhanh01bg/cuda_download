import cv2
import numpy as np

# Đọc ảnh nhiệt
thermal_image = cv2.imread("./img/images.jpeg", cv2.IMREAD_COLOR)

# Chuyển đổi thành ảnh màu sắc
color_image = cv2.applyColorMap(thermal_image, cv2.COLORMAP_JET)

# Hiển thị ảnh gốc
cv2.imshow("Original Thermal Image", thermal_image)

# Hiển thị ảnh chuyển đổi thành màu sắc
cv2.imshow("Color Mapped Image", color_image)
cv2.waitKey(0)

# Đóng cửa sổ hiển thị
cv2.destroyAllWindows()
