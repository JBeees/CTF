import time
import subprocess 

def test_pin(pin):
  start_time = time.time()
  result= subprocess.run(["./pin_checker"], input=pin.encode(), capture_output=True)
  end_time   = time.time()
  return  end_time - start_time

max_time = 0
index = 0
correct_pin = ""
for i in range(8):
    for j in range(0,10):
        testpin = correct_pin + str(j) + (str(j) * (7 - i))
        cur_time =  test_pin(testpin)
        print("Test PIN : ",testpin)
        if (cur_time > max_time):
            max_time = cur_time
            index = j
    correct_pin = correct_pin + str(index)
    max_time = 0
    print(correct_pin)
