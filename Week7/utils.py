import numpy as np
from gensim import matutils

def show_topics(model, num_topics=10, num_words=5):
    sort_alpha = model.alpha + 0.0001 * model.random_state.rand(len(model.alpha))
    sorted_topics = list(matutils.argsort(sort_alpha))
    chosen_topics = sorted_topics[:num_topics // 2] + sorted_topics[-num_topics // 2:]
    shown = []
    topic = model.state.get_lambda()
    rel_topic_ = topic / np.sum(topic, axis=1)[:, np.newaxis]
    log_topic_ = np.log(topic)
    topic = rel_topic_ * (log_topic_ - np.mean(log_topic_, axis=0)[np.newaxis, :])
    for i in chosen_topics:
        topic_ = topic[i]
        bestn = matutils.argsort(topic_, num_words, reverse=True)
        topic_ = [model.id2word[id] for id in bestn]
        shown.append(topic_)
    return shown
