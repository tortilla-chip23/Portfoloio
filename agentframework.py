import random
class agents:
 def __init__(self):
     
  def __init__(environment):
     self.environment = environment
     self.store = 0 # We'll come to this in a second
     
  for i in range(num_of_agents):     
   agents.append([random.randint(0,99),random.randint(0,99)])     
    
  
   for j in range(num_of_iterations):
     for i in range(num_of_agents):
         
 
      if random.random() < 0.5:
          agents[i][0] = (agents[i][0] + 1) % 100
      else:
          agents[i][0] = (agents[i][0] - 1) % 100

   if random.random() < 0.5:
      agents[i][1] = (agents[i][1] + 1) % 100
   else:
      agents[i][1] = (agents[i][1] - 1) % 100

def eat(self): # can you make it eat what is left?
     if self.environment[self.y][self.x] > 10:
         self.environment[self.y][self.x] -= 10
         self.store += 10 