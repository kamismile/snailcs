# -*- coding: utf-8 -*-
import sys
import wx
from wx.py import images

__author__ = 'lidong'
#-------------------------------------------------------------------------------
# Name:        TextCtrlExampleFrame
# Purpose:
#
# Author:      ankier
#
# Created:     17/09/2012
# Copyright:   (c) ankier 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx

class TextCtrlExampleFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, \
                          "Text ctrl example", pos =(0,0), size =(800, 600))
        panel = wx.Panel(self, -1)

        #多行文本样式
        text = wx.TextCtrl(panel, wx.ID_ANY,pos=(0,70), size =(200, 60), style = wx.TE_MULTILINE)

        #window下富文本
        text = wx.TextCtrl(panel, wx.ID_ANY,pos=(0,140), size =(200, 60), style = wx.TE_RICH)
def main():
    app = wx.PySimpleApp()
    frame = TextCtrlExampleFrame()
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()