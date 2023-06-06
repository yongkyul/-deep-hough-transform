1. gt lines all: each row describes x1, x2, y1, y2, image width, image height
2. gt_pri_lines_for_test: priary gt lines are denoted as 1, otherwise 0.


Inference on pre-trained model
1. Inference images have to be in .jpg (Change to .jpg from .png from data/image_ops/changeFileExtension.py)
2. Put images in data/agriNav_data
3. Run saveFilenameList.py from data/image_ops to obtain txt file with all filenames
4. Move agriNav_test_idx.txt to data/
5. In config.yml, verify that TEST_DIR and TEST_LABEL_FILE are correct
6. Change utils.py line 86 specify image directory for inference
7. Run python forward.py --model ./result/agriNav_0226/reproduce/model_best.pth --tmp ./result/agriNav_0226_inference/


Generate training data
1. In deep-hough-transform,
	run: python data/prepare_data_NKL.py --root './data/agriNav_0313' --label './data/agriNav_0313' --save-dir './data/training/agriNav_0313_resized_100_100' --fixsize 400 

2. In deep-hough-transform/data
	modify and run saveFilenameList_trainIdx.py, divide train.txt and val.txt file

3. Modify config.yml, pay attention to MISC

python forward.py --model ./result/agriNav_0313/reproduce/model_best.pth --tmp ./result/agriNav_0313_inference_fig2/
