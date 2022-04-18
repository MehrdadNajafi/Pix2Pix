from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import cv2

from model import GeneratorModel
    
class Pix2Pix_Map2Aerial(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load("ui/mainWindow.ui")
        self.ui.show()
        
        self.generator_model = GeneratorModel()
        
        self.ui.browsfile_btn.clicked.connect(self.browsFile)
        self.ui.process_btn.clicked.connect(self.process)
        
    def browsFile(self):   
        try:
            self.file_name = QFileDialog.getOpenFileName(self, "Open File", "", "Images (*.png *.jpg *.xmp, *.jpeg);; All Files (*)")
            img = cv2.imread(str(self.file_name[0]))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (256, 256))
            img = QImage(img, img.shape[1], img.shape[0], QImage.Format_RGB888)
            img = QPixmap(img)
            self.ui.input_label.setPixmap(img)
        except:
            mb = QMessageBox(QMessageBox.Warning, "Warning", "Can't load the image file, Try again")
            mb.exec()
    
    def process(self):
        generated_image = self.generator_model.generate(self.file_name[0])
        generated_image = QImage(generated_image, generated_image.shape[1], generated_image.shape[0], QImage.Format_RGB888)
        generated_image = QPixmap(generated_image)
        self.ui.output_label.setPixmap(generated_image)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = Pix2Pix_Map2Aerial()
    app.exec()