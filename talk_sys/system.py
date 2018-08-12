import json

dict = {
        'noun':{
            'I'
            },
        'verb':{
            'am'
            },
        'aj':{
            'smart'
            }
       }


class DictManage:

    def addWord(self, word, word_type):

       dict[word_type] = word 

def main():

    take = DictManage()
    take.addWord('take', 'verb')

    print(dict)



main()




