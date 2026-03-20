from preprocessor import preprocess

sample = "Experienced in Running Machine Learning Models and building Pipelines!!!"
cleaned = preprocess(sample)
print("Before:", sample)
print("After:", cleaned)