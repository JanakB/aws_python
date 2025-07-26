def encryption(shift):
    ptext="CRYPTOGRAPHY"
    shift=shift if shift>0 else 26+shift
    ctext=[chr((((int(ord(i))-65)+shift)%26)+65) for i in ptext]
    ctext="".join(ctext)
    return ctext

print("Encrypted text : "+encryption(3))

def decryption(shift):
    ptext=encryption(shift)
    shift=(shift if shift>0 else 26+shift)*-1
    ctext=[chr((((int(ord(i))-65)+shift)%26)+65) for i in ptext]
    ctext="".join(ctext)
    return ctext
print("Decrypted text : "+decryption(3))
