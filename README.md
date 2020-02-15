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
to connect to __medium__ server runing on backend;

then set value like this:
```
medium.set('speed', Number(0))
```
backend will receive update if subscribed to `speed` variable;

and updates are received like this:
```
medium.subscribe('speed', (value) => {
    console.log(value);
})
```
now whenever `speed` value changed by backend, frontend is notified;

the above allows for updating and receiving updates on values for both backend and frontend whenever values get
updated by either frontend or backend