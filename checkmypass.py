#Input any password that we have and check whether it has ever been hacked.

import requests #(Allows us to request for something )
import hashlib   #(Allows us to hash passwords on here)
import sys

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'  #URL API with first 5 char of hash password k-anonimity
res = requests.get(url)
print(res)

def read_response(response):
  print(response.text)

def get_password_leaks_count(hashes, hash_to_check):
  hashes=(line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
   if h== hash_to_check:
    return int(count)
  return 0
  password="password123"
  count = pwned_api_check(password)
def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
  return res

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response,tail)

def main(args):
  for password in args:
    count= pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times you should probably change your password!')
    else:
      print(f' {password} was not found! Carry On :)')
      return 'done!' 

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
