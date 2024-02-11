import fire

def hello(name="World"):
  return "Hello %s!\n How are you?" % name

if __name__ == '__main__':
  fire.Fire(hello)