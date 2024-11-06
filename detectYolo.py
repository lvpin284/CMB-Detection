import os
import shutil

import nibabel as nib
import numpy as np
from PIL import Image
from ultralytics import YOLO


def nii_to_jpg(input_nii_path, output_folder):
    # Load NIfTI image
    nii_img = nib.load(input_nii_path)
    nii_data = nii_img.get_fdata()

    # Normalize pixel values to [0, 255]
    normalized_data = (nii_data - np.min(nii_data)) / (np.max(nii_data) - np.min(nii_data)) * 255
    normalized_data = normalized_data.astype(np.uint8)

    # Slice through depth and save each slice as JPEG
    for i in range(nii_data.shape[2]):
        slice_img = normalized_data[:, :, i]
        slice_img = np.rot90(slice_img)  # Optional: Rotate if needed
        slice_img = Image.fromarray(slice_img)
        slice_img.save(f"{output_folder}/slice_{i}.jpg")

def detect(images_path):

    # 加载训练好的模型权重
    model = YOLO("D:/dachuang/runs/detect/train9/weights/best.pt")

    # 指定待预测的图像路径
    # images_path = "D:/dachuang/dataset/jpg/"

    # 创建用于保存结果的文件夹
    output_folder = "D:/dachuang/detection_results/"
    os.makedirs(output_folder, exist_ok=True)

    # 获取文件夹下所有图像文件
    image_files = [f for f in os.listdir(images_path) if f.endswith('.jpg')]

    for img in image_files:
        print("Processing image:", img)
        img_path = os.path.join('D:/dachuang/runs/detect/predict/', img)

        predictions = model.predict(source=images_path + img, save=True, line_width=1)

        for result in predictions:

            if len(result.boxes) > 0:
                shutil.copyfile(img_path, os.path.join(output_folder, img))

                output_file = os.path.join(output_folder, img.replace('.jpg', f'.txt'))

                with open(output_file, 'w') as f:
                    boxes = result.boxes
                    for box in boxes:
                        class_id = result.names[box.cls[0].item()]
                        cords = box.xyxy[0].tolist()
                        cords = [round(x) for x in cords]
                        conf = round(box.conf[0].item(), 2)

                        f.write("Object type: {}\n".format(class_id))
                        f.write("Coordinates: {}\n".format(cords))
                        f.write("Probability: {}\n".format(conf))
                        f.write("---\n")



            boxes = result.boxes

            for box in boxes:
                class_id = result.names[box.cls[0].item()]
                cords = box.xyxy[0].tolist()
                cords = [round(x) for x in cords]
                conf = round(box.conf[0].item(), 2)
                print("Object type:", class_id)
                print("Coordinates:", cords)
                print("Probability:", conf)
                print("---")
        ruta_a_borrar = 'D:/dachuang/runs/detect/predict'
        borrar_carpeta(ruta_a_borrar)

def borrar_carpeta(path_carpeta):
    try:
        # Utiliza shutil.rmtree para borrar la carpeta y su contenido de forma recursiva
        shutil.rmtree(path_carpeta)
        print(f'Carpeta {path_carpeta} borrada exitosamente.')
    except Exception as e:
        print(f'Error al borrar la carpeta: {e}')

if __name__ == '__main__':
    input_nii_path = "D:/dachuang/dataset/nii/01.nii"  # 输入NIfTI图像的路径
    output_folder = "D:/dachuang/dataset/jpg/"  # JPEG图像的输出文件夹
    nii_to_jpg(input_nii_path, output_folder)
    detect(output_folder)
