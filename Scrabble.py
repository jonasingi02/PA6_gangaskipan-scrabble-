# veit ekki alveg hvar ég á að byrja í þessu verkefni enn þetta gæti alveg verið ágætis borð
# svo væri hægt að hafa bara if slikirði í innstu for lykkjunni til þess að um það hvort einhver bókstafur ætti að koma þar.git 
class Board:
    def __init__(self) -> None:
        pass
    def __str__(self) -> None:
        ret_str= ""
        for i in range(15):
           ret_str = ret_str + " _"
        ret_str = ret_str + "\n"
        for i in range(15):
            for j in range(15):
                ret_str = ret_str + "|_"
            ret_str = ret_str + "|\n"
        return ret_str





a = Board()
print(a)

 



