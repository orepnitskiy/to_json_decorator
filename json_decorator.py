from functools import wraps


def to_json(func):
	
	
	@wraps(func)
	def wrapped(*args,**kwargs):
		func_result = func(*args,**kwargs)
		json_result = json.JSONEncoder().encode(func_result)
		return json_result
	return wrapped