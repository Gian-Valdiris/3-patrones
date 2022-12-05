
from interface_alert import TransaccionState
from pending import Pending,Aceptada


  
class TransaccionContext:
    
  def __init__(self) -> None:
    self.__current_state:TransaccionState = Pending()
    
  def set_state(self,state:TransaccionState):
    self.__current_state = state
  
  def alert(self):
    self.__current_state.alert()

    
