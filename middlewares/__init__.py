from .big_brothers import BigBrother
from main import dp

if __name__ == "middlewares":
    dp.middleware.setup(BigBrother)