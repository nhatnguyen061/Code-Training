# from RitrieveListDoc import extract_project_info
import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


#---------------------------
# def paraphrase_on_zerogpt(driver,text:str):
#     paraphrase_result = ""
#     print("Starting paraphrasing on ZeroGPT...")
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#     try:
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#     except Exception as e:
#         print(f"❌ Lỗi khi khởi tạo WebDriver. Vui lòng kiểm tra kết nối mạng hoặc cài đặt Chrome. Lỗi: {e}")
#         return ""
#     try:
#         # 1. Mở trang web
#         driver.get(TARGET_URL)
#         print(f"✅ Đã truy cập thành công trang: {TARGET_URL}")

#         # 3. Nhập văn bản gốc
#         # Trang này sử dụng data-test-id, một bộ chọn rất ổn định để tự động hóa
#         input_box_selector = (By.ID, "textArea")
#         input_box = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(input_box_selector)
#         )
#         input_box.clear()
#         input_box.send_keys(text)
#         print("✅ Đã nhập văn bản gốc.")
#         time.sleep(2) # Chờ một chút để trang web xử lý input
#         # 4. Nhấn nút "Paraphrase"
#         submit_button_selector = (By.XPATH, "//button[@class='scoreButton' and text()='Paraphrase Text']")
#         submit_button = WebDriverWait(driver, 20).until(
#             EC.element_to_be_clickable(submit_button_selector)
#         )
#         # submit_button.click()
#         driver.execute_script("arguments[0].click();", submit_button)
#         print("✅ Đã nhấn nút 'Paraphrase Text'. Chờ kết quả...")
#         time.sleep(2)
#         print("🕵️ Test hoàn thành...")
#         # 5. Chờ kết quả
#         result_container_selector = (By.CSS_SELECTOR, ".result-container.margin-v-15")
#         WebDriverWait(driver, 60).until(
#             EC.presence_of_element_located(result_container_selector)
#         )
#         print("✅ Container ket qua da xuat hien.")
#         time.sleep(2)  # Chờ một chút để kết quả được cập nhật
#         print("🕵️ Đang tìm nút copy với selector 'div.copy-icon-div'...")
#         copy_button_selector = (By.CSS_SELECTOR, "div.copy-icon-div")
#         copy_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(copy_button_selector)
#         )
#         copy_button.click()
#         print("✅ Đã nhấn nút copy.")
#         # 6. Lấy kết quả
#         time.sleep(1)  # Chờ một chút để kết quả được cập nhật
#         paraphrase_result = pyperclip.paste()
#         print("✅ Đã lấy kết quả từ clipboard.")
            
#     except Exception as e:
#         print(f"❌ Đã xảy ra lỗi trong quá trình tự động hóa: {e}")
#         print("💡 GỢI Ý: Hãy kiểm tra lại các selector khác (URL, input, submit, result-container) xem đã chính xác chưa.")
#     finally:
#         print("✅ Hoàn thành. Đóng trình duyệt.")
#         if 'driver' in locals():
#             driver.quit()
#     return paraphrase_result

#---------------------------

def paraphrase_on_zerogpt(driver, text: str):
    """
    Sử dụng một trình duyệt (driver) đã có sẵn để paraphrase văn bản.
    Hàm này sử dụng các selector do người dùng cung cấp và được tối ưu để chạy trong vòng lặp.
    """
    paraphrase_result = ""
    
    try:
        # --- BƯỚC 1: NHẬP VĂN BẢN ---
        # Sử dụng selector bạn cung cấp
        input_box_selector = (By.ID, "textArea")
        print("  -> Đang tìm ô nhập liệu...")
        input_box = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable(input_box_selector)
        )
        input_box.clear()
        input_box.send_keys(text)
        print("  -> Đã nhập văn bản gốc.")

        # --- BƯỚC 2: NHẤN NÚT PARAPHRASE ---
        # Sử dụng selector bạn cung cấp
        submit_button_selector = (By.XPATH, "//button[@class='scoreButton' and text()='Paraphrase Text']")
        print("  -> Đang tìm nút Paraphrase...")
        submit_button = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located(submit_button_selector)
        )
        # Sử dụng JavaScript click để tránh lỗi bị che khuất
        driver.execute_script("arguments[0].click();", submit_button)
        print("  -> Đã nhấn nút 'Paraphrase Text'. Chờ kết quả...")

        # --- BƯỚC 3: CHỜ KẾT QUẢ ---
        # Sử dụng selector bạn cung cấp và chờ cho đến khi nó hiển thị
        result_container_selector = (By.CSS_SELECTOR, ".result-container.margin-v-15")
        print("  -> Đang chờ container kết quả xuất hiện...")
        WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located(result_container_selector)
        )
        print("  -> Container kết quả đã xuất hiện.")
        time.sleep(3)  # Chờ một chút để kết quả được cập nhật

        # --- BƯỚC 4: NHẤN NÚT COPY ---
        # Sử dụng selector bạn cung cấp
        copy_button_selector = (By.CSS_SELECTOR, "div.copy-icon-div")
        print("  -> Đang tìm nút copy...")
        copy_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(copy_button_selector)
        )
        copy_button.click()
        print("  -> Đã nhấn nút copy.")

        # --- BƯỚC 5: LẤY KẾT QUẢ TỪ CLIPBOARD ---
        time.sleep(2)  # Chờ một chút để clipboard kịp cập nhật
        paraphrase_result = pyperclip.paste()
        print("  -> Lấy kết quả từ clipboard thành công!")
        
    except Exception as e:
        print(f"  -> ❌ Đã xảy ra lỗi trong quá trình tự động hóa cho văn bản này: {e}")
        # Nếu có lỗi, ta nên refresh lại trang để đảm bảo trạng thái "sạch" cho lần tiếp theo
        print("  -> Gặp lỗi, đang làm mới lại trang để thử lại ở lần sau...")
        driver.refresh()

    paraphrase_result = paraphrase_result.strip()  # Loại bỏ khoảng trắng thừa
    time.sleep(1)  # Chờ một chút trước khi kết thúc hàm
    return paraphrase_result
