import pyautogui
import time
import os
time.sleep(5)

def capture_screenshot(output_path):
    # 获取屏幕尺寸
    screen_width, screen_height = pyautogui.size()

    # 截取全屏并保存到指定路径
    screenshot = pyautogui.screenshot()
    screenshot.save(output_path)


if __name__ == "__main__":
    try:
        # 指定保存截屏的文件路径
        save_path = r"C:\Users\28412\Pictures\Screenshots"
        os.makedirs(save_path, exist_ok=True)

        while True:
            # 每隔一秒截取全屏
            timestamp = int(time.time())
            file_name = f"screenshot_{timestamp}.png"
            file_path = os.path.join(save_path, file_name)

            capture_screenshot(file_path)
            # 获取当前鼠标位置
            x, y = pyautogui.position()

            # 模拟鼠标左键点击
            pyautogui.click(x, y)
            print(f"截屏已保存到 {file_path}")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n截屏脚本已终止.")
