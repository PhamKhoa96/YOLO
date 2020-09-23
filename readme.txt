1. Tải source code Darknet – Yolo về máy tính, chỉnh tham số và tiến hành biên dịch (make) source code đó ra file thực thi tùy theo hệ điều hành (window thì là exe, macos với linux thì file bash thì phải, tóm lại là file chạy được)
2. Chuẩn bị dữ liệu train: Hình ảnh của đối tượng bạn định train. Ví dụ như bài này là súng ngắn.
3. Gán nhãn cho dữ liệu: Cụ thể là với từng ảnh trong dữ liệu, chúng ta sẽ gán nhãn cho máy biết đâu là đối tượng cần nhận dạng bằng cách vẽ một hình chữ nhật xung quanh đối tượng đó. Cái này có tool nhé.
4. Tạo các file cần thiết để phục vụ quá trình train, chỉnh sửa tham số train trong file cấu hình Yolo.
5. Chạy lệnh train và ngồi uống cafe đợi.
6. Tận hưởng thành quả bằng cách detect thử một ảnh sample.