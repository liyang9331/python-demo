import logging

# 创建日志记录器
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# 创建处理器并设置其级别
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# 创建日志消息格式化器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 添加处理器到日志记录器
logger.addHandler(file_handler)

# 记录日志消息
# logger.debug('这是一个debug级别的日志')
# logger.info('这是一个info级别的日志')
# logger.warning('这是一个warning级别的日志')
# logger.error('这是一个error级别的日志')
# logger.critical('这是一个critical级别的日志')
