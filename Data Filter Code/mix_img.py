import os
import pandas as pd
import random
import shutil

output_img_dir = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\img'
output_csv_path = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\metamelanoma.csv'

# Đọc CSV hiện tại
df = pd.read_csv(output_csv_path)

# Lấy danh sách ảnh hiện tại trong folder
image_files = [f for f in os.listdir(output_img_dir) if f.endswith('.png')]

# Kiểm tra độ khớp giữa CSV và ảnh (ảnh có trong CSV không)
csv_images = set(df['image'] + '.png')
image_set = set(image_files)
missing_in_csv = image_set - csv_images
missing_in_folder = csv_images - image_set
if missing_in_csv:
    print(f"Cảnh báo: Có ảnh trong folder không có trong CSV: {missing_in_csv}")
if missing_in_folder:
    print(f"Cảnh báo: Có ảnh trong CSV không có trong folder: {missing_in_folder}")

# Xáo trộn danh sách ảnh
random.seed(42)  # cố định seed để xáo trộn reproducible
random.shuffle(image_files)

# Tạo folder tạm lưu ảnh xáo trộn
temp_dir = output_img_dir + '_temp'
os.makedirs(temp_dir, exist_ok=True)

# Copy ảnh theo thứ tự xáo trộn sang thư mục tạm
for img_name in image_files:
    src_path = os.path.join(output_img_dir, img_name)
    dst_path = os.path.join(temp_dir, img_name)
    shutil.copyfile(src_path, dst_path)

# Xây dựng lại DataFrame theo thứ tự xáo trộn
shuffled_images = [os.path.splitext(f)[0] for f in image_files]
new_df = df.set_index('image').loc[shuffled_images].reset_index()

# Ghi lại CSV theo thứ tự mới
new_df.to_csv(output_csv_path, index=False)

# Xóa thư mục ảnh cũ, đổi tên thư mục tạm thành thư mục ảnh chính
for f in image_files:
    os.remove(os.path.join(output_img_dir, f))
os.rmdir(output_img_dir)
os.rename(temp_dir, output_img_dir)

print("Đã xáo trộn ảnh và cập nhật file CSV thành công.")
