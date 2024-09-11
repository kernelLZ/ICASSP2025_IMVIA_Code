import h5py

with h5py.File('datasets/MKG-W/MKG_W_img_BEIT_16-224.h5', 'r') as hf:
    # 列出所有数据集名称
    print(hf['Herbert_Lom'][:])