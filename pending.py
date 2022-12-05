from interface_alert import TransaccionState

class Pending(TransaccionState):
  def alert(self ):
    print('Pending...')
    
class Aceptada(TransaccionState):
  def alert(self):
    print('aceptada...')