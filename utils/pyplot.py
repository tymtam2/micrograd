import matplotlib.pyplot as plt

def show(X, y):
    # visualize in 2D
    plt.figure(figsize=(5,5))
    plt.scatter(X[:,0], X[:,1], c=y, s=20, cmap='jet')


    plt.axis("off")
    plt.show()