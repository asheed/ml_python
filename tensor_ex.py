#!/usr/bin/env python
# -*- coding: utf8 -*
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

# tf.constant: 말 그대로 상수
hello = tf.constant('안녕, 텐서플로!')
print(hello)

a = tf.constant(10)
b = tf.constant(32)
c = tf.add(a, b)    # a + b 도 가능
print(c)

# 위에서 변수와 수식들을 정의했지만, 실행이 정의한 시점에서 실행되는 것은 아닙니다.
# 다음처럼 Session 객제와 run 메소드를 사용할 때 계산이 됩니다.
# 따라서 모델을 구성하는 것과, 실행하는 것을 분리하여 프로그램을 깔끔하게 작성할 수 있습니다.
# 그래프를 실행할 세션을 구성합니다.

sess = tf.Session()
# sess.run: 설정한 텐서 그래프(변수나 수식 등)를 실행
print(sess.run(hello))
print(sess.run([a, b, c]))

# 세션 닫기
sess.close()