# 假设有一个base64编码的字符串
import base64
import binascii

base64_str = "w0Z9YFnsHsB4sgYLup7Y5hfy3syjyvmwAASfLN2HmcYQsZQVQhzts2lt8dx6x3rREHGYn8IlawTw752jrvWvcVyhUNOzx8AlJ8W3EWaW1svzhee+lSSdBfvHtIfU6WHz8fuSm4RgQWI7yz097PYelPrqTpM3YVigY49olP2cMSjFFCysnA3NeLevlmPkL9RwsXyUyt84tiIarUiFN5pNECMHZOuNJfbThQcDnBEqIdhHCOp5VW/XhDVSnSob6jGBRJvIjLXrO1fzMCEWCP5FGDGxbzZ0UrjjcpF6MFdAEXeFuQ8cjbHAps74jq1wWPWU++n52XGNgSYGQjdjKI12zQ=="

# 解码base64字符串
decoded_data = base64.b64decode(base64_str)

# 将解码后的数据转换为16进制字符串
hex_str = binascii.hexlify(decoded_data).decode('utf-8')

print(hex_str)
print(len(hex_str))
# # print(len(hex_str))
#
#
# def convert_endianness(hex_string):
#     # 将16进制字符串转换为整数
#     num = int(hex_string, 16)
#     # 使用按位非操作来交换字节的高低位
#     return hex(num & 0xFF)[-2:].upper() + \
#            hex((num >> 8) & 0xFF)[-2:].upper() + \
#            hex((num >> 16) & 0xFF)[-2:].upper() + \
#            hex((num >> 24) & 0xFF)[-2:].upper()
#
#
# # 示例
# original_hex = "12345678"
#
# converted_hex = convert_endianness(original_hex)
# print(f"Original: {original_hex}")
# print(f"Converted: {converted_hex}")
# hex_str1 = "1A2B3C4"  # 假设是一个8位16进制数
#
#
# def change_to_hex(hex_str):
#     # 使用格式化字符串补零并转换
#     padded_hex_str = format(int(hex_str, 16), '08X')
#
#     # 或者使用f-string
#     # padded_hex_str = f'{int(hex_str, 16):08X}'
#
#     # 输出结果
#     print(padded_hex_str)  # 输出: 0001A2B3C4D
#     return padded_hex_str
#
#
# # 如果需要转换为字节
# # byte_str = padded_hex_str.encode('utf-8')
# #
# # # 输出结果
# # print(byte_str)  # 输出: b'\x00\x01\x2B\x3C\x4D'
#
# string = "1dc869c2-1a192-36c8e3ce-5492ac1e"
# new_hex = ''
# parts = string.split('-')
# print(parts)  # 输出: ['this', 'is', 'a', 'test']
# for i in parts:
#     new_hex += convert_endianness(i)
# new_hex2=new_hex.replace('X','0')
# print(new_hex2.lower()=='c269c81d92a10100cee3c8361eac9254')
# print(new_hex2)