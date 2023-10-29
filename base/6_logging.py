"""
Логирование
"""
import logging
import requests

import secrets


class TelegramHandler(logging.Handler):
    """Handler для отправки логов в телеграм."""

    def __init__(self, token, chat_id):
        super().__init__()

        self.token = token
        self.chat_id = chat_id

    def send_message_to_telegram(self, message: str) -> None:
        """Отправляет сообщение в телеграм."""
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        data = {
            'chat_id': self.chat_id,
            'text': message
        }
        requests.post(url=url, json=data)

    def emit(self, record: logging.LogRecord) -> None:
        """
        Зарегистрировать запись лога.

        Данный метод защищён от возможных ошибок, чтобы ошибка при логировании не повлияла на работу кода.
        """
        try:
            message = self.format(record)
            self.send_message_to_telegram(message)
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)


def create_tg_logger(name: str) -> logging.Logger:
    """Создать telegram Logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.DEBUG)
    handler = TelegramHandler(secrets.TOKEN, secrets.CHAT_ID)
    handler.formatter = logging.Formatter('%(levelname)s: LOGGER: %(name)s TIME: %(asctime)s: MESSAGE: %(message)s')
    logger.addHandler(handler)

    return logger


def main() -> None:
    """Тестовое логирование."""
    logger = create_tg_logger('test-logger')

    print('До')
    logger.critical('qweqwe, ой беда все сюда')
    print('После')


if __name__ == '__main__':
    main()
