import logging

# 创建一个logger
logger = logging.getLogger('error_logger')
logger.setLevel(logging.DEBUG)  # 设置日志级别

# 创建一个handler，用于将日志写入磁盘文件
file_handler = logging.FileHandler('./log/error_log.log')
file_handler.setLevel(logging.DEBUG)

# 创建一个handler，用于将日志输出到控制台
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)  # 只输出错误及以上级别的日志

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 将handlers添加到logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# 测试日志输出
