from werkzeug.security import generate_password_hash,check_password_hash
# print (generate_password_hash("@dmin&$iet", "sha256"))

data = "sha256$gV1b2TmF$45667b50f8464c1ec42e5bd81d0d35106f49f50f7027a89569cd0058fc28b517"
print (check_password_hash(data, "@dmin&$iet"))