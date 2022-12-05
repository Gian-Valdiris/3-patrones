from context import TransaccionContext
from pending import Aceptada,Pending
def main():
  state_context = TransaccionContext()
  state_context.alert()
  state_context.alert()
  state_context.alert()
  state_context.alert()
  state_context.alert()
  state_context.set_state(Aceptada())
  state_context.alert()
  state_context.set_state(Pending())
  state_context.alert()
main()