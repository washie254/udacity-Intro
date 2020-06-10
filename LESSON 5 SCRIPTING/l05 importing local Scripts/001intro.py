import other_script as osc#script located in same directory
import useful_functions as usf

print(osc.num)
scores = [88,92,79,93,85]

mean = usf.mean(scores)
curved = usf.add_five(scores)

mean_c = usf.mean(curved)

print("Scores : ", scores)
print("Crurved: ",curved)
print("Original Mean: ",mean,"\nNew mean: ", mean_c)

print(__name__)  # indicates this is the main script running
print(usf.__name__) # indicates the name of usf, script