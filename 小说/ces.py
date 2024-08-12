# import keyboard  # 导入keyboard库，用于检测键盘按键
#
#
# # 定义一个函数，根据按键执行不同的操作
# def execute_action(key):
#     print('输入')
#     if key == 'Key up pressed':
#         print("执行1")
#     elif key == 'Key down pressed':
#         print("执行2")
#
#
# # 监听键盘事件
# keyboard.on_press(execute_action)
#
# # 保持程序运行，等待键盘事件
# keyboard.wait()
import keyboard


# 定义一个回调函数
def on_key_press(event):
    print(f"{event.name}")
    if event.name == 'home':
        上班()
    elif event.name == 'end':
        下班()


# 监听键盘按键，回调函数为on_key_press
keyboard.on_press(on_key_press)
keyboard.wait('q')  # 等待用户按下'q'键后停止监听
