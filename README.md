# DE_CIFAR10_Assignment
Resnet on CIFAR10 Image dataset
================================

1) Built Resnet-18 Architecture. 
2) Trained the model with CIFAR10 dataset
3) Various experiments were conducted by configuring values of parameters such as Image Augmentation, Normalization, Optimizers and Dropout. The results are available in modelTraining\TrainingExperimentResults.xlsx
4) The best model with image augmentation, normlization, SGD with dynamic learning rate and dropout(0.25). 
5) The model was trained for 200 eppoch with the best accuracy of 90.98 on test data.
6) The following per class accuracy on test data were obtained. 

					aeroplane: 0.86
					automobile: 0.96
					bird: 0.865
					cat: 0.762
					deer: 0.916
					dog: 0.85
					frog: 0.947
					horse: 0.935
					ship: 0.951
					truck: 0.935
	with confusion matrix of :
      [[860,  16,  32,  13,   9,   4,   4,   4,  34,  24],
       [  1, 960,   2,   1,   0,   0,   0,   1,   6,  29],
       [ 13,   1, 865,  14,  40,  13,  30,  13,   2,   9],
       [  6,   2,  35, 762,  35, 102,  24,  20,   6,   8],
       [  6,   2,  18,  14, 916,  12,   8,  20,   3,   1],
       [  1,   2,  20,  75,  21, 850,   5,  22,   1,   3],
       [  3,   3,  11,  14,  10,   8, 947,   1,   0,   3],
       [  3,   0,   6,   5,  19,  20,   1, 935,   2,   9],
       [ 21,   8,   2,   0,   0,   2,   1,   1, 951,  14],
       [  7,  41,   2,   1,   1,   0,   2,   1,  10, 935]]
	
	Inferences:
		Ships and automobiles have the highest accuracy amoung all the classes
		Cats are being misclassified as dogs and vice versa.

7) 