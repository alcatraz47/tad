# tad
Text as data:
```
    - cleaning;
    - pre-processing;
    - post processing:
    - Topic Modelling: LDA, seeded LDA
    - Word2Vec and other static embedding
    - RNN, LSTM, and Seq2Seq
    - Attention and Transformers
```
Python Version: 3.7.16

Scikit-learn versions that are supported: 0.20 to 0.24 and 1.0, 1.0.1, and 1.0.2

To install the packages:
```
pip install -r requirements.txt
```

Ad-hoc materials:

Along with the lecture slides, we can also refer to the resources below:

0. Speech and Language Processing:

    - Book: [Speech and Language Processing by Dan Jurafsky and James H. Martin](https://web.stanford.edu/~jurafsky/slp3/)
    - Book: [Machine Learning for Text by Charu C. Aggarwal](https://link.springer.com/book/10.1007/978-3-319-73531-3)

1.  Text Processing:

    - Blog: [Jaccard vs Cosine Distance](https://towardsdatascience.com/overview-of-text-similarity-metrics-3397c4601f50)
    - Blog: [Understanding the Levenshtein Distance Equation](https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0)
    - Blog: [Stemming vs Lemmatization](https://databasecamp.de/en/data/stemming-lemmatization)

2.  Fundamentals:

    - Tf-IDf:
        - Blog: [TF-IDF](https://medium.com/analytics-vidhya/understanding-calculation-of-tf-idf-by-example-8975304e7fc4)

    - Zipf's Law:
        - Blog: [Zipf's Law](https://medium.com/@_init_/using-zipfs-law-to-improve-neural-language-models-4c3d66e6d2f6)
        - YT: [Zipf's Law](https://youtu.be/WYO8Rc4JB_Y?si=W80TjSPD-PpTKx-m)

    - Heaps' Law:
        - YT: [Heaps' law](https://youtu.be/QwV-aCaWKq8?si=Hcu86mPsqPlSSXNK)

3.  Clustering:

    - SVD:
        - Basics, YT: [Singular Value Decomposition (the SVD)](https://www.youtube.com/watch?v=mBcLRGuAFUk)
        - High Level Overview, YT: [Singular Value Decomposition (SVD): Overview](https://www.youtube.com/watch?v=gXbThCXjZFM)
        - Mathematical Overview: YT: [Singular Value Decomposition (SVD): Mathematical Overview](https://www.youtube.com/watch?v=nbBvuuNVfco)
        - Rank R Approximation, YT: [Singular Value Decomposition (SVD): Matrix Approximation](https://www.youtube.com/watch?v=xy3QyyhiuY4)

    - LSA:
        - YT: [LSA](https://www.youtube.com/watch?v=bzNch-dBCN8)

4.  Topic Modelling:

    - Data Pre-processing for Topic Modelling:
        - Blog: [NLP Preprocessing and Latent Dirichlet Allocation (LDA) Topic Modeling with Gensim](https://towardsdatascience.com/nlp-preprocessing-and-latent-dirichlet-allocation-lda-topic-modeling-with-gensim-713d516c6c7d)

    - LDA:
        - YT: [Latent Dirichlet Allocation (Part 1 of 2)](https://www.youtube.com/watch?v=T05t-SqKArY)
        - YT: [Training Latent Dirichlet Allocation: Gibbs Sampling (Part 2 of 2)](https://www.youtube.com/watch?v=BaM1uiCpj_E)
        - Blog: [Topic Modeling and Latent Dirichlet Allocation (LDA) in Python](https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24)

5.  Word2Vec:

    - YT: [Word2Vec, GloVe, FastText- EXPLAINED!](https://www.youtube.com/watch?v=9S0-OC4LFNo)
    - YT: [Word Vector Representations: word2vec](https://youtu.be/ERibwqs9p38?si=ju1Wsf7oHd1XV8m5)
    - YT: [GloVe: Global Vectors for Word Representation](https://youtu.be/ASn7ExxLZws?si=Ikz2MIXw4xDWF99F)
    - YT: [Word2Vec Detailed Explanation, Train custom Word2Vec Model using genism in Python](https://www.youtube.com/watch?v=MtM9QrCjuK4)
    - YT: [Coding Word2Vec : Natural Language Processing](https://www.youtube.com/watch?v=d2E-pU4H2gc)
    - YT: [Word Embedding and Word2Vec, Clearly Explained!!!](https://www.youtube.com/watch?v=viZrOnJclY0&list=PLsrpjPHm_EOo8LhK8JOAqbqNxy-Rd53sE)
    - Extra, YT: [Word Embeddings - EXPLAINED!](https://www.youtube.com/watch?v=GmXkCCa4eVA)

6.  Doc2Vec:

    - Blog: [How to Vectorize Text in DataFrames for NLP Tasks — 3 Simple Techniques](https://towardsdatascience.com/how-to-vectorize-text-in-dataframes-for-nlp-tasks-3-simple-techniques-82925a5600db)
    - Blog: [Practical Guide To Doc2Vec & How To Tutorial In Python](https://spotintelligence.com/2023/09/06/doc2vec/)
    - Blog: [Multi-Class Text Classification with Doc2Vec & Logistic Regression](https://towardsdatascience.com/multi-class-text-classification-with-doc2vec-logistic-regression-9da9947b43f4)

7. RNN and LSTM:

    - YT: [Recurrent Neural Networks (RNNs), Clearly Explained!!!](https://youtu.be/AsNTP8Kwu80?si=NvOjXqcrFOdl889r)
    - YT:[Long Short-Term Memory (LSTM), Clearly Explained](https://www.youtube.com/watch?v=YCzL96nL7j0&list=PLsrpjPHm_EOo8LhK8JOAqbqNxy-Rd53sE&index=3)
    - YT: [Sequence-to-Sequence (seq2seq) Encoder-Decoder Neural Networks, Clearly Explained!!!](https://www.youtube.com/watch?v=L8HKweZIOmg&list=PLsrpjPHm_EOo8LhK8JOAqbqNxy-Rd53sE&index=4)

8. Attention and Transformers:

    - YT: [The Attention Mechanism in LLMs a High Level Overview](https://youtu.be/OxCpWwDCDFQ?si=YiY5Q7hQ357H0uPe)
    - YT: [The math behind Attention: Keys, Queries, and Values matrices](https://youtu.be/UPtG_38Oq8o?si=8YP0WpZDf4hNmuYp)
    - YT: [Attention for Neural Networks, Clearly Explained!!!](https://www.youtube.com/watch?v=PSs6nxngL6k&list=PLsrpjPHm_EOo8LhK8JOAqbqNxy-Rd53sE&index=5)
    - YT: [What is Transformer Models and how do they work?](https://youtu.be/qaWMOYf4ri8?si=ziuii-e4Bt3wtu75)
    - YT: [Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!](https://www.youtube.com/watch?v=zxQyTK8quyY&list=PLsrpjPHm_EOo8LhK8JOAqbqNxy-Rd53sE&index=6)
    - YT:[Decoder-Only Transformers, ChatGPTs specific Transformer, Clearly Explained!!!](https://www.youtube.com/watch?v=bQ5BoolX9Ag&list=PLsrpjPHm_EOo8LhK8JOAqbqNxy-Rd53sE&index=7)
    - Blog: [A Gentle Introduction to Positional Encoding in Transformer Models, Part 1](https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/)