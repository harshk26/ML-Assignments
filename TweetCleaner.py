'''
Contains a class for rudimentary cleaning of tweets. Removes Tweet Id's, Whitespaces, Emojis and Hashtags. Replaces @ mentions with **NAME**. Edited File is created as a new file.
'''

import re
import os

class Tweet_Cleaner:

    def __init__(self, FileInput, FileOutput):
        self.FileInput = FileInput
        self.FileOutput = FileOutput

    def Convert_To_String(self, FileInput):
        file = open(FileInput, 'r')
        string = file.read()
        file.close()
        return string

    def Remove_Emotions(self, FileInput):
        str = self.Convert_To_String(FileInput)
        print('Removing Emotions')
        newstr = ''
        for line in str.splitlines():
            pattern =  re.compile(r':: \w+')
            newstr += re.sub(pattern, '', line) + '\n'
        return newstr

    def Remove_TweetID(self, FileInput):
        str = self.Remove_Emotions(FileInput)
        print('Removing Tweet ID')
        list = str.split('\n')
        newstr = ''
        for line in list:
            ctr = 0
            for char in line:
                if char.isalpha() == False:
                    ctr+=1
                else:
                    break
            newstr += line[ctr:]
        return newstr

    def Remove_Whitespace(self, FileInput):
        str = self.Remove_TweetID(FileInput)
        print ('Removing Whitespaces')
        list = str.split('\t')
        newstr = ''
        for line in list:
            newstr += line + '\n'
        return newstr

    def Remove_Emojis(self, FileInput):
        str = self.Remove_Whitespace(FileInput)
        print ('Removing Emojis')
        list = str.split('\n')
        newstr = ''
        for line in list:
            EmojiPattern = re.compile(r'[():-;\[\]]+')
            newstr += EmojiPattern.sub("", line) + '\n'
        return newstr

    def Remove_AtMentions(self, FileInput):
        str = self.Remove_Emojis(FileInput)
        print ('Replacing @mentions with **NAME**')
        list = str.split('\n')
        newstr = ''
        for line in list:
            Pattern = re.compile(r'@\w+')
            newstr += Pattern.sub(r'**NAME**', line) + '\n'
        return  newstr

    def Remove_Hashtags(self, FileInput):
        str = self.Remove_AtMentions(FileInput)
        print ('Removing # instances')
        list = str.split('\n')
        newstr = ''
        for line in list:
            pattern = re.compile(r'#')
            newstr += re.sub(pattern, '', line) + '\n'
        return newstr

    def Write_To_File(self, FileInput, FileOutput):
        str = self.Remove_Hashtags(FileInput)
        print ('Writing Edited File')
        newfile = open(FileOutput, 'w')
        newfile.write(str)
        newfile.close()

Testing = Tweet_Cleaner(r'C:\Users\Guls HP\Desktop\Python 2018\jan9-2012.txt', 'EditedFile.txt')
Testing.Write_To_File(r'C:\Users\Guls HP\Desktop\Python 2018\jan9-2012.txt', 'EditedFile.txt')
