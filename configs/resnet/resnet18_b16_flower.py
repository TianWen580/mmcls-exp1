_base_ = ['../_base_/models/resnet18.py', '../_base_/datasets/imagenet_bs32.py',
'../_base_/default_runtime.py']

load_from = 'pth/resnet18_batch256_imagenet_20200708-34ab8f90.pth'

model = dict(
	head = dict(
		num_classes = 5,
		topk = (1, )))

data = dict(
	samples_per_gpu = 32,
	workers_per_gpu = 2,
	train = dict(
		data_prefix = 'data/train',
		ann_file = 'data/train.txt',
		classes = 'data/classes.txt'),
	val = dict(
		data_prefix = 'data/val',
		ann_file = 'data/val.txt',
		classes = 'data/classes.txt'))

optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
lr_config = dict(
	policy='step', 
	step=[60, 120, 160], 
	gamma=0.2)
	
evaluation = dict(metric_options={'topk': (1, )})
runner = dict(type='EpochBasedRunner', max_epochs = 50)

