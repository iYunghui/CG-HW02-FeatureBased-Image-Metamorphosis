# CG HW02 Feature Based Image Metamorphosis

## Hardware and software requirement

* Windows 10
* Python 3.7
	* Spyder 3.3.6
	* Opencv2 3.4.2
	* PyQt5 5.15.1

## Program overview

* class `Line(object)`：紀錄feature line的起點、終點、向量、垂直線、長度平方及長度
* function `Draw_Feature_Line(event, x, y, flags, param)`：點擊滑鼠左鍵呼叫此函數畫出feature line
* function `Wrap_Feature_Line()`：點選GUI上的`WrapFeatureLine`按鈕會呼叫此函數，依據src和dst的feature line，計算出wrap image的feature line
* function `Call_Wrap_Image()`：點選GUI上的`WrapImage`按鈕會呼叫此函數，此函數會再呼叫函數`Wrap_Image`並將結果顯示出來
* function `Wrap_Image(img, wrap_line, img_line)`：使用公式計算變化後圖形
* function `Animation()`：點選`Animation`按鈕會呼叫此函數，alpha從0.1到1變化並呼叫函數`Wrap_Feature_Line()`和`Wrap_Image`來產生結果

## Operations manual

1. 若需要修改GUI介面，開啟pyqt5的designer.exe修改，修改完畢後開啟Anaconda Prompt至ui檔案位置，輸入`pyuic5 main_window.ui -o generate_file.py`，即可將ui檔轉換成py檔
2. 在Anaconda的Spyder中執行`main.py`
3. 在`Source Image`和`Destination Image`視窗中點擊滑鼠左鍵來畫Feature Line，在點選`WrapFeatureLine`按鈕計算wrap line、`WrapImage`按鈕完成圖形變形並顯示原圖變形及融合圖像(alpha=0.5)
<img src="https://user-images.githubusercontent.com/53482795/113876065-f647b200-97e9-11eb-9fe2-34b8adbfda56.png"/>
<img src="https://user-images.githubusercontent.com/53482795/113876451-59394900-97ea-11eb-93e6-2c03b7aa324a.png"/>
4. 點選`Animation`按鈕可產生alpha從0.1到1的動畫
<img src="https://user-images.githubusercontent.com/53482795/113878096-e16c1e00-97eb-11eb-9ffc-03c8d0c12343.gif"/>
