#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  #开始你的表演
  bran.speed(1)
  bran.forward(100)
  bran.right(45)
  bran.forward(150)
  
  

  #bran.goto(500,500)
  bran.setheading(270)
  bran.backforward(150)
  
  
if __name__ == '__main__':
  main()