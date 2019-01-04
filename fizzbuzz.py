def fizz(x):
  r=False
  if x%3==0:
    r=True
  else:
    r=False
  return r

def buzz(x):
  r=False
  if x%5==0:
    r=True
  else:
    r=False
  return r

def fizzbuzz(x):
  r="new"
  if not fizz(x)and not buzz(x):
    r=x
  else:
    if fizz(x):
      r="fizz"
    if buzz(x):
      r="buzz"
    if fizz(x) and buzz(x):
      r="fizzbuzz"
      
  return r


