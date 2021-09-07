import utils
import sys

for i in sys.argv[1:]:
    print(utils.currency_rates(i))