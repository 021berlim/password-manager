import string as st
import numpy as np

letters = st.ascii_letters
numbers = st.digits
special = st.punctuation
algarism =  letters+numbers+special
password = np.random.choice(list(algarism),30)
print(''.join(password))