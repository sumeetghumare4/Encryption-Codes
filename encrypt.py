# Transposition Cipher Encrypt/Decrypt File

 2. # http://inventwithpython.com/hacking (BSD Licensed)

 3.

 4. import time, os, sys, transpositionEncrypt, transpositionDecrypt

 5.

 6. def main():

 7.     inputFilename = 'frankenstein.txt'

 8.     # BE CAREFUL! If a file with the outputFilename name already exists,

 9.     # this program will overwrite that file.

10.     outputFilename = 'frankenstein.encrypted.txt'

11.     myKey = 10

12.     myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

13.

14.     # If the input file does not exist, then the program terminates early.

15.     if not os.path.exists(inputFilename):

16.         print('The file %s does not exist. Quitting...' % (inputFilename))

17.         sys.exit()

18.

19.     # If the output file already exists, give the user a chance to quit.

20.     if os.path.exists(outputFilename):

21.         print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))

22.         response = input('> ')

23.         if not response.lower().startswith('c'):

24.             sys.exit()

25.

26.     # Read in the message from the input file

27.     fileObj = open(inputFilename)

28.     content = fileObj.read()

29.     fileObj.close()

30.

31.     print('%sing...' % (myMode.title()))

32.

33.     # Measure how long the encryption/decryption takes.

34.     startTime = time.time()

35.     if myMode == 'encrypt':

36.         translated = transpositionEncrypt.encryptMessage(myKey, content)

37.     elif myMode == 'decrypt':

38.         translated = transpositionDecrypt.decryptMessage(myKey, content)

39.     totalTime = round(time.time() - startTime, 2)

40.     print('%sion time: %s seconds' % (myMode.title(), totalTime))

41.

42.     # Write out the translated message to the output file.

43.     outputFileObj = open(outputFilename, 'w')

44.     outputFileObj.write(translated)

45.     outputFileObj.close()

46.

47.     print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))

48.     print('%sed file is %s.' % (myMode.title(), outputFilename))

49.

50.

51. # If transpositionCipherFile.py is run (instead of imported as a module)

52. # call the main() function.

53. if __name__ == '__main__':

54.     main()
