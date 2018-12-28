from functools import wraps
def to_json(func):
	@wraps(func)
	def wrapped(*args,**kwargs):
		result=func(*args,**kwargs)
		c=json.JSONEncoder().encode(result)
		print(c)
		return c
	return wrapped