import cv2
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title('色比率解析App')
path = st.file_uploader("画像を選択してください", type=['jpg','JPG','jpeg','JPEG'])
if path is not None:
    # ファイルをバイト列として読み込む
    image_bytes = path.read()
    bgr_array = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    st.image(bgr_array, channels="BGR")
    
    #figure()でグラフを表示する領域をつくり，figというオブジェクトにする．
    fig = plt.figure()

    #add_subplot()でグラフを描画する領域を追加する．引数は行，列，場所
    ax1 = fig.add_subplot(3, 2, 1)
    ax2 = fig.add_subplot(3, 2, 2)
    ax3 = fig.add_subplot(3, 2, 3)
    ax4 = fig.add_subplot(3, 2, 4)
    ax5 = fig.add_subplot(3, 2, 5)
    ax6 = fig.add_subplot(3, 2, 6)
    # 青と緑で解析する
    bgr_array = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    bgr_array = bgr_array.transpose()
    b = 0
    g = 0
    b = np.sum(bgr_array[0]>bgr_array[1])
    g = np.sum(bgr_array[0]<bgr_array[1])
    bgr_array[0] = np.where(bgr_array[0]>bgr_array[1],255,0)
    bgr_array[1] = np.where(bgr_array[0]<bgr_array[1],255,0)
    bgr_array[2] = 0
    bgr_array = bgr_array.transpose()
    img = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2RGB)
    ax1.imshow(img)
    ax2.pie([b,g], colors=["blue","green"],startangle=90, autopct="%1.1f%%")

    #赤と緑で解析する
    bgr_array  = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    bgr_array = bgr_array.transpose()
    r = 0
    g = 0
    r = np.sum(bgr_array[2]>bgr_array[1])
    g = np.sum(bgr_array[2]<bgr_array[1])
    bgr_array[2] = np.where(bgr_array[2]>bgr_array[1],255,0)
    bgr_array[1] = np.where(bgr_array[2]<bgr_array[1],255,0)
    bgr_array[0] = 0
    bgr_array = bgr_array.transpose()
    img = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2RGB)
    ax3.imshow(img)
    ax4.pie([r,g], colors=["red","green"],startangle=90, autopct="%1.1f%%")

    #3色で解析する
    bgr_array  = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    bgr_array = bgr_array.transpose()
    r = 0
    g = 0
    b = 0
    r = np.sum((bgr_array[2]>bgr_array[1]) & (bgr_array[2]>bgr_array[0]))
    g = np.sum((bgr_array[1]>bgr_array[2]) & (bgr_array[1]>bgr_array[0]))
    b = np.sum((bgr_array[0]>bgr_array[2]) & (bgr_array[0]>bgr_array[1]))
    bgr_array[2] = np.where(((bgr_array[2]>bgr_array[1]) & (bgr_array[2]>bgr_array[0])),255,0)
    bgr_array[1] = np.where(((bgr_array[1]>bgr_array[2]) & (bgr_array[1]>bgr_array[0])),255,0)
    bgr_array[0] = np.where(((bgr_array[0]>bgr_array[2]) & (bgr_array[0]>bgr_array[1])),255,0)
    bgr_array = bgr_array.transpose()
    img = cv2.cvtColor(bgr_array, cv2.COLOR_BGR2RGB)
    ax5.imshow(img)
    ax6.pie([r,g,b], colors=["red","green","blue"],startangle=90, autopct="%1.1f%%")
    fig.tight_layout()              #レイアウトの設定
    st.pyplot(fig)
