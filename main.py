from sjtuMessageClient import *
from FeishuClient import FeishuClient
import pandas
import sys

def format_display(tgs):
    columns = ['time', 'titles']
    data = [[time[1], title] for time, title in zip(list(tgs.values()), list(tgs.keys()))]
    table = pandas.DataFrame(data, columns=columns)
    return table

if __name__ == "__main__":
    feishuclient = FeishuClient()
    tgs = get_tg()
    tgs = AI_summarize(tgs)
    format_tgs = format_display(tgs)
    feishuclient.send(format_tgs.to_string())
    while True:
        print(format_tgs)
        print('------------------------------')
        index = input("input the news_index you want to check, enter 'q' to quit the program: ")
        if index == 'q':
            sys.exit()
        elif not index.isdigit():
            print('Invalid index')
            continue
        flag = input('summarization or the detailed information? y/n: ')
        content = tgs[list(tgs.keys())[int(index)]]
        if flag == 'y':
            print(content[2])
            feishuclient.send(content[2])
        elif flag == 'n':
            print(content[3])
            feishuclient.send(content[3])
        else:
            print('invalid input')
        


