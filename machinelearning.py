import os
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
      print("""
the output column name should be 'y'
      """)
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
          print(y_pred)

        elif ch == 2:
          print(data.columns)
        
        elif ch == 3:
          print(data.head)

        elif ch == 4:
          print(data.info())

        elif ch == 5:
          print(model.get_config())

        elif ch == 6:
          print(model.summary())

        elif ch == 7:
          weight = model.get_weights()
          print(weight)

        elif ch == 8:
          break
        input("Press Enter to continue..........")
        os.system("clear")
    elif ch == 2:
        print("bye bye!!!!!!!!!!!")
        break
