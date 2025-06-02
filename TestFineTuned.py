# Import các thư viện cần thiết
from sentence_transformers import SentenceTransformer
import torch
import sys
import io
import os
# from RitrieveListDoc import extract_project_info
# --- Bước 1: Tải lại mô hình đã fine-tune  với gg codelab---
# print("Đang kết nối tới Google Drive...")
# drive.mount('/content/drive')
# final_model_path = "/content/drive/MyDrive/my_models/my-finetune-nhatkarit"
# Sửa lại đường dẫn tới thư mục chứa mô hình của bạn nếu cần

#fix lỗi format 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
final_model_path = r"D:/Traning AI/Model/my-finetune-nhatkarit-with-SP-SU25-data-v2"
print(f"Đang tải mô hình từ: {final_model_path}")
model = SentenceTransformer(final_model_path)
print("Tải mô hình thành công!")


# --- Chuẩn bị các câu tiếng Anh và tạo embeddings ---
sentences_to_test = [
"Build the FCareerConnect system to enable smart job matching with a virtual workspace.",
"Building a Job Hiring and Search Platform"
]

print("\nĐang tạo embeddings cho các câu test...")
embeddings = model.encode(sentences_to_test)
print("Đã tạo xong!")


# --- Tính toán độ tương đồng bằng model.similarity() ---
print("\nĐang tính toán ma trận tương đồng...")
similarities = model.similarity(embeddings, embeddings)
print("Đã tính xong!")



print("\n--- KẾT QUẢ SO SÁNH TƯƠNG ĐỒNG ---")

for i in range(len(sentences_to_test)):
    for j in range(i + 1, len(sentences_to_test)):
        print(f"'{sentences_to_test[i]}' \n& '{sentences_to_test[j]}'")
        print(f">>> Score: {similarities[i][j].item():.4f}\n")