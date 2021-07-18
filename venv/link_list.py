# Узел
class Node :
    def __init__ (self , dataval = None) :
        self.dataval = dataval
        self.nextval = None

# Список связанный
class LinkedList :
    def __init__ (self) :
        self.headval = None
# Чтение списка
    def PrintList (self):
        printval = self.headval
        while printval is not None :
            print ( printval.dataval )
            printval = printval.nextval
# Вставка в начало
    def AtBeginning (self , new_val) :
        new_node = Node ( new_val )
        new_node.nextval = self.headval
        self.headval = new_node

# Вставка в конец
    def AtEnd (self , new_val) :
        new_node = Node ( new_val )
        if self.headval is None :
            self.headval = new_node
        last = self.headval
        while last.nextval :
            last = last.nextval
        last.nextval = new_node

# Вставка между значениями
    def InBetween (self , middle_node , new_val) :
        if middle_node is None :
            print ( "Указанный узел отсутствует" )
            return

        new_node = Node ( new_val )
        new_node.nextval = middle_node.nextval
        middle_node.nextval = new_node

if __name__ == '__main__':

    list_1 = LinkedList ()
    list_1.headval = Node ( 'Mon' )
    val_2 = Node ( 'Tue' )
    val_3 = Node ( 'Wed' )

    list_1.headval.nextval = val_2
    val_2.nextval = val_3

    list_1.AtBeginning ( 'Sun' )
    list_1.AtEnd ( 'Fri' )
    list_1.InBetween ( val_3 , 'Thu' )
    list_1.AtEnd ( 'Sat' )

    list_1.PrintList ()
