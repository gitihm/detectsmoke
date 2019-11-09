import tensorflow-gpu as tf
hello = tf.constant("hello TensorFlow!")
sess=tf.Session() 
print(sess.run(hello))