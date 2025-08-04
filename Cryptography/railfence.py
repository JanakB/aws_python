def rail_fence_encrypt(message):
    rail1 = ''
    rail2 = ''
    rail3 = ''
    rail = rail1
    direction = 1

    for letter in message:
        rail += letter

        if rail == rail1:
            direction = 1
        elif rail == rail3:
            direction = -1

        if direction == 1:
            if rail == rail2:
                rail = rail3
            elif rail == rail1 + message[-1]:
                rail = rail2
        else:
            if rail == rail2:
                rail = rail1
            elif rail == rail3 + message[-1]:
                rail = rail2

    return rail1 + rail2 + rail3

choice = int(input("Enter choice 1 for encryption and 2 for decryption:"))
if(choice==1):
    pt = input("Enter plaintext:")
    print("Plaintext"+rail_fence_encrypt(pt))
elif(choice==2):
    ct = input("Enter ciphertext:")
    print(railfence_decrypt(ct))

