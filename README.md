simple middle layer between __python flask app__ on backend and __html/js__ on front end using __socket.io__ websocket library

middle layer called __medium__ and it basically provides the next functionality:

on backend you can have:
```
import medium

medium.set('speed', 0)
```
to create/set variable called `speed` to 0;

then
```
@medium.subscribe('speed')
def speedUpdated(value):
    print('speed =', value)
```
to receive updates on `speed` value when it's changed by front end;


```
medium.listen('0.0.0.0', 5000)
``` 
starts __medium__ server as __flask app__ with __socket.io__ support

on front end __api__ is the same:

```
import { Medium } from './medium.js'

const medium = new Medium('http://' + document.domain + ':' + location.port);
```

then set value like this:
```
medium.set('speed', Number(0))
```

and updates are received like this:
```
medium.subscribe('speed', (value) => {
    console.log(value);
})
```