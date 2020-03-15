import MaxPlus
import pymxs
#import os
from PySide2 import QtWidgets, QtCore, QtGui

RT = pymxs.runtime
# max열기
# max파일 섬네일
# max파일 프리뷰
# fbx 익스포트
print("hellow max python")

class FileToolUI(QtWidgets.QDialog):

    def __init__(self, parent=MaxPlus.GetQMaxMainWindow()):
        super(FileToolUI, self).__init__(parent)
        RT.clearlistener()
        self.main_dir_path = RT.getFilenamePath(RT.maxfilepath)
        self.current_MaxFilePath = RT.getFilenamePath(RT.maxfilepath)
        self.current_maxfile_name = RT.maxFileName
        self.setWindowTitle(u"파일툴")
        self.initUI()

    def initUI(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        # 레이아웃
        self.maxfile_list_layout = QtWidgets.QVBoxLayout()
        self.inputFileNameLayout = QtWidgets.QHBoxLayout()
        self.button_layout = QtWidgets.QHBoxLayout()
        
        self.main_layout.addLayout(self.maxfile_list_layout)
        self.main_layout.addLayout(self.inputFileNameLayout)
        self.main_layout.addLayout(self.button_layout)
        # ui객체
        self.dirLabel = QtWidgets.QLabel(u"[대상 경로] " + self.main_dir_path)
        self.filesList_tree_widget = QtWidgets.QTreeWidget()
        self.filesList_tree_widget.setHeaderLabel(u"파일이름")
        self.maxFileNameEdit = QtWidgets.QLineEdit(self.current_maxfile_name, self)
        self.fileAnnotaionEdit = QtWidgets.QLineEdit(u"주석", self)
        self.saveMaxBtn = QtWidgets.QPushButton(u"max로 저장")
        self.saveFbxBtn = QtWidgets.QPushButton(u"fbx로 저장")
        self.openFolder = QtWidgets.QPushButton(u"경로 열기")

        for i in range(1,6):
            item = QtWidgets.QTreeWidgetItem(self.filesList_tree_widget)
            item.setText(0, str(i))
        
        self.maxfile_list_layout.addWidget(self.dirLabel)
        self.maxfile_list_layout.addWidget(self.filesList_tree_widget)
        self.inputFileNameLayout.addWidget(self.maxFileNameEdit)
        self.inputFileNameLayout.addWidget(self.fileAnnotaionEdit)
        
        # 레이아웃에 버튼 추가
        self.button_layout.addWidget(self.saveMaxBtn)
        self.button_layout.addWidget(self.saveFbxBtn)
        self.button_layout.addWidget(self.openFolder)

        self.openFolder.clicked.connect(self.OpenCurrentMaxFile)

        self.setLayout(self.main_layout)
        self.updateUI()
        
    def updateUI(self):
        print(u"updateUI")

    def GetFileList(self):
        pass

    def SaveMaxFile(self, fileName, annotaion):
        pass

    def ExportFBX(self, fileName):
        pass

    def InPutFileName(self, fileNameString):
        pass
    def OpenCurrentMaxFile(self):
        RT.ShellLaunch(self.current_MaxFilePath, "")

#맥스 스크립트 창에서는 사용 못함 즉 필요없음. 
#if __name__ == "__main__":
try:
    ui.close()
except:
    pass
ui = FileToolUI()
ui.show()