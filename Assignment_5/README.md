# Assignment 5: Transfer Learning: Duck vs Chicken Image Classifier  

This repository involve Transfer Learning for image data using CNN and for text data using Transformer.

## Files and Directories

### 1. [`AML_5_1.ipynb`](./AML_5_1.ipynb)

This notebook demonstrates the use of **transfer learning** for image classification using **Convolutional Neural Networks (CNNs)**.  

**Overview**  
- Collected ~100 images each of ducks and chickens from the internet  
- Used a **pre-trained CNN** (ResNet)  
- Fine-tuned the model to classify images as either *duck* or *chicken*  
- Evaluated performance using a **classification report**  

**Key Features**  
- Efficient training with limited data using transfer learning  
- End-to-end pipeline: data loading → preprocessing → training → evaluation  
- Simple and adaptable for other binary image classification tasks  

### 2. [`AML_5_2.ipynb`](./AML_5_2.ipynb)

This notebook applies **transfer learning** for **sentiment classification** using a **pre-trained Transformer model** (BERT).  

**Overview**  
- Used a [sentiment analysis dataset](https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset) with labeled text samples  
- Fine-tuned a pre-trained **Transformer model** to classify text into **positive**, **neutral**, or **negative** sentiment  
- Evaluated the model's performance using a **classification report**  

**Key Features**  
- Fine-tuning of powerful NLP models like BERT for custom classification tasks  
- Multi-class sentiment prediction  
- Fully reproducible pipeline: data loading → preprocessing → model training → evaluation  
