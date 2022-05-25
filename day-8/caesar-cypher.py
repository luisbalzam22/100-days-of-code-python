from re import match

WELCOME_MESSAGE: str = "Welcome to the \"Caesar Cypher\" program"
ENCRYPTION_DECRIPTION_PROMPT_MSG: str = "Do you wanna encrypt or decrypt? (enc / dec)\n"
GET_MESSAGE_PROMPT_MSG: str = "Now, enter the secret message\n"
SHIFTING_PROMPT_MSG: str = "Please, type the shifting offset (integer)\n"
CONTINUE_CIPHERING_PROMPT_MSG: str = "Do you wnat to continue cyphering? (y/n)\n"
ASCII_RANGES: int = 25
ASCII_FIRST_LAST_CHAR_INDEXES: "list[int]" = [97, 122]

def cleanse_offset(shift: int) -> int:
    if (shift >= 0):
        return shift % ASCII_RANGES
    return shift % -ASCII_RANGES
    

def shift_ascii(char :str, shift: int) -> str:
    if shift > 0:        
        if ord(char) + shift > ASCII_FIRST_LAST_CHAR_INDEXES[1]:
            return chr(ASCII_FIRST_LAST_CHAR_INDEXES[0]  + (ord(char) + shift - ASCII_FIRST_LAST_CHAR_INDEXES[1] -1))
    else:
        if ord(char) + shift < ASCII_FIRST_LAST_CHAR_INDEXES[0]:
            return chr(ASCII_FIRST_LAST_CHAR_INDEXES[1]  - ( ASCII_FIRST_LAST_CHAR_INDEXES[0] - (ord(char) + shift)) + 1)
            
    return chr(ord(char) + shift)
    
def crypt(message: str, shift : int) -> str:
    offset = cleanse_offset(shift)
    resulting_msg = ''
    for letter in message:
        if match("[a-z]",letter):    
            resulting_msg += shift_ascii(letter, offset)
        else:
            resulting_msg += letter
    return resulting_msg

continue_ciphering: bool = True

while (continue_ciphering):
    print(WELCOME_MESSAGE)
    raw_msg = input(GET_MESSAGE_PROMPT_MSG).lower()
    shifting = int(input(SHIFTING_PROMPT_MSG))

    print(crypt(raw_msg, shifting))
    continue_ciphering = input(CONTINUE_CIPHERING_PROMPT_MSG).lower() == 'y'