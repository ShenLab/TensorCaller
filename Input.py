#!/home/local/users/jw/anaconda2/bin/python
#Author: jywang	explorerwjy@gmail.com

#========================================================================================================
# Prepare Input Data For Training
#========================================================================================================

from optparse import OptionParser
import os
import Region
import time
import gzip

BatchSize = 32

class Data():
	def __init__(self,TrainingHand,ValidationHand,TestingHand):
		self.TrainingHand = TrainingHand
		self.TrainingBatch = BatchSize
		self.ValidationHand = ValidationHand
		self.TestingHand = TestingHand
	def ReadingTraining(self):
		# Args:    file hand of Training windows, get [batch_size] Lines of records. 
		# Returns: 4D tensor of [batch_size, height, width, depth] size
		#		   1D tensor of [batch_size] size.
		self.Training = []
		self.TrainingLabels = []
		i = 0
		while i < self.TrainingBatch:
			l = TrainingHand.readline()
			if l == '':
				self.handle.seek(0)
				continue
			tensor, label = Record(l)
			self.Training.append(tensor)
			self.label.append(label)
			i += 1
		return self.Training, self.TrainingLabels
	def ReadingValidation(self):
		self.Validation = []
		self.ValidationLabels = []
		for l in self.ValidationHand:
			tensor, label = Record(l)
			self.Validation.append(tensor)
			self.ValidationLabels.append(labels)
		return self.Validation, self.ValidationLabels
	def ReadingTesting(self):
		self.Testing = []
		self.TestingLabels = []
		for l in self.TestingHand:
			tensor, label = Record(l)
			self.Testing.append(tensor)
			self.TestingLabels.append(labels)
		return self.Testing, self.TestingLabels

class Record():
	#First 13 bytes is Meta Data
	#Label x1, Chrom x2, Pos x10
	#Record starts from 14th byte, total width x height x depth bytes.
	def __init__(self,lineRecord):
		self.width = WIDTH
		self.height = HEIGHT
		self.depth = DEPTH
		self.label = lineRecord[0]
		self.data = lineRecord[13:]
		
		x = tf.placeholder(tf.float32, shape=(self.width * self.height * self.depth))
		y = tf.placeholder(tf.int64, shape=(1))
		
		

def Generate_Tensor_and_label_batch(tensor, label, min_queue_examples, batch_size=BatchSize):
	Tensors, Labels_batch = tf.train.batch([tensor, label], batch_size = batch_size, num_threads = num_preprocess_threads, capacity = min_queue_examples + 3*batch_size)
	tf.image_summary('tensors',Tensors)
	return Tensors, tf.reshape(Label_batch, [batch_size])

def Inputs_training(Training_fname, batch_size=BatchSize):
	
	
	return

def Inputs_validation_testing():

	return
def GetOptions():
	parser = OptionParser()
	parser.add_option('-','--',dest = '', metavar = '', help = '')
	(options,args) = parser.parse_args()
	
	return

def main():

	return

if __name__=='__main__':
	main()