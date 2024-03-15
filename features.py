import func
def greeting():
    '''
    Відображення фічі СтартоваЗаставка - зробимо коли дійдуть руки.
    На мінімалках - друк привітання.
    '''
    print("\x1b[2J")  # clean the screen
    print("Welcome to Personal Information Processor PIP-Boy-Bot-3000!\n")
    func.hello()


def goodbye():
    '''
    Відображення фічі ФінальнаЗаставка - зробимо коли дійдуть руки.
    На мінімалках - друк прощання.
    '''
    print("Good bye! I wish you to survive in this beautiful world! See you next time!")
