### tweetimgsplit.py
import cv2
import sys
import os
# 処理する画像ファイル名を定義
BaseFile,ExtFile = os.path.splitext(os.path.basename(sys.argv[1]))
# 書き出すファイル名を定義
MakeFile = [ 0 for i in range(5) ]
for i in range(1,5):
  if 'jpg' in ExtFile:
    MakeFile[i] = BaseFile + '_' + str(i) + '.jpg'
  elif 'png' in ExtFile:
    MakeFile[i] = BaseFile + '_' + str(i) + '.png'
# 画像の読み出し
ImgSrc = cv2.imread(sys.argv[1])
# 画像のサイズを取得
ymax, xmax, channels = ImgSrc.shape[:3]
# 画像のサイズが分割可能か確認
print("4:3 " + str(xmax) + ":" + str(ymax))
try:
  # 16:9で処理する
  x9 = xmax // 16
  _ymax = x9 * 9
  # 16:9の場合y軸をずらす
  shiftpx = ( ymax - _ymax ) // 2
  print("shiftpx: " + str(shiftpx))
  # 座標を求める
  yzero = 0 + shiftpx
  xzero = 0
  # 16:9の場合y軸をずらす
  ydiv = ( _ymax // 2 ) + shiftpx
  xdiv = xmax // 2
  # 16:9の場合y軸をずらす
  _ymax = _ymax + shiftpx
except ZeroDivisionError:
  print("画像が分割できませんでした")
else:
  # トリミングを行う
  print("16:9 " + str(xmax) + ":" + str(_ymax))
  Img1 = ImgSrc[yzero:ydiv,xzero:xdiv, :]
  Img2 = ImgSrc[yzero:ydiv,xdiv:xmax, :]
  Img3 = ImgSrc[ydiv:_ymax,xzero:xdiv, :]
  Img4 = ImgSrc[ydiv:_ymax,xdiv:xmax, :]
  # 画像を保存
  cv2.imwrite(MakeFile[1],Img1)
  cv2.imwrite(MakeFile[2],Img2)
  cv2.imwrite(MakeFile[3],Img3)
  cv2.imwrite(MakeFile[4],Img4)
# End Program
