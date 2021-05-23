"""
import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn("Для выполнения этой программы необходима как минимум \
            версия Python 3.0",
    RuntimeWarning)
else:
    print('Нормальное продолжение')"""
"""
import os, platform, logging
if platform.platform().startswith('Windows'):
    print("go")
    logging_file = "C:\\Users\\Charcharadon Astra\\Desktop\\Питон\\PYTHON XIOMI\\Sandbox\\test.log"
    """os.path.join(os.getenv('C:\\'),
                                os.getenv("Users\\Charcharadon Astra\\Desktop\\Питон\\PYTHON XIOMI\\Sandbox\\"),
                                'test.log')"""
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
    print("Сохраняем лог в", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)
logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умирает")"""