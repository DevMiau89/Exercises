def p_decorate(func):
   def func_wrapper(name):
       return "<p>" + func(name) + "</p>"
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, " + name + " dolor sit amet"

print get_text("John")
