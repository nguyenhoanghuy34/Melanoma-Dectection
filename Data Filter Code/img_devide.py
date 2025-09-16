import os
import pandas as pd
import random
import shutil

# Đường dẫn thư mục ảnh và metadata
img_dir = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\img'
csv_path = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\metamelanoma.csv'

# Đường dẫn thư mục train và test mới
train_img_dir = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\train'
test_img_dir = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\test'

# Đường dẫn file csv cho train và test
train_csv_path = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\metamelanoma_train.csv'
test_csv_path = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\metamelanoma_test.csv'

# Tạo thư mục nếu chưa có
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(test_img_dir, exist_ok=True)

# Đọc file CSV gốc
df = pd.read_csv(csv_path)

# Xáo trộn
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Chia 1000 train, 200 test
train_df = df_shuffled.iloc[:1000]
test_df = df_shuffled.iloc[1000:1200]

# Copy ảnh vào thư mục train
for idx, row in train_df.iterrows():
    src_path = os.path.join(img_dir, row['image'] + '.png')
    dst_path = os.path.join(train_img_dir, row['image'] + '.png')
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dst_path)
    else:
        print(f"[TRAIN] MISSING: {src_path}")

# Copy ảnh vào thư mục test
for idx, row in test_df.iterrows():
    src_path = os.path.join(img_dir, row['image'] + '.png')
    dst_path = os.path.join(test_img_dir, row['image'] + '.png')
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dst_path)
    else:
        print(f"[TEST] MISSING: {src_path}")

# Lưu file CSV tương ứng
train_df.to_csv(train_csv_path, index=False)
test_df.to_csv(test_csv_path, index=False)

print("✅ Đã chia thành tập huấn luyện (1000 ảnh) và kiểm tra (200 ảnh).")
