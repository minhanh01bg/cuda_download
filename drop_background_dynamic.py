import cv2

# Tạo một đối tượng BackgroundSubtractorMOG2
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Mở video hoặc webcam
cap = cv2.VideoCapture(0)  # Thay "your_video_file.mp4" bằng tên tệp video của bạn

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Áp dụng thuật toán loại bỏ nền
    fg_mask = bg_subtractor.apply(frame)

    # Áp dụng bản đồ màu
    fg_colored = cv2.applyColorMap(fg_mask, cv2.COLORMAP_JET)

    # Hiển thị kết quả
    cv2.imshow("Foreground", fg_colored)
    cv2.imshow("Original Frame", frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
