from statistics import ft_statistics
import numpy as np

ft_statistics(1.0, 42, 360, 11, 64,
              toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
              ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61, 68,
              truc="quartile")
print("-----")
ft_statistics(1, 11, 15, 19, 20, 24, 28, 34, 37, 47, 50, 61,
              truc="quartile")
print("-----")

print("\n\nTesting a random array")
array = np.random.randint(100, size=(np.random.randint(100))).tolist()
print("Array", sorted(array))
print("Length", len(array))
print()
ft_statistics(*array, hey="mean", yop="median",
              truc="quartile", hola="std", yes="var")
print("\nExpected values")
print("mean :", np.mean(array))
print("median :", np.median(array))
print("quartile :", np.quantile(array, [0.25, 0.75], method="nearest"))
print("std :", np.std(array))
print("var :", np.var(array))
