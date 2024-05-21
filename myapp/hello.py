import fire

def hello(name="World"):
  return "h3ll0 %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
