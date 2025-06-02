import pandas as pd
import random
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# ==============================================================================
import pandas as pd
import random
import re

# ==============================================================================
# "CƠ SỞ TRI THỨC" VỀ CÁC CÔNG NGHỆ TƯƠNG ĐƯƠNG
# Nền tảng cho việc tạo ra các mẫu "positive" một cách thông minh.
# Bạn có thể tự do mở rộng từ điển này nếu muốn.
# ==============================================================================
EQUIVALENTS = {
    # Front-end Web
    'react': ['angular', 'vue.js', 'svelte', 'next.js', 'nuxt.js'],
    'angular': ['react', 'vue.js', 'svelte'],
    'vue.js': ['react', 'angular', 'svelte'],
    # Back-end
    '.net': ['java spring boot', 'python django', 'node.js express', 'golang gin', 'nest.js'],
    'node.js': ['.net', 'java spring boot', 'python django', 'ruby on rails'],
    'django': ['asp.net core', 'spring boot', 'fastapi'],
    'java spring boot': ['.net', 'django', 'node.js'],
    # Mobile
    'swift': ['kotlin'],
    'kotlin': ['swift'],
    'react native': ['flutter', 'xamarin', '.net maui'],
    'flutter': ['react native', 'xamarin'],
    # Game Engines
    'unity': ['unreal engine', 'godot'],
    'unreal engine': ['unity', 'godot'],
    # Databases
    'sql server': ['postgresql', 'mysql', 'oracle'],
    'postgresql': ['mysql', 'sql server', 'sqlite'],
    'mysql': ['postgresql', 'sql server'],
    'mongodb': ['cassandra', 'redis', 'dynamodb'],
    'redis': ['memcached'],
    # Cloud & DevOps
    'aws': ['azure', 'google cloud platform (gcp)'],
    'azure': ['aws', 'gcp'],
    'gcp': ['aws', 'azure'],
    'docker': ['podman', 'kubernetes'],
    'jenkins': ['github actions', 'gitlab ci/cd', 'circleci'],
    'github actions': ['gitlab ci/cd', 'jenkins'],
    'jira': ['trello', 'asana', 'notion'],
}

def find_and_replace_tech(tech_string):
    """
    Tìm và thay thế một công nghệ trong chuỗi bằng một công nghệ tương đương.
    """
    tech_string_lower = tech_string.lower()
    found_keys = [key for key in EQUIVALENTS if re.search(r'\b' + re.escape(key) + r'\b', tech_string_lower)]

    if not found_keys:
        return tech_string

    key_to_replace = random.choice(found_keys)
    replacement = random.choice(EQUIVALENTS[key_to_replace])
    return re.sub(r'(?i)\b' + re.escape(key_to_replace) + r'\b', replacement, tech_string, count=1)

def generate_triplets(df, tech_column, num_positives=10):
    """
    Tạo ra bộ dữ liệu triplet từ DataFrame đầu vào.
    """
    all_techs = df[tech_column].dropna().tolist()
    triplets = []

    for _, row in df.iterrows():
        anchor = row[tech_column]
        if pd.isna(anchor):
            continue

        for _ in range(num_positives):
            positive = find_and_replace_tech(anchor)
            possible_negatives = [t for t in all_techs if t != anchor]
            if not possible_negatives:
                continue
            negative = random.choice(possible_negatives)
            triplets.append({'anchor': anchor, 'positive': positive, 'negative': negative})

    return pd.DataFrame(triplets)

# --- PHẦN THỰC THI CHÍNH ---
if __name__ == "__main__":
    try:
        df_input = pd.read_csv("D:/Traning AI/technology.csv")
        tech_col_name = df_input.columns[0] # Giả định cột công nghệ là cột đầu tiên
        
        print(f"Đã đọc thành công tệp 'technology.csv'. Sử dụng cột '{tech_col_name}' làm anchor.")
        print("Bắt đầu tạo dữ liệu...")

        df_triplets = generate_triplets(df_input, tech_col_name, num_positives=10)
        
        df_triplets.to_csv('D:/Traning AI/triplet_dataset_technology.csv', index=False, encoding='utf-8-sig')

        print("\n--- HOÀN THÀNH ---")
        print(f"Đã tạo thành công {len(df_triplets)} bộ dữ liệu.")
        print("Tệp kết quả đã được lưu với tên 'triplet_dataset.csv'.")

    except FileNotFoundError:
        print("\nLỖI: Không tìm thấy tệp 'technology.csv'.")
        print("Vui lòng đảm bảo bạn đã đặt tệp 'technology.csv' vào cùng thư mục với tệp mã nguồn này.")
    except Exception as e:
        print(f"\nĐã xảy ra lỗi: {e}")