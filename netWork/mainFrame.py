# -*- coding: utf-8 -*-
import cookielib
import httplib
import urllib
import urllib2
import cStringIO

__author__ = 'lidong'
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame")
        self.panel = wx.Panel(self, -1)
        # panel.Bind(wx.EVT_MOTION,  self.OnMove)
        self.button = wx.Button(self.panel,
                        label="Not Over", pos=(100, 15))
        self.panel.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)    #1 绑定按钮事件
        # wx.StaticText(panel, -1, "name:",(10, 10))
        # wx.StaticText(panel, -1, "pwd:",(10, 30))
        self.posCtrl = wx.TextCtrl(self.panel, -1,pos=(10,10))
        self.posCtrl1 = wx.TextCtrl(self.panel, -1,pos=(10,50))
        self.posCtrl3 = wx.TextCtrl(self.panel, -1,pos=(10,100))
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj));
        urllib2.install_opener(self.opener);
        image_url = "https://sso.woniu.com/captcha"
        image_bytes = self.opener.open(image_url).read()
        data_stream = cStringIO.StringIO(image_bytes)
        bmp = wx.BitmapFromImage(wx.ImageFromStream(data_stream))
        wx.StaticBitmap(self.panel, -1, bmp, pos=(50, 120))

    def OnMove(self, event):
        pos = event.GetPosition()
        # self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))
    def OnButtonClick(self, event):
        print(self.posCtrl.GetValue())
        print(self.posCtrl1.GetValue())
        print(self.posCtrl3.GetValue())
        params = urllib.urlencode({
            'username': self.posCtrl.GetValue(),
            'password': self.posCtrl1.GetValue(),
            'captcha': self.posCtrl3.GetValue(),
            '_eventId': "submit",
            '_submit': "true",
        })





        self.opener.add_handler = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'),
            ("Content-type","application/x-www-form-urlencoded"),
            ("Accept","text/plain")
                              ]
        op= urllib2.urlopen('https://sso.woniu.com/login',params)
        data= op.read()
        print(data)
        print self.cj._cookies.values()


        for index, cookie in enumerate(self.cj):
           print '[',index, ']',cookie;

        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()