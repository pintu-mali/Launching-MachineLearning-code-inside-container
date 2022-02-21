import os
os.system("tput setaf 39")
print("""
#########################################
#                                       #
#                                       #
#            Machine Learning           #
#                                       #
#########################################
_________________________________________
_________________________________________
""")
while True:
    print("""
1.Artificial Neural network
2.Exit
    """)
    ch = int(input("Enter your choice: "))
    if ch == 1:
      import os
      import pandas as pd
      os.system("tput setaf 21")
      print("""
the output column name should be 'y'
      """)
      os.system("tput setaf 7")
      location = input("Enter the location of dataset: ")
      data = pd.read_csv(location)
      x = data.drop('y',axis=1)
      y = data['y']
      from keras.models import Sequential
      model = Sequential()
      from keras.layers import Dense
      iteration = int(input("How many layers you need: "))
      n=1
      n_neurons = int(input("Enter the number of neurons for layer {}: ".format(n)))
      activation = input("Enter activation function for layer {}: ".format(n))
      in_shape = int(input("Enter the number of input column shape: "))

      model.add(Dense(
          units=n_neurons,
          activation=activation,
          input_shape= (in_shape,)
      ))

      for i in range(iteration-1):
        n += 1  
        n_neurons = int(input("Enter the number of neurons for layer {}: ".format(n)))
        activation = input("Enter activation function for layer {}: ".format(n))
        model.add(Dense(
          units=n_neurons,
          activation=activation
        ))

      loss_func = input("Enter loss func: ")
      #"mean_squared_error"
      Optimizer = input("Optimizer: ")
      #"adam"
      model.compile(loss = loss_func , optimizer = Optimizer ,metrics=['accuracy'])

      e = int(input("Enter epoch: "))
      model.fit(x,y,epochs=e , validation_split = .2)

      while True:
        ch = int(input("""
1. To predict
2. Column names
3. Dataset
4. Dataset information
5. Layers details
6. Number of layers
7. Model weight
8. Exit
Enter your choice: """))
        if ch == 1:
          x_input = input("Enter your x values in order: ")
          list_x = list(x_input.split(","))
          int_x = [float(x) for x in list_x]
          y_pred = model.predict(int_x)
          os.system("tput setaf 34")
          print(y_pred)
          os.system("tput setaf 7")

        elif ch == 2:
          os.system("tput setaf 34")
          print(data.columns)
          os.system("tput setaf 7")

        elif ch == 3:
          os.system("tput setaf 34")
          print(data.head)
          os.system("tput setaf 7")

        elif ch == 4:
          os.system("tput setaf 34")
          print(data.info())
          os.system("tput setaf 7")

        elif ch == 5:
          os.system("tput setaf 34")
          print(model.get_config())
          os.system("tput setaf 7")

        elif ch == 6:
          os.system("tput setaf 34")
          print(model.summary())
          os.system("tput setaf 7")

        elif ch == 7:
          os.system("tput setaf 34")
          weight = model.get_weights()
          print(weight)
          os.system("tput setaf 7")

        elif ch == 8:
          break
        input("Press Enter to continue..........")
        os.system("clear")
    elif ch == 2:
        os.system("tput setaf 85")
        print("bye bye!!!!!!!!!!!")
        os.system("tput setaf 7")
        break
