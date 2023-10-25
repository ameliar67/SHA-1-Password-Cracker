import hashlib


def crack_sha1_hash(hash, use_salts = False):

  
  def hashing(password):
    password = bytes(password, 'utf-8')
    sha256 = hashlib.sha1()
    sha256.update(password)
      
    return sha256.hexdigest()

  file = open('top-10000-passwords.txt')
  list = file.read()
  file.close()

  new_list = list.split()
  
  for password in new_list:
    file_hash = ''
    left_file_hash = ''
    right_file_hash = ''

    if use_salts == True:
      file = open('known-salts.txt')
      salts_to_add = file.read().split()
      file.close()
      for salt in salts_to_add:
        left_side_password = salt + password
        right_side_password = password + salt
        left_file_hash = hashing(left_side_password)
        right_file_hash = hashing(right_side_password)
        if left_file_hash == hash or right_file_hash == hash:
          return password
        else:
          continue
    else:
      file_hash = hashing(password)
  
      
      
    if file_hash == hash or left_file_hash == hash or right_file_hash == hash:
      return password
    else:
      continue
      
  
  return 'PASSWORD NOT IN DATABASE'



    
 