# Cipher wheel with a function for finding an element in a list
# find_in_list function defined here but not called
# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
# this should return the position of the "query" in the "mainlist
# encrypt_message function defined here but not called
# this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
# for character in msg
# decrypt_message function defined here but not called
# this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
# methods should return or print the new messages.
############################################### Code starts from here ##################################################


    # mainlist_len = len(query)
    # range_for_loop = range(mainlist_len)
    # # index = None
    # for i in range_for_loop:
    #     element = mainlist[i]
    #     if element == query:
    #         index = i
    # return i
    # for character in plain_msg:
    # for character in decrypted_msg:
# def find_in_list(query, mainlist):
#     a=0
#     while a<len(mainlist):
#         if query==mainlist[a]:
#             return a
#         a=a+1

# chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# def encrypt_message(plain_msg):
#     encrypted_msg = ""
    
#     i=0
#     while i<len(plain_msg):
#         if plain_msg[i] in chars:
#             char_index = find_in_list(plain_msg[i], chars)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char
#         else:
#            encrypted_msg = encrypted_msg + plain_msg[i]
#         i=i+1
#     return encrypted_msg       
# def decrypt_message(encrypted_msg):
#     decrypted_msg = ""
    
#     i=0
#     while i<len(encrypted_msg):
#         if encrypted_msg[i] in shifted_chars:
#             char_index = find_in_list(encrypted_msg[i], shifted_chars)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + encrypted_msg[i]
#         i=i+1
#     return decrypted_msg
# flag = True
# while flag == True:
#     choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter e or d respectively!")
#     if choice == '1':
#        plain_message = input("Enter message to encrypt??")
#        print(encrypt_message(plain_message))
#     elif choice == '2':
#        encrypted_msg = input("Enter message to decrypt?")
#        print(decrypt_message(encrypted_msg))
#     play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
#     if play_again == 'Y':
#         continue
#     elif play_again == 'N':
#         break

    # mainlist_len = len(query)
    # range_for_loop = range(mainlist_len)
    # index = None
def find_in_list(query, mainlist):
    for i in range(0,len(mainlist)):
        element = mainlist[i]
        if element == query:
            return i
chars =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in range(0,len(plain_msg)):
        if plain_msg[character] in chars:
            char_index = find_in_list(plain_msg[character], chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
    return encrypted_msg

def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in range(0,len(encrypted_msg)):
        if encrypted_msg[character] in shifted_chars:
            char_index = find_in_list(encrypted_msg[character], shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
    return decrypted_msg
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter e or d respectively!")
    if choice == '1':
        plain_message = input("Enter message to encrypt??")
        print(encrypt_message(plain_message))
    elif choice == '2':
        encrypted_msg = input("Enter message to decrypt?")
        print(decrypt_message(encrypted_msg))
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y':
        continue
    elif play_again == 'N':
        break