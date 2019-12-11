from __future__ import division, absolute_import, print_function
from six.moves import urllib, xrange
import tensorflow as tf
import numpy as np
import collections, math, os, random, zipfile
import nltk
import pickle

num_steps = 50001 
batch_size = 128
embedding_size = 128
skip_window = 2
num_skips = 2 

max_vocab_size = 50000 
valid_size = 16 
valid_window = 100 
valid_examples = np.random.choice(valid_window, valid_size, replace=False)
num_sampled = 64 
data_src = "data/"

def read_data(lines):
	corpus_lines = [row.strip().lower().replace('"', '') for row in lines]

	words = []
	for line in corpus_lines:
		for word in line.split():
			words.append(word)

	cnt = len(set(words))
	print("vocabulary size is ::::::: " + str(cnt))
	return words

def build_dataset(words, vocab_sz):
    count = [['UNK', -1]] # set count for "UNK" token to -1 
    count.extend(collections.Counter(words).most_common(min(vocab_sz, max_vocab_size) - 1))
    dictionary = {}
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = []
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else: # set index to 0 (corresponding to "UNK")
            index = 0  
            unk_count += 1
        data.append(index)

    count[0][1] = unk_count 

    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys())) # idx_to_word

    return data, count, dictionary, reverse_dictionary

def generate_batch(data, data_index, batch_size, num_skips, skip_window):
    assert batch_size % num_skips == 0
    assert num_skips <= 2 * skip_window
    batch = np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    span = 2 * skip_window + 1
    buffer = collections.deque(maxlen=span)
    for _ in range(span):
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    for i in range(batch_size // num_skips):
        target = skip_window
        targets_to_avoid = [skip_window]
        for j in range(num_skips):
            while target in targets_to_avoid:
                target = random.randint(0, span - 1)
            targets_to_avoid.append(target)
            batch[i * num_skips + j] = buffer[skip_window]
            labels[i * num_skips + j, 0] = buffer[target]
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    return batch, labels, data_index

def generatePretrainedEmbeddings(infile, outfile):
	words = read_data(infile)
	print('data size:', len(words))
	vocabulary_size = len(set(words))
	data, count, dictionary, reverse_dictionary = build_dataset(words, vocabulary_size)
	del words
	print('most common words (+UNK):', count[:10])
	print('sample data:', data[:10], [reverse_dictionary[i] for i in data[:10]])
	data_index = 0
	batch, labels, data_index = generate_batch(data, data_index, batch_size=8, num_skips=2, skip_window=1)
	for i in range(8):
	    print(batch[i], reverse_dictionary[batch[i]], '->', labels[i, 0], reverse_dictionary[labels[i, 0]])

	graph = tf.Graph()

	with graph.as_default():
	    train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
	    train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
	    valid_dataset = tf.constant(valid_examples, dtype=tf.int32)
	    
	    embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
	    
	    embed = tf.nn.embedding_lookup(embeddings, train_inputs)

	    nce_weights = tf.Variable(tf.truncated_normal([vocabulary_size, embedding_size], stddev=1.0 / math.sqrt(embedding_size)))
	    nce_biases = tf.Variable(tf.zeros([vocabulary_size]))

	    loss = tf.reduce_mean(tf.nn.nce_loss(weights=nce_weights, biases=nce_biases,
	                     labels=train_labels, inputs=embed, num_sampled=num_sampled, num_classes=vocabulary_size))
	    
	    optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

	    norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, keep_dims=True)) # cosine similarity
	    normalized_embeddings = embeddings / norm
	    valid_embeddings = tf.nn.embedding_lookup(normalized_embeddings, valid_dataset)
	    similarity = tf.matmul(valid_embeddings, normalized_embeddings, transpose_b=True)

	    init = tf.initialize_all_variables()
	    steplist=[]
	    losslist=[]
	    with tf.Session(graph=graph) as session:
		    init.run()
		    
		    average_loss = 0
		    for step in xrange(num_steps):
		        batch_inputs, batch_labels, data_index = generate_batch(data, data_index, batch_size, num_skips, skip_window)
		        feed_dict = {train_inputs: batch_inputs, train_labels: batch_labels}
		        
		        _, loss_val = session.run([optimizer, loss], feed_dict=feed_dict)
		        average_loss += loss_val
		        
		        if step % 2000 == 0:
		            steplist.append(step)
		            if step > 0:
		                average_loss /= 2000
		            print("Average loss at step ", step, ": ", average_loss)
		            losslist.append(average_loss)
		            average_loss = 0
		        
		    final_embeddings = normalized_embeddings.eval()
		    if vocabulary_size != len(final_embeddings):
		    	print("ERROR: Dimension mismatch: " + len(vocabulary_size) + " vs "+ len(final_embeddings))
		    else:
		    	print("ALL IS CLEAR!")

		    lookup = {}
		    for i in range(vocabulary_size):
		    	lookup[reverse_dictionary[i]] = final_embeddings[i]

		    print("finished creating lookup")
		    print(len(lookup["thou"]))
		    pickle.dump(lookup, open(data_src + outfile, "w"))

def main():
	og16 = "allLines.original.nltktok"
	mod16 = "allLines.modern.nltktok"
	additional20 = "shakespeare_nonparallels_dialog.nltktok"

	aligned_only = []
	with open(og16, "r") as f, open(mod16, "r") as f2:
		aligned_only.extend(f.read().splitlines())
		aligned_only.extend(f2.read().splitlines())

	generatePretrainedEmbeddings(aligned_only, "embeddings16.obj")

	all_36_plays = []
	with open(og16, "r") as f, open(mod16, "r") as f2, open(additional20, "r") as f3:
		all_36_plays.extend(f.read().splitlines())
		print(len(all_36_plays))
		all_36_plays.extend(f2.read().splitlines())
		print(len(all_36_plays))
		all_36_plays.extend(f3.read().splitlines())
		print(len(all_36_plays))
		print('printed length thrice')
	generatePretrainedEmbeddings(all_36_plays, "embeddings36.obj")

if __name__ == "__main__":
	main()
