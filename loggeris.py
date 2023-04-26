import logging

# logging.basicConfig(level=logging.DEBUG)

# logging.basicConfig(level=logging.INFO, filename="istorija.log", format="%(asctime)s, %(name)s, %(levelname)s, %(message)s")




logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s, %(name)s, %(levelname)s, %(message)s")
file_handler = logging.FileHandler("istorija.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(level)s:%(name)s"))
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.debug("PERSPEJIMAS")
                             
class produktas:
    def __init__(self, **kwargs) -> None:
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])
            logger.info(f"kuriamo produkto {kwarg}={kwargs[kwarg]}")

daiktas = produktas(pavadinimas="daiktas")
kitas = produktas(pavadinimas="kitas daiktas", kaina=1.99)

try:
    skaicius = 10 / 0
except ZeroDivisionError as error:
    logger.exception("KLAIDA: %s", error)

        