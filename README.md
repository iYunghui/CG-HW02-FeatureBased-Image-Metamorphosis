# CG HW02 Feature Based Image Metamorphosis

## Hardware and software requirement

* Windows 10
* Python 3.7
	* Spyder 3.3.6
	* Opencv2 3.4.2
	* PyQt5 5.15.1

## Program overview


## Operations manual

1. 若需要修改GUI介面，開啟pyqt5的designer.exe修改，修改完畢後開啟Anaconda Prompt至ui檔案位置，輸入`pyuic5 main_window.ui -o generate_file.py`
2. 執行`main.py`
3. 在`Source Image`和`Destination Image`視窗中點擊滑鼠左鍵來畫Feature Line，在點選`WrapFeatureLine`按鈕計算wrap line、`WrapImage`按鈕完成圖形變形並顯示原圖變形及融合圖像(alpha=0.5)
4. 點選`Animation`按鈕可產生alpha從0.1到1的動畫
5. 執行畫面
<img src=""/>
<img src="" />

