import os
from dotenv import load_dotenv
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

load_dotenv()

pasta = os.getenv("IMG_TRAIN")

gt_file_path = os.getenv("GT_FILE")

caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
images_names = [arq for arq in arquivos if arq.lower().endswith(".jpg")]
# print(images_names)
try:
	gt_file = open(gt_file_path, "r")
	gt_lines = gt_file.readlines()
	print(gt_lines, len(gt_lines))
except Exception as e:
	gt_file = open(gt_file_path, "w")
	gt_lines = 0
	print(e)

gt_file = open(gt_file_path, "w")

cnt_lines = 0;

for act_img in images_names:
	img_path_names = act_img.split("/")
	img_name = img_path_names[len(img_path_names)-1]

	img = mpimg.imread(act_img)
	imgplot = plt.imshow(img)
	plt.show(block=False)
	#plt.imshow(img)
	toSave = '{},"{}"\n'
	if cnt_lines < len(gt_lines):
		print("Name in file: ", gt_lines[cnt_lines])
	else:
		print("NEW LINE in file: ")

	p_img = input("Digite o nome na imagem: ")
	plt.close()
	if cnt_lines < len(gt_lines):	
		print (p_img !='')	
		if p_img != '':
			gt_lines[cnt_lines] = toSave.format(img_name,p_img)
			gt_file.writelines( gt_lines )
	else:
		gt_last_line = toSave.format(img_name,p_img)
		gt_file.write(gt_last_line)
	
	cnt_lines = cnt_lines + 1
	print(p_img)

