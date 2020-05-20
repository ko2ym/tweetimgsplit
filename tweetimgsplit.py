### tweetimgsplit.py
import cv2
import sys
# 処理する画像ファイル名を定義
BaseFile = sys.argv[1] + '.jpg'
# 書き出すファイル名を定義
MakeFile = [ 0 for i in range(5) ]
for i in range(1,5):
  MakeFile[i] = sys.argv[1] + '_' + str(i) + '.jpg'
# 画像の読み出し
ImgSrc = cv2.imread(BaseFile)
# 画像のサイズを取得
ymax, xmax, channels = ImgSrc.shape[:3]
# 画像のサイズが分割可能か確認
try:
  # 座標を求める
  yzero = 0
  xzero = 0
  ydiv = ymax // 2
  xdiv = xmax // 2
except ZeroDivisionError:
  print("画像が分割できませんでした")
else:
  # トリミングを行う
  Img1 = ImgSrc[yzero:ydiv,xzero:xdiv, :]
  Img2 = ImgSrc[yzero:ydiv,xdiv:xmax, :]
  Img3 = ImgSrc[ydiv:ymax,xzero:xdiv, :]
  Img4 = ImgSrc[ydiv:ymax,xdiv:xmax, :]
  # 画像を保存
  cv2.imwrite(MakeFile[1],Img1)
  cv2.imwrite(MakeFile[2],Img2)
  cv2.imwrite(MakeFile[3],Img3)
  cv2.imwrite(MakeFile[4],Img4)
# End Program
