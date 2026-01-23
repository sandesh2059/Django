import pickle
import io

listing = [ 1, 2, 3 ,4]

buffer = io.BytesIO()
pickle.dump(listing, buffer)

print(buffer.getvalue())
buffer.seek(0)

listing2 = pickle.load(buffer)
print(listing2)