import logging

try:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        filename="app.log",
    )
except Exception as e:
    print(f"logging initialization exception: {e}")