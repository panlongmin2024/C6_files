def convert_hex(hex_str):
    # 确保输入是7位16进制数
    assert len(hex_str) == 7
    # 将16进制数的高低位交换，并补零
    return '{:07x}'.format(int(hex_str, 16))


# 示例使用
original_hex = "1234567"
converted_hex = convert_hex(original_hex)
print(f"原始7位16进制数: {original_hex}")
print(f"转换后的7位16进制数: {converted_hex}")