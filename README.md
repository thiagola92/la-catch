# la-catch
Decorator and context manager to catch exception(s) and call a function to handle the error.  

# install
`pip install la-catch`  

# syntax
```python
Catch(exceptions, callback, *args, **kwargs)
```
`exceptions` - Exception or Tuple of exceptions to be captured  
`callback` - function to be called in case of exceptions being raised **or** a return value to be returned in case of exceptions  
`*args` - Any extra arguments are passed to **context manager** callback  
`**kwargs` - Any extra keywords are passed to **context manager** callback  

# usage
There is two ways to use `catch`:
- Context Manager
- Decorator

# context manager
Catch exception and do nothing:  
```python
from la_catch import Catch

def func():
    with Catch(TypeError):
        raise TypeError("example")
```

Catch exception and call callback passing exception:  
```python
from la_catch import Catch

def on_error(exception):
    print(exception)

def func():
    with Catch(TypeError, callback=on_error):
        raise TypeError("example")
```

Catch exception and call callback passing keywords arguments and exception:  
```python
from la_catch import Catch

def on_error(message, exception):
    print(message, exception)

def func():
    with Catch(TypeError, callback=on_error, message="WARNING:"):
        raise TypeError("example")
```

Catch multiple exceptions:  
```python
from la_catch import Catch

def func():
    with Catch((TypeError, FileNotFoundError)):
        raise FileNotFoundError("example")
```


# decorator
Catch exception and return `None`:  
```python
from la_catch import Catch

@Catch(TypeError)
def func():
    raise TypeError("example")
```

Catch exception and return a value:   
```python
from la_catch import Catch

@Catch(TypeError, callback=10)
def func():
    raise TypeError("example")
```

Catch exception and call callback passing exception:   
```python
from la_catch import Catch

def on_error(exception):
    print(exception)

@Catch(TypeError, callback=on_error)
def func():
    raise TypeError("example")
```

Catch exception and call callback passing decorated function arguments and exception:   
```python
from la_catch import Catch

def on_error(message, exception):
    print(message, exception)

@Catch(TypeError, callback=on_error)
def func(message="WARNING:"):
    raise TypeError("example")
```

Chain catchs:  
```python
from la_catch import Catch

def on_file_not_found_error(exception):
    print(exception)

def on_typerror(exception):
    print(exception)

@Catch(FileNotFoundError, callback=on_file_not_found_error)
@Catch(TypeError, callback=on_typerror)
def func():
    raise FileNotFoundError("example")
    raise TypeError("example")
```