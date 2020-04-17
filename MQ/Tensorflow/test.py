import tensorflow as tf

a = tf.constant([1, 2])
b = tf.constant([2, 3])
res = a + b
print(res)
sess = tf.Session()
ans = sess.run(res)
sess.close()
print(ans)