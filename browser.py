from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QTabWidget, QPushButton, QLineEdit

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.addTab(self.create_new_tab("https://www.google.com"), "New Tab")
        self.tabs.setCurrentIndex(0)

        self.new_tab_button = QPushButton("New Tab")
        self.new_tab_button.clicked.connect(self.create_new_tab_with_button)

        self.search_field = QLineEdit()
        self.search_field.returnPressed.connect(self.load_url)

        self.setWindowTitle("CodeComets Browser v2")

        layout = QVBoxLayout(self)
        layout.addWidget(self.tabs)
        layout.addWidget(self.search_field)
        layout.addWidget(self.new_tab_button)

    def create_new_tab(self, url):
        view = QWebEngineView()
        view.load(QUrl(url))
        view.titleChanged.connect(lambda title, view=view: self.update_title(title, view))
        view.iconChanged.connect(lambda icon, view=view: self.update_icon(icon, view))
        return view

    def update_title(self, title, view):
        index = self.tabs.indexOf(view)
        if index != -1:
            self.tabs.setTabText(index, title)

    def update_icon(self, icon, view):
        index = self.tabs.indexOf(view)
        if index != -1:
            self.tabs.setTabIcon(index, icon)

    def close_tab(self, index):
        self.tabs.removeTab(index)
        if self.tabs.count() == 0:
            self.close()
   
    def create_new_tab_with_button(self):
        self.tabs.addTab(self.create_new_tab("https://www.google.com"), "New Tab")
        self.tabs.setCurrentIndex(self.tabs.count()-1)
        
    def load_url(self):
        current_tab = self.tabs.currentWidget()
        current_tab.load(QUrl(self.search_field.text()))

if __name__ == "__main__":
    app = QApplication([])
    browser = Browser()
    browser.setGeometry(50, 50, 850, 500)
    browser.show()
    app.exec_()
