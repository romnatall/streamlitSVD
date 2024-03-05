import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
from io import BytesIO
import requests



def svd_plot(img,k):

    # Преобразование изображения в массив NumPy
    if len(img.mode) != 1:
        # Если изображение не в оттенках серого, берем только один канал (R)
        img_array = np.array(img)[:, :, 0]
    else:
        # Если изображение уже в оттенках серого, оставляем как есть
        img_array = np.array(img)

    # Уменьшение размера изображения, если его размер больше 1000
    if sum(img_array.shape) > 1000:
        # Получение размеров изображения
        a, b = img_array.shape
        # Уменьшение размера изображения с использованием масштабирования
        scale_factor = (a + b) // 1000
        img_array = img_array[::scale_factor, ::scale_factor]

    # Выполнение сингулярного разложения
    U, Sv, VT = np.linalg.svd(img_array)
    S = np.zeros(shape = img_array.shape)
    np.fill_diagonal(S, Sv)

    # Уменьшение количества сингулярных значений до k
    U_k = U[:, :k]
    S_k = S[:k, :k]
    VT_k = VT[:k, :]
    
    # Восстановление изображения
    img_approx_array = U_k @ S_k @ VT_k

    # Отображение изображений
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.imshow(img_array, cmap='gray')
    ax1.set_title("Оригинальное изображение")
    ax1.axis('off')

    ax2.imshow(img_approx_array, cmap='gray')
    ax2.set_title(f'Аппроксимация с {k} сингулярными значениями')
    ax2.axis('off')

    st.pyplot(fig)

def main():
    st.title("SVD Image Approximation App")

   

    # Возможность выбора источника изображения
    image_source = st.radio("Выберите источник изображения:", ("URL", "Файл на устройстве"))

    if image_source == "URL":

        image_url = st.text_input("Введите URL изображения:")
        if image_url != '':
            try:
                st.image(image_url, caption="Выбранное изображение", use_column_width=True)
                response = requests.get(image_url)
                
            except:
                st.warning("Загрузка не удалась.")
                return
            k_value = st.slider("Выберите количество сингулярных значений (k):", 2, 300, value=10)
            svd_plot(Image.open(BytesIO(response.content)),k_value)
        else:
            st.warning("Загрузите изображение перед тем, как продолжить.")
            return

    else:
        uploaded_file = st.file_uploader("Загрузите изображение", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            st.image(uploaded_file, caption="Выбранное изображение", use_column_width=True)
        else:
            st.warning("Загрузите изображение перед тем, как продолжить.")
            return
        k_value = st.slider("Выберите количество сингулярных значений (k):", 2, 300, value=10)
        svd_plot(Image.open(BytesIO(uploaded_file.read())),k_value)

    # Возможность выбора значения k
    

    # Отображение графиков
    

if __name__ == "__main__":
    main()
