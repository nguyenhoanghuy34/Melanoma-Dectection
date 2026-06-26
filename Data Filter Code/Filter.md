# Pipeline Xử Lý Dữ Liệu Melanoma

## 1. Overview

Dự án này xây dựng một pipeline xử lý dữ liệu ảnh y khoa phục vụ bài toán phân loại melanoma. Toàn bộ quy trình gồm 3 bước chính:

- Trích xuất và cân bằng dữ liệu từ metadata gốc
- Chuẩn bị tập ảnh và file CSV tương ứng
- Xáo trộn và chia tập train/test để huấn luyện mô hình

Mục tiêu là tạo ra dataset sạch, cân bằng và có cấu trúc rõ ràng phục vụ training machine learning.

---

## 2. Features

- Lọc dữ liệu theo nhãn melanoma và non-melanoma
- Cân bằng số lượng mẫu giữa các lớp
- Copy và tổ chức lại dữ liệu ảnh
- Tạo file CSV mapping ảnh – label
- Shuffle dữ liệu để tránh bias
- Chia dataset thành train/test reproducible (seed cố định)
- Kiểm tra tính toàn vẹn giữa CSV và file ảnh

---

## 3. Structure từng file

### 3.1 File 1: Tạo dataset ban đầu (lọc + copy ảnh + tạo CSV)

**Chức năng:**

- Đọc `metadata.csv`
- Lọc theo cột `MEL`
- Lấy mẫu:
  - 800 melanoma
  - 400 non-melanoma

- Copy ảnh từ thư mục `masks` sang `datamelanoma/img`
- Tạo file `metamelanoma.csv`

**Output:**

```
datamelanoma/
 ├── img/
 └── metamelanoma.csv
```

---

### 3.2 File 2: Shuffle và chia train/test

**Chức năng:**

- Đọc `metamelanoma.csv`
- Shuffle dữ liệu
- Chia:
  - 1000 train
  - 200 test

- Copy ảnh sang:
  - `train/`
  - `test/`

- Tạo 2 file CSV:
  - `metamelanoma_train.csv`
  - `metamelanoma_test.csv`

**Output:**

```
datamelanoma/
 ├── train/
 ├── test/
 ├── metamelanoma_train.csv
 └── metamelanoma_test.csv
```

---

### 3.3 File 3: Shuffle dataset + kiểm tra đồng bộ

**Chức năng:**

- Kiểm tra mismatch giữa CSV và folder ảnh
- Shuffle danh sách ảnh (seed cố định)
- Copy sang thư mục tạm
- Đồng bộ lại thứ tự CSV theo ảnh
- Ghi đè CSV gốc
- Thay thế folder ảnh bằng bản mới đã shuffle

**Output:**

- Dataset được đồng bộ lại giữa:
  - file ảnh
  - file CSV

---

## 4. Installation liên quan

### Yêu cầu môi trường:

- Python >= 3.8
- pandas
- numpy (tuỳ chọn)
- shutil (built-in)
- os (built-in)

### Cài đặt:

```bash
pip install pandas
```

---

## 5. Configuration

Các tham số quan trọng cần cấu hình:

- Đường dẫn dữ liệu:
  - `metadata.csv`
  - `masks/`
  - `datamelanoma/img/`

- Số lượng mẫu:
  - melanoma: 800
  - non-melanoma: 400
  - train: 1000
  - test: 200

- Seed:

```python
random_state = 42
```

---

## 6. Dataset

Dataset cuối cùng bao gồm:

### Cấu trúc:

```
datamelanoma/
 ├── img/
 ├── train/
 ├── test/
 ├── metamelanoma.csv
 ├── metamelanoma_train.csv
 └── metamelanoma_test.csv
```

### Định dạng CSV:

```
image,label
```

- image: tên file ảnh (không có .png trong một số bước)
- label:
  - 1: melanoma
  - 0: non-melanoma

---

## 7. Results

Sau khi chạy toàn bộ pipeline:

- Dataset được cân bằng giữa 2 lớp
- Ảnh được tổ chức lại rõ ràng theo train/test
- Dữ liệu có tính reproducible nhờ seed cố định
- CSV và ảnh được đồng bộ
- Sẵn sàng cho training model deep learning (CNN, U-Net, v.v.)

Kết quả cuối cùng là một dataset sạch, có cấu trúc chuẩn và có thể sử dụng trực tiếp trong pipeline huấn luyện.
