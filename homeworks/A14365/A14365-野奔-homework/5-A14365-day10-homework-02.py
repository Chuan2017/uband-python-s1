#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
#作业一：只用改一处老爸
#作业二：改一处tear_word= "abase"和 if not serach
#作业四：调用两次search函数即可

# 实现了和 homework01 一样的功能
# 供你分析和对比
def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老妈'
  tear_word = 'abase' #可能会被撕毁的页的key

  print '%s在看一本英文书 ' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)

    if not search('abase', book, who):
      #老爸黏贴了代码
      book[tear_word] = tear_mean
      print '%s把 %s 的字典页又贴上了' % (who, tear_word)
  who = '老爸'
  search('abase',book,who)
  search('abash',book,who)


def search(key, dictionary, who):
  if dictionary.has_key(key):
    print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  homework2()