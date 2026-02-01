from kivymd.app import MDApp
from kivy.uix.webview import WebView
from kivy.uix.widget import Widget
from kivy.core.window import Window

class StockAnalysisApp(MDApp):
    def build(self):
        self.icon = 'assets/logo.png'
        Window.clearcolor = (1, 1, 1, 1)
        webview = WebView(url='https://marketnite-2.onrender.com')
        return webview

if __name__ == '__main__':
    StockAnalysisApp().run()