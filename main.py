import logging
import log_config
from grafic_interface import gui_view
from models import Contacts

log_config.set_logging_conf()


data = Contacts().get('people')
logging.info('Запуск работы программы')
gui_view(data)
logging.info('Завершение работы программы')
