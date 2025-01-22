import time
import pyautogui
import tkinter as tk
from tkinter import filedialog, messagebox
import threading  # 用於多線程運行

# 全局變量
button_image_path = None  # 用戶上傳的按鈕圖片路徑
is_monitoring = False     # 用於控制是否啟動監控
click_count = 0           # 計算點擊次數
monitor_interval = 1      # 默認監控間隔時間（秒）

def find_and_click_button():
    """查找按鈕圖片並點擊"""
    global is_monitoring, click_count

    while is_monitoring:
        if button_image_path is not None:
            try:
                # 調試輸出圖片檢測流程
                print(f"正在搜索圖片: {button_image_path}")
                location = pyautogui.locateCenterOnScreen(button_image_path, confidence=0.8)
                if location:
                    print(f"匹配成功！位置：{location}")
                    pyautogui.click(location)  # 點擊按鈕
                    click_count += 1           # 點擊次數+1
                    update_click_count_label() # 更新點擊次數顯示
                else:
                    print("未檢測到圖片匹配...")
            except Exception as e:
                print(f"檢測圖片過程中出現錯誤: {e}")

        # 使用用戶指定的監控時間間隔
        time.sleep(monitor_interval)

def start_monitoring():
    """啟動監控"""
    global is_monitoring, monitor_interval

    if not button_image_path:
        messagebox.showerror("錯誤", "請先上傳按鈕的圖片！")
        return

    # 從輸入框獲取監控間隔時間
    try:
        interval = float(interval_entry.get())
        if interval <= 0:
            raise ValueError("監控間隔時間必須大於 0")
        monitor_interval = interval  # 設置全局監控間隔
    except ValueError:
        messagebox.showerror("錯誤", "請輸入正確的監控間隔時間（必須為正數）")
        return

    is_monitoring = True
    monitor_thread = threading.Thread(target=find_and_click_button)
    monitor_thread.setDaemon(True)  # 子線程隨主程式結束
    monitor_thread.start()
    messagebox.showinfo("提示", "監控已啟動！")

    # 禁用「上傳圖片」和「開始」按鈕
    upload_button.config(state='disabled')
    start_button.config(state='disabled')

def stop_monitoring():
    """暫停監控"""
    global is_monitoring
    is_monitoring = False
    messagebox.showinfo("提示", "監控已暫停！")

    # 恢復「上傳圖片」和「開始」按鈕為可用
    upload_button.config(state='normal')
    start_button.config(state='normal')

def upload_image():
    """上傳按鈕圖片"""
    global button_image_path
    file_path = filedialog.askopenfilename(
        title="選擇按鈕圖片",
        filetypes=[("圖片文件", "*.png;*.jpg;*.jpeg;*.bmp"), ("所有文件", "*.*")]
    )
    if file_path:
        button_image_path = file_path
        messagebox.showinfo("上傳成功", f"按鈕圖片已上傳：\n{file_path}")
    else:
        messagebox.showwarning("提示", "未選擇圖片.")

def update_click_count_label():
    """更新點擊次數的標籤顯示"""
    click_count_label.config(text=f"已點擊次數：{click_count}")

# 創建 Tk 窗體
root = tk.Tk()
root.title("按鈕自動點擊工具")

# 上傳按鈕圖片按鈕
upload_button = tk.Button(root, text="上傳按鈕圖片", command=upload_image)
upload_button.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# 監控時間間隔輸入框和標籤
interval_label = tk.Label(root, text="監控時間間隔（秒）：")
interval_label.grid(row=1, column=0, padx=10)
interval_entry = tk.Entry(root, width=10)
interval_entry.insert(0, "1")  # 預設值為 1 秒
interval_entry.grid(row=1, column=1, padx=10)

# 開始與暫停按鈕
start_button = tk.Button(root, text="開始", command=start_monitoring)
start_button.grid(row=2, column=0, pady=10)

stop_button = tk.Button(root, text="暫停", command=stop_monitoring)
stop_button.grid(row=2, column=1, pady=10)

# 點擊次數顯示
click_count_label = tk.Label(root, text="已點擊次數：0", font=("Arial", 12))
click_count_label.grid(row=3, column=0, columnspan=2, pady=10)

# 運行 Tk 窗體
root.mainloop()
