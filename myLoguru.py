import datetime

from loguru import logger

# 設定程式記錄除了輸出到 Terminal，還要輸出到紀錄檔案
# 輸出檔案規則
# [1] 一天保存一份紀錄檔案
# [2] 清除超過七天以上的紀錄檔案
# [3] 保存權重在 DEBUG 以上的紀錄
logger.add(
    f'{datetime.date.today():%Y%m%d}.log',
    rotation='1 day',
    retention='7 days',
    level='DEBUG'
)



# TRACE
# 權重 5
logger.trace('<message>')

# DEBUG
# 權重 10
logger.debug('<message>')

# INFO
# 權重 20
logger.info('<message>')

# SUCCESS
# 權重 25
logger.success('<message>')

# WARNING
# 權重 30
logger.warning('<message>')

# ERROR
# 權重 40
logger.error('<message>')

# CRITICAL
# 權重 50
logger.critical('<message>')