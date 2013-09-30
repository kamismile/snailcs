import urllib
import wx
# -*- coding: utf-8 -*-
from cStringIO import StringIO

__author__ = 'Administrator'
# display an image from an internet webpage
# using wxPython

import wx
import urllib2
import cStringIO

class ImagePanel(wx.Panel):
    """ create a panel with a wx.StaticBitmap """
    def __init__(self, parent, bmp, image_name):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        self.SetBackgroundColour('brown')

        # show the static bitmap
        wx.StaticBitmap(self, wx.ID_ANY, bmp, pos=(50, 40))

        # optionally show some image information
        info = "name = %s   image size = %dx%d" % \
               (image_name, bmp.GetWidth(), bmp.GetHeight())
        # the parent is the frame
        parent.SetTitle(info)


# find yourself a picture on a web page you like and then
# right click on the picture, look under properties and copy the URL
# (right click only tested on a Windows machine)
image_url = "http://sns.woniu.com/account/imgCode.do"

# extract the picture's name (optional)
image_name = image_url.split('/')[-1]

# open the image url and read bytes it into a variable
opener = urllib2.build_opener()
image_bytes = opener.open(image_url).read()

# convert image bytes to data stream
data_stream = cStringIO.StringIO(image_bytes)

app = wx.App(0)
# convert data_stream to a bitmap
bmp = wx.BitmapFromImage(wx.ImageFromStream(data_stream))
# calculate width and height needed to set the frame
# plus a little extra for the border
width = bmp.GetWidth() + 100
height = bmp.GetHeight() + 100
# create window/frame instance
frame = wx.Frame(None, wx.ID_ANY, size=(width, height))
# create the panel instance
ImagePanel(frame, bmp, image_name)
# show the frame
frame.Show(True)
# start the GUI event loop
app.MainLoop()