# ex1-munche
We need to develop an algorithm that control elevators.
In off-line algorithm we get all the calls before the movements start.
the problem is to devide the calls between the elevators in the form that will lead to the minimum time pear call.
our research:
https://blog.birost.com/a?ID=00450-d7c47455-0bd9-42bd-bd9d-d790532c1010
https://en.wikipedia.org/wiki/Elevator_algorithm

off-line algorithm

count: read all the calls and divied them to up and down.
 devide the calls to two groups of ups and down.
 define dev_up = all calls/group calls_up,dev_down = all calls/group calls_down.
 el_up =  total elevators*dev_up,el_down = total elevators*dev_down.
 num_call_elv_up=calls_up/el_up,num_call_elv_down = calls_down/el_down.
  