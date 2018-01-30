import random

study_examples = []
for i in range (2, 10):
    for ii in range (i, 10):
        study_examples.append(str('%d x %d =' % (i, ii)))

counter = 0
while counter < 15:
    length = len(study_examples)
    example_num = random.randint(0, length - 1)
    print(study_examples[example_num])
    study_examples.remove(study_examples[example_num])
    counter += 1
