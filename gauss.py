import cv2
import numpy as np
# Bạn có thể sử dụng lọc thông thấp để loại bỏ nhiễu và làm mịn hình ảnh nhiệt. Lọc thông cao có thể giúp làm nổi bật các cạnh và chi tiết.
# Đọc ảnh nhiệt
thermal_image = cv2.imread("./img/images.jpeg", cv2.IMREAD_COLOR)

# Áp dụng bộ lọc Gauss (lọc thông thấp)
blurred_image = cv2.GaussianBlur(thermal_image, (5, 5), 0)

# Áp dụng bộ lọc Laplacian
laplacian_image = cv2.Laplacian(thermal_image, cv2.CV_64F)

# Hiển thị ảnh gốc
cv2.imshow("Original Thermal Image", thermal_image)

# Hiển thị ảnh sau khi áp dụng bộ lọc Gauss
cv2.imshow("Blurred Image", blurred_image)

# Hiển thị ảnh sau khi áp dụng bộ lọc Laplacian
cv2.imshow("Laplacian Image", laplacian_image)
cv2.waitKey(0)

# Đóng cửa sổ hiển thị
cv2.destroyAllWindows()
