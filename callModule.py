from modules.module1 import colin 
colin();

from modules.module2 import colin 
colin();

#main 是被 Python 直接執行的模組的名字。這樣的話除非直接運行該模組，if 條件下的這些程式碼是不會執行的。
if  __name__  ==  ' __main__ ' :
    colin();