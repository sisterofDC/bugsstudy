import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path='./savemodel/linear.tflite')
interpreter.allocate_tensors()

print(interpreter.get_input_details())
print(interpreter.get_output_details())