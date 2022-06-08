# .pop(<index>) vs .remove(<first_occurrence_of_item>)
test = ['one', 'two', 'three']
test.pop(1) # 'two' -> ['one', 'three']
test.remove('one') # <no-return> -> ['three']