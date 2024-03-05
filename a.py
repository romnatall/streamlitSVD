import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import requests

def resize_image(image_array, target_height=300, target_width=300):
    """
    Уменьшает размер массива изображения до указанных размеров.

    :param image_array: Массив изображения (NumPy array).
    :param target_height: Целевая высота изображения.
    :param target_width: Целевая ширина изображения.
    :return: Уменьшенный массив изображения.
    """
    # Использование функции resize для изменения размера
    resized_image = np.resize(image_array, (target_height, target_width))
    return resized_image

def svd_plot(image_path, k):
    # Загрузка изображения
    if image_path.startswith("http"):
        response = requests.get(image_path)
        img = Image.open(BytesIO(response.content))
    else:
        img = Image.open(image_path)

    
    # Преобразование изображения в массив NumPy
    img_array = np.array(img)[:,:,0]
    if sum(img_array.shape)>1000:
        a,b = img_array.shape
        sc = (a+b)//1000
        img_array =  img_array[::sc,::sc]

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
            except:
                st.warning("Загрузка не удалась.")
                return
        else:
            st.warning("Загрузите изображение перед тем, как продолжить.")
            return

    else:
        uploaded_file = st.file_uploader("Загрузите изображение", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image_url = None
            st.image(uploaded_file, caption="Выбранное изображение", use_column_width=True)
        else:
            st.warning("Загрузите изображение перед тем, как продолжить.")
            return

    # Возможность выбора значения k
    k_value = st.slider("Выберите количество сингулярных значений (k):", 2, 100, value=10)

    # Отображение графиков
    svd_plot(image_url, k_value)

if __name__ == "__main__":
    main()
