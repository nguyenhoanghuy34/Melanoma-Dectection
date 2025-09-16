import os
import pandas as pd
import shutil

mask_dir = r'C:\Users\Hoang Huy\Downloads\Seg\data\masks'
output_img_dir = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\img'
output_csv_path = r'C:\Users\Hoang Huy\Downloads\Seg\datamelanoma\metamelanoma.csv'

os.makedirs(output_img_dir, exist_ok=True)

metadata_path = r'C:\Users\Hoang Huy\Downloads\Seg\data\metadata.csv'
metadata = pd.read_csv(metadata_path)

melanoma_df = metadata[metadata['MEL'] == 1.0]
non_melanoma_df = metadata[metadata['MEL'] == 0.0]

melanoma_selected = melanoma_df.sample(n=800, random_state=42) if len(melanoma_df) >= 800 else melanoma_df
non_melanoma_selected = non_melanoma_df.sample(n=400, random_state=42) if len(non_melanoma_df) >= 400 else non_melanoma_df

selected_df = pd.concat([melanoma_selected, non_melanoma_selected], ignore_index=True)

for idx, row in selected_df.iterrows():
    image_id = row['image']
    src_path = os.path.join(mask_dir, image_id + '.png')
    if not os.path.exists(src_path):
        print(f'File ảnh không tồn tại: {src_path}')
        continue
    dst_path = os.path.join(output_img_dir, image_id + '.png')
    shutil.copyfile(src_path, dst_path)

selected_df['label'] = selected_df['MEL'].apply(lambda x: 1 if x == 1.0 else 0)
selected_df[['image', 'label']].to_csv(output_csv_path, index=False)

print('Hoàn thành lọc ảnh và lưu file CSV metamelanoma.csv')
