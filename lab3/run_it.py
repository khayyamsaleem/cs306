import os

algs_minkeys = [('DES',56), ('TripleDES',112), ('RC2',40), ('AES',128), ('Blowfish',32)]
modes_of_operation = ['ECB', 'CBC', 'OFB', 'PCBC']
ITERATIONS = 100000
msg = "\"I am a superstar\""

# All algorithms, ECB
for alg,keysize in algs_minkeys:
    runCmd="java SymmetricKeyTest {} {} {} {} {}".format(alg, keysize, 'ECB', ITERATIONS, msg)
    os.system('echo "COMMAND: ' + runCmd + '\n" >> out.txt')
    os.system(runCmd + " >> out.txt")
    os.system('echo "--------------------\n" >> out.txt')

# AES, all modes of operation
for m in modes_of_operation:
    runCmd = "java SymmetricKeyTest {} {} {} {} {}".format('AES', 192, m, ITERATIONS, msg)
    os.system('echo "COMMAND: '+ runCmd + '\n" >> aes_out.txt')
    os.system(runCmd + " >> aes_out.txt")
    os.system('echo "--------------------\n" >> aes_out.txt')

# RC2, ECB, (64, 512 ,1024)
for keysize in (64, 512, 1024):
    runCmd = "java SymmetricKeyTest {} {} {} {} {}".format('RC2', keysize, 'ECB', ITERATIONS, msg)
    os.system('echo "COMMAND: '+ runCmd + '\n" >> rc2_ecb_out.txt')
    os.system(runCmd + " >> aes_out.txt")
    os.system('echo "--------------------\n" >> rc2_ecb_out.txt')

# AES, varying msg lengths
for m in ("I am a superstar", "c", "9428urho1icu3bo123itybo23giybv2o4uybgo2uyrbfo2fyb2o4fuyb"):
    runCmd = "java SymmetricKeyTest {} {} {} {} {}".format('AES', 128, 'ECB', ITERATIONS, m)
    os.system('echo "COMMAND: '+ runCmd + '\n" >> aes_vmsg_out.txt')
    os.system(runCmd + " >> aes_out.txt")
    os.system('echo "--------------------\n" >> aes_vmsg_out.txt')
